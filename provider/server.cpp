// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include "server.hpp"


#include "debug_tags.hpp"
#include "mi_module_self.hpp"
#include "mi_script_extensions.hpp"
#include "server_protocol.hpp"
#include "repeat.hpp"
#include "unique_ptr.hpp"


#include <cassert>
#include <cctype>
#include <config.h>
#include <errno.h>
#include <fcntl.h>
#include <list>
#include <netinet/in.h>
#include <sstream>
#include <sys/select.h>
#include <sys/socket.h>
#include <unistd.h>


extern util::unique_ptr<Server> g_pServer;


namespace
{


typedef util::unique_ptr<char[]> char_array;


template<typename CHAR_t>
inline int
compare_case_insensitive (
    CHAR_t const* pLHS,
    CHAR_t const* pRHS)
{
    for (; *pLHS || *pRHS; ++pLHS, ++pRHS)
    {
        CHAR_t l = tolower (*pLHS);
        CHAR_t r = tolower (*pRHS);
        if (l != r)
        {
            return l < r ? -1 : 1;
        }
    }
    return 0;
}


class ClassFinder
{
public:
    /*ctor*/ ClassFinder (MI_Char const* const name)
        : m_Name (name) {}

    bool operator () (MI_ClassDecl const* pClass)
    {
#if (PRINT_BOOKENDS)
        SCX_BOOKEND ("ClassFinder::operator ()");
        std::ostringstream strm;
        strm << "m_Name: \"" << m_Name << '\"';
        SCX_BOOKEND_PRINT (strm.str ());
        strm.str ("");
        strm.clear ();
        strm << "pClass->name: \"" << pClass->name << '\"';
        SCX_BOOKEND_PRINT (strm.str ());
#endif
        return 0 == compare_case_insensitive (m_Name.c_str (), pClass->name);
    }

private:
    std::string const m_Name;
};


class MethodFinder
{
public:
    /*ctor*/ MethodFinder (MI_Char const* const name)
        : m_Name (name) {}

    bool operator () (MI_MethodDecl const* pMethod)
    {
#if (PRINT_BOOKENDS)
        SCX_BOOKEND ("MethodFinder::operator ()");
        std::ostringstream strm;
        strm << "m_Name: \"" << m_Name << '\"';
        SCX_BOOKEND_PRINT (strm.str ());
        strm.str ("");
        strm.clear ();
        strm << "pMethod->name: \"" << pMethod->name << '\"';
        SCX_BOOKEND_PRINT (strm.str ());
        strm.str ("");
        strm.clear ();
        strm << (m_Name == pMethod->name ? "Equal" : "Not Equal");
        SCX_BOOKEND_PRINT (strm.str ());
#endif
        return m_Name == pMethod->name;
    }

private:
    std::string const m_Name;
};


MI_MethodDecl const*
findMethodDecl (
    MI_ClassDeclEx const* const pClassDecl,
    MI_Char const* const methodName)
{
    SCX_BOOKEND ("findMethodDecl");
    MI_MethodDecl const* const* ppMethodDecl =
        std::find_if (
            pClassDecl->methods,
            pClassDecl->methods + pClassDecl->numMethods,
            MethodFinder (methodName));
    return ppMethodDecl != (pClassDecl->methods + pClassDecl->numMethods) ?
        *ppMethodDecl : NULL;
}


int
handle_post_instance (
    MI_Context* const pContext,
    MI_SchemaDecl const* const pSchema,
    MI_Filter const* const pFilter,
    socket_wrapper& sock)
{
    SCX_BOOKEND ("handle_post_instance");
    int rval = socket_wrapper::SUCCESS;
    MI_Instance* pInstance = NULL;
    if (socket_wrapper::SUCCESS == (
            rval = (protocol::recv (&pInstance, pContext, pSchema, sock))))
    {
        SCX_BOOKEND_PRINT ("recv instance succeeded");
        MI_Boolean post = MI_TRUE;
        if (NULL != pFilter)
        {
            if (MI_RESULT_OK == MI_Filter_Evaluate (pFilter, pInstance, &post))
            {
                if (MI_FALSE == post)
                {
                    SCX_BOOKEND_PRINT ("Filtered out");
                }
            }
            else
            {
                SCX_BOOKEND_PRINT ("MI_Filter_Evaluate failed");
                post = MI_FALSE;
            }
        }
        if (MI_FALSE != post)
        {
            if (MI_RESULT_OK == MI_Context_PostInstance (pContext, pInstance))
            {
                SCX_BOOKEND_PRINT ("PostInstance succeeded");
            }
            else
            {
                SCX_BOOKEND_PRINT ("PostInstance failed");
            }
        }
        MI_Instance_Delete (pInstance);
    }
    else
    {
        SCX_BOOKEND_PRINT ("something went wrong");
    }
    return rval;
}


int
handle_post_result (
    MI_Context* const pContext,
    socket_wrapper& sock)
{
    SCX_BOOKEND ("handle_post_result");
    MI_Result result;
    int rval = protocol::recv (&result, sock);
    if (socket_wrapper::SUCCESS == rval)
    {
        SCX_BOOKEND_PRINT ("rec'd result");
        MI_Context_PostResult (pContext, result);
    }
    else
    {
        SCX_BOOKEND_PRINT ("recv result failed");
    }
    return rval;
}


int
handle_return (
    MI_Context* const pContext,
    MI_SchemaDecl const* const pSchema,
    MI_Filter const* const pFilter,
    socket_wrapper& sock)
{
    SCX_BOOKEND ("handle_return");
    int rval = socket_wrapper::SUCCESS;
    protocol::opcode_t opcode;
    do
    {
        rval = protocol::recv_opcode (&opcode, sock);
        if (socket_wrapper::SUCCESS == rval)
        {
            switch (opcode)
            {
            case protocol::POST_INSTANCE:
                SCX_BOOKEND_PRINT ("rec'ved POST_INSTANCE");
                rval = handle_post_instance (pContext, pSchema, pFilter, sock);
                break;
            case protocol::POST_RESULT:
                SCX_BOOKEND_PRINT ("rec'ved POST_RESULT");
                rval = handle_post_result (pContext, sock);
                break;
            default:
                SCX_BOOKEND_PRINT ("unexpected opcode");
                // todo: error
                break;
            }
        }
        else
        {
            SCX_BOOKEND_PRINT ("error receiving opcode");
            // todo: error
        }
    } while (socket_wrapper::SUCCESS == rval &&
             protocol::POST_RESULT != opcode);
    return rval;
}


void
close_listener_socket (
    int* fd)
{
    SCX_BOOKEND ("close_listener_socket");
    close (*fd);
}


void
generate_key (
    unsigned int (&key)[4])
{
    srand (time (0));
    for (int i = 0; i < 4; ++i)
    {
        key[i] = 0;
        for (int j = 0; j < 4; ++j)
        {
            key[i] |= static_cast<unsigned int>(
                static_cast<unsigned char> (rand () % 0xff) << (8 * j));
        }
    }
}


int
create_listener (
    unsigned short* pPortOut,
    int* pListenerFDOut)
{
    SCX_BOOKEND ("create_listener");
    assert (pPortOut);
    assert (pListenerFDOut);
    int result = Server::LISTEN_SOCKET_FAILED;
    util::unique_ptr<int, void (*)(int*)> listener_holder (NULL, close_listener_socket);
    int listener_fd = socket (AF_INET, SOCK_STREAM, 0);
    if (-1 != listener_fd)
    {
        listener_holder.reset (&listener_fd);
        int flags = fcntl (listener_fd, F_GETFL, 0);
        if (-1 != flags &&
            -1 != fcntl (listener_fd, F_SETFL, flags | O_NONBLOCK))
        {
            sockaddr_in addr;
            memset (&addr, 0, sizeof (addr));
            addr.sin_family = AF_INET;
            addr.sin_addr.s_addr = INADDR_ANY;
            unsigned short port = 5999;
            int local_result;
            do
            {
                ++port;
                addr.sin_port = htons (port);
                local_result =
                    bind (listener_fd, reinterpret_cast<sockaddr*>(&addr),
                          sizeof (addr));
            } while (-1 == local_result &&
                     EADDRINUSE == errno);
            if (0 == local_result)
            {
                local_result = listen (listener_fd, 5);
                if (0 == local_result)
                {
                    *pPortOut = port;
                    *pListenerFDOut = listener_fd;
                    listener_holder.release ();
                    result = Server::SUCCESS;
                }
#if (PRINT_BOOKENDS)
                else
                {
                    std::ostringstream strm;
                    strm << "listen failed: " << errnoText;
                    SCX_BOOKEND_PRINT (strm.str ().c_str ());
                }
            }
            else
            {
                std::ostringstream strm;
                strm << "bind failed: " << errnoText;
                SCX_BOOKEND_PRINT (strm.str ().c_str ());
            }
        }
        else
        {
            std::ostringstream strm;
            strm << "set flags for bind socket failed: " << errnoText;
            SCX_BOOKEND_PRINT (strm.str ().c_str ());
        }
    }
    else
    {
        std::ostringstream strm;
        strm << "create socket failed: " << errnoText;
        SCX_BOOKEND_PRINT (strm.str ().c_str ());
    }
#else // PRINT_BOOKENDS
            }
        }
    }
#endif // PRINT_BOOKENDS
    return result;
}


class pending_client
{
public:
    enum Result
    {
        VALID,
        INVALID,
        INCOMPLETE,
    };

    /*ctor*/ pending_client (int fd)
        : m_remaining (sizeof (m_key))
        , m_fd (fd)
    {
        SCX_BOOKEND ("pending_client::ctor");
        memset (m_key, 0, sizeof (m_key));
    }

    int get_fd () { return m_fd; }
    void close_socket ()
    {
        SCX_BOOKEND ("pending_client::close_socket");
        close (m_fd);
    }
    int read_and_validate (unsigned int (&key)[4]);

private:
    unsigned int m_key[4];
    ssize_t m_remaining;
    int m_fd;
};


int
pending_client::read_and_validate (
    unsigned int (&key)[4])
{
    SCX_BOOKEND ("pending_client::read_and_validate");
    int result = INCOMPLETE;
    if (0 < m_remaining)
    {
        ssize_t nRead = read (
            m_fd,
            reinterpret_cast<unsigned char*>(
                m_key) + (sizeof (m_key) - m_remaining),
            m_remaining);
        if (0 < nRead)
        {
            m_remaining -= nRead;
        }
        else if (EINTR != errno ||
                 0 == nRead)
        {
            SCX_BOOKEND_PRINT ("error on read");
            close (m_fd);
            result = INVALID;
        }
    }
    if (0 == m_remaining)
    {
        result = std::equal (key, key + 4, m_key) ? VALID : INVALID;
        if (VALID == result)
        {
            SCX_BOOKEND_PRINT ("VALID");
        }
        else
        {
            SCX_BOOKEND_PRINT ("INVALID");
        }
    }
    return result;
}


int
accept_socket (
    int listenerFD,
    std::list<pending_client>* pPendingClients)
{
    SCX_BOOKEND ("accept_socket");
    int result = EXIT_SUCCESS;
    bool done = false;
    do
    {
        sockaddr_in addr;
        socklen_t addrlen = sizeof (addr);
        int fd = accept (listenerFD, reinterpret_cast<sockaddr*>(&addr),
                         &addrlen);
        if (-1 != fd)
        {
            int flags = fcntl (fd, F_GETFL, 0);
            if (-1 != flags &&
                -1 != fcntl (fd, F_SETFL, flags | O_NONBLOCK))
            {
                pPendingClients->push_back (pending_client (fd));
            }
            else
            {
                // failed to set the socket to non-blocking
                SCX_BOOKEND_PRINT ("failed to set new socket to non-blocking");
                close (fd);
            }
        }
        else
        {
            // out of sockets to accept
            done = true;
            if (EAGAIN != errno && EWOULDBLOCK != errno)
            {
#if (PRINT_BOOKENDS)
                std::ostringstream strm;
                strm << "accept_socket: error on accept - " << errnoText;
                SCX_BOOKEND_PRINT (strm.str ());
#endif
                result = EXIT_FAILURE;
            }
        }
    } while (!done);
    return result;
}


int
wait_for_client (
    int listenerFD,
    unsigned int (&key)[4],
    int* pClientFDOut)
{
    SCX_BOOKEND ("wait_for_client");
    int result = Server::CLIENT_FAILED_TO_CONNECT;
    std::list<pending_client> pendingClients;
    timeval tv;
    tv.tv_sec = 5;
    tv.tv_usec = 0;
    bool done = false;
    while (!done)
    {
        // create the fd set
        int maxfd = listenerFD;
        fd_set read_fds;
        FD_ZERO (&read_fds);
        FD_SET (listenerFD, &read_fds);
        for (std::list<pending_client>::iterator
                 pos = pendingClients.begin (), end = pendingClients.end ();
             pos != end;
             ++pos)
        {
            FD_SET (pos->get_fd (), &read_fds);
            maxfd = std::max (maxfd, pos->get_fd ());
        }
        int count = select (maxfd + 1, &read_fds, NULL, NULL, &tv);
        if (0 < count)
        {
            std::list<pending_client>::iterator pos = pendingClients.begin ();
            std::list<pending_client>::iterator endPos = pendingClients.end ();
            while (!done &&
                   0 < count &&
                   pos != endPos)
            {
                --count;
                if (FD_ISSET (pos->get_fd (), &read_fds))
                {
                    switch (pos->read_and_validate (key))
                    {
                    case pending_client::VALID:
                    {
                        done = true;
                        *pClientFDOut = pos->get_fd ();
                        int flags = fcntl (*pClientFDOut, F_GETFL, 0);
                        if (-1 != flags &&
                            -1 != fcntl (*pClientFDOut, F_SETFL,
                                         flags ^ O_NONBLOCK))
                        {
                            result = Server::SUCCESS;
                            pendingClients.erase (pos);
                        }
                        else
                        {
                            SCX_BOOKEND_PRINT (
                                "failed to reset socket to blocking");
                            *pClientFDOut = socket_wrapper::INVALID_SOCKET;
                        }
                        break;
                    }
                    case pending_client::INVALID:
                    {
                        std::list<pending_client>::iterator nextPos = pos;
                        ++nextPos;
                        close (pos->get_fd ());
                        pendingClients.erase (pos);
                        pos = nextPos;
                        break;
                    }
                    case pending_client::INCOMPLETE:
                        ++pos;
                        break;
                    }
                }
            }
            if (!done &&
                0 < count &&
                FD_ISSET (listenerFD, &read_fds))
            {
                // accept
                if (EXIT_SUCCESS !=
                    accept_socket (listenerFD, &pendingClients))
                {
                    done = true;
                }
            }
        }
        else
        {
            done = true;
#if (PRINT_BOOKENDS)
            if (0 > count)
            {
                std::ostringstream strm;
                strm << "error: " << errnoText;
                SCX_BOOKEND_PRINT (strm.str ());
            }
            else
            {
                SCX_BOOKEND_PRINT ("timed out");
            }
#endif
        }
    }
    //close all of the remaining sockets
    for (std::list<pending_client>::iterator pos = pendingClients.begin (),
             end = pendingClients.end ();
         pos != end;
         ++pos)
    {
        close (pos->get_fd ());
    }
    return result;
}


} // namespace (unnamed)


#define _COUNT 25


#define LOAD_DEF(I) \
MI_EXTERN_C void \
MI_CALL Load##I ( \
    void** ppSelf, \
    MI_Module_Self* pSelfModule, \
    MI_Context* pContext) \
{ \
    pSelfModule->pServer->Load (I, ppSelf, pSelfModule, pContext); \
}

#define LOAD_DECL(I) Load##I,

REPEAT (_COUNT, LOAD_DEF)

MI_ProviderFT_Load LoadFunctions[] = {
    REPEAT (_COUNT, LOAD_DECL)
};


#define UNLOAD_DEF(I) \
MI_EXTERN_C void \
MI_CALL Unload##I ( \
    void* pSelf, \
    MI_Context* pContext) \
{ \
    reinterpret_cast<MI_Module_Self*>(pSelf)->pServer->Unload ( \
        I, pSelf, pContext); \
}

#define UNLOAD_DECL(I) Unload##I,

REPEAT (_COUNT, UNLOAD_DEF)

MI_ProviderFT_Unload UnloadFunctions[] = {
    REPEAT (_COUNT, UNLOAD_DECL)
};


/*ctor*/
Server::Server (
    std::string interpreter,
    std::string startup,
    std::string moduleName)
    : m_Interpreter (interpreter)
    , m_Startup (startup)
    , m_ModuleName (moduleName)
    , m_pSocket ()
    , m_pSchemaDecl ()
{
    SCX_BOOKEND ("Server::ctor");
}


/*dtor*/
Server::~Server ()
{
    SCX_BOOKEND ("Server::dtor");
}


int
Server::open ()
{
    int rval = Server::SUCCESS;
    if (!m_pSocket)
    {
        rval = init ();
    }
    return rval;
}


void
Server::setSchema (
    MI_SchemaDecl const* const pSchema)
{
    if (pSchema)
    {
        m_ClassNames.reserve (pSchema->numClassDecls);
        for (MI_Uint32 i = 0; i < pSchema->numClassDecls; ++i)
        {
            MI_ClassDecl const* pClass = pSchema->classDecls[i];
            m_ClassNames.push_back (pClass->name);
            if (NULL != pClass->providerFT)
            {
                const_cast<MI_ProviderFT*>(pClass->providerFT)->Load =
                    LoadFunctions[i];
                const_cast<MI_ProviderFT*>(pClass->providerFT)->Unload =
                    UnloadFunctions[i];
            }
        }
    }
    m_pSchemaDecl.reset (pSchema);
}


MI_ClassDeclEx const*
Server::findClassDecl (
    MI_Char const* const className)
{
    SCX_BOOKEND ("Server::findClassDecl");
    MI_ClassDecl const* const* ppClassDecl =
        std::find_if (
            m_pSchemaDecl->classDecls,
            m_pSchemaDecl->classDecls + m_pSchemaDecl->numClassDecls,
            ClassFinder (className));
    return (ppClassDecl != (
        m_pSchemaDecl->classDecls + m_pSchemaDecl->numClassDecls) ?
        static_cast<MI_ClassDeclEx const*>(*ppClassDecl) : NULL);
}


void
Server::Module_Load (
    MI_Module_Self** ppSelf,
    struct _MI_Context* pContext)
{
    SCX_BOOKEND ("Server::Module_Load");
    int rval = protocol::send_opcode (protocol::MODULE_LOAD, *m_pSocket);
    if (socket_wrapper::SUCCESS == rval)
    {
        protocol::opcode_t opcode;
        rval = protocol::recv_opcode (&opcode, *m_pSocket);
        if (socket_wrapper::SUCCESS == rval)
        {
            if (protocol::POST_RESULT == opcode)
            {
                SCX_BOOKEND_PRINT ("rec'ved POST_RESULT");
                rval = handle_post_result (pContext, *m_pSocket);
            }
            else
            {
                SCX_BOOKEND_PRINT ("rec'd unhandled opcode");
                // todo: error
            }
        }
        else
        {
            SCX_BOOKEND_PRINT ("socket error");
            // socket error
            // todo: error
        }
    }
    if (socket_wrapper::SUCCESS != rval)
    {
        MI_Context_PostResult (pContext, MI_RESULT_FAILED);
    }
}


void
Server::Module_Unload (
    MI_Module_Self* pSelf,
    struct _MI_Context* pContext)
{
    SCX_BOOKEND ("Server::Module_Unload");
    int rval = protocol::send_opcode (protocol::MODULE_UNLOAD, *m_pSocket);
    if (socket_wrapper::SUCCESS == rval)
    {
        protocol::opcode_t opcode;
        rval = protocol::recv_opcode (&opcode, *m_pSocket);
        if (socket_wrapper::SUCCESS == rval)
        {
            if (protocol::POST_RESULT == opcode)
            {
                SCX_BOOKEND_PRINT ("rec'ved POST_RESULT");
                rval = handle_post_result (pContext, *m_pSocket);
            }
            else
            {
                SCX_BOOKEND_PRINT ("rec'd unhandled opcode");
                // todo: error
            }
        }
        else
        {
            SCX_BOOKEND_PRINT ("socket error");
            // socket error
            // todo: error
        }
    }
    if (socket_wrapper::SUCCESS != rval)
    {
        MI_Context_PostResult (pContext, MI_RESULT_FAILED);
    }
}


void
Server::Load (
    size_t const& index,
    void** ppSelf,
    MI_Module_Self* pSelfModule,
    MI_Context* pContext)
{
    SCX_BOOKEND ("Server::Load (index)");
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << "index: " << index;
    SCX_BOOKEND_PRINT (strm.str ());
    strm.str ("");
    strm.clear ();
    strm << "class: " << m_ClassNames[index];
    SCX_BOOKEND_PRINT (strm.str ());
#endif
    *ppSelf = pSelfModule;
    int rval = SUCCESS;
    if (socket_wrapper::SUCCESS == (
            rval = protocol::send_opcode (protocol::CLASS_LOAD, *m_pSocket)) &&
        socket_wrapper::SUCCESS == (
            rval = protocol::send (m_ClassNames[index], *m_pSocket)))
    {
        protocol::opcode_t opcode;
        rval = protocol::recv_opcode (&opcode, *m_pSocket);
        if (socket_wrapper::SUCCESS == rval)
        {
            if (protocol::POST_RESULT == opcode)
            {
                SCX_BOOKEND_PRINT ("rec'ved POST_RESULT");
                rval = handle_post_result (pContext, *m_pSocket);
            }
            else
            {
                SCX_BOOKEND_PRINT ("rec'd unhandled opcode");
                // todo: error
            }
        }
        else
        {
            SCX_BOOKEND_PRINT ("socket error");
            // socket error
            // todo: error
        }
    }
    if (SUCCESS != rval)
    {
        MI_Context_PostResult (pContext, MI_RESULT_FAILED);
    }
}


void
Server::Unload (
    size_t const& index,
    void* pSelf,
    MI_Context* pContext)
{
    SCX_BOOKEND ("Server::Unload (index)");
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << "index: " << index;
    SCX_BOOKEND_PRINT (strm.str ());
    strm.str ("");
    strm.clear ();
    strm << "class: " << m_ClassNames[index];
    SCX_BOOKEND_PRINT (strm.str ());
#endif
    int rval = SUCCESS;
    if (socket_wrapper::SUCCESS == (
            rval = protocol::send_opcode (protocol::CLASS_UNLOAD, *m_pSocket)) &&
        socket_wrapper::SUCCESS == (
            rval = protocol::send (m_ClassNames[index], *m_pSocket)))
    {
        protocol::opcode_t opcode;
        rval = protocol::recv_opcode (&opcode, *m_pSocket);
        if (socket_wrapper::SUCCESS == rval)
        {
            if (protocol::POST_RESULT == opcode)
            {
                SCX_BOOKEND_PRINT ("rec'ved POST_RESULT");
                rval = handle_post_result (pContext, *m_pSocket);
            }
            else
            {
                SCX_BOOKEND_PRINT ("rec'd unhandled opcode");
                // todo: error
            }
        }
        else
        {
            SCX_BOOKEND_PRINT ("socket error");
            // socket error
            // todo: error
        }
    }
    if (SUCCESS != rval)
    {
        MI_Context_PostResult (pContext, MI_RESULT_FAILED);
    }
}


void
Server::EnumerateInstances (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_PropertySet const* pPropertySet,
    MI_Boolean keysOnly,
    MI_Filter const* pFilter)
{
    SCX_BOOKEND ("Server::EnumerateInstances");
    int rval = SUCCESS;
    MI_ClassDeclEx const* pClassDecl = findClassDecl (className);
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << "namespace: \"" << nameSpace << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    strm.str ("");
    strm.clear ();
    strm << "className: \"" << className << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    if (NULL == pClassDecl)
    {
        SCX_BOOKEND_PRINT ("classDecl was NOT found");
    }
#endif
    if (NULL != pClassDecl)
    {
        if (SUCCESS == open () &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send_opcode (
                    protocol::ENUMERATE_INSTANCES, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (nameSpace, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (className, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (pPropertySet, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send_boolean (keysOnly, *m_pSocket)))
        {
            rval = handle_return (pContext, m_pSchemaDecl.get (), pFilter,
                                  *m_pSocket);
        }
        if (SUCCESS != rval)
        {
            SCX_BOOKEND_PRINT ("send FAILED somewhere");
            MI_Context_PostResult (pContext, MI_RESULT_FAILED);
        }
    }
    else
    {
        MI_Context_PostResult (pContext, MI_RESULT_INVALID_CLASS);
    }
}


void
Server::GetInstance (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Instance const* pInstanceName,
    MI_PropertySet const* pPropertySet)
{
    SCX_BOOKEND ("Server::GetInstance");
    int rval = SUCCESS;
    MI_ClassDeclEx const* pClassDecl = findClassDecl (className);
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << "namespace: \"" << nameSpace << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    strm.str ("");
    strm.clear ();
    strm << "className: \"" << className << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    if (NULL == pClassDecl)
    {
        SCX_BOOKEND_PRINT ("classDecl was NOT found");
    }
#endif
    if (NULL != pInstanceName &&
        NULL != pClassDecl)
    {
        // skipping: nameSpace, pPropertySet
        if (socket_wrapper::SUCCESS == (
                rval = protocol::send_opcode (
                    protocol::GET_INSTANCE, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (nameSpace, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (className, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (*pInstanceName, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (pPropertySet, *m_pSocket)))
        {
            rval = handle_return (pContext, m_pSchemaDecl.get (), NULL,
                                  *m_pSocket);
        }
        if (SUCCESS != rval)
        {
            MI_Context_PostResult (pContext, MI_RESULT_FAILED);
        }
    }
    else
    {
        MI_Context_PostResult (pContext, MI_RESULT_INVALID_CLASS);
    }
}


void
Server::CreateInstance (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Instance const* pNewInstance)
{
    SCX_BOOKEND ("Server::CreateInstance");
    int rval = SUCCESS;
    MI_ClassDeclEx const* pClassDecl = findClassDecl (className);
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << "namespace: \"" << nameSpace << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    strm.str ("");
    strm.clear ();
    strm << "className: \"" << className << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    if (NULL == pClassDecl)
    {
        SCX_BOOKEND_PRINT ("classDecl was NOT found");
    }
#endif
    if (NULL != pNewInstance &&
        NULL != pClassDecl)
    {
        // skipping: nameSpace
        if (socket_wrapper::SUCCESS == (
                rval = protocol::send_opcode (
                    protocol::CREATE_INSTANCE, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (nameSpace, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (className, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (*pNewInstance, *m_pSocket)))
        {
            protocol::opcode_t opcode;
            rval = protocol::recv_opcode (&opcode, *m_pSocket);
            if (socket_wrapper::SUCCESS == rval)
            {
                if (protocol::POST_RESULT == opcode)
                {
                    SCX_BOOKEND_PRINT ("rec'ved POST_RESULT");
                    rval = handle_post_result (pContext, *m_pSocket);
                }
                else
                {
                    SCX_BOOKEND_PRINT ("rec'd unhandled opcode");
                    // todo: error
                }
            }
            else
            {
                SCX_BOOKEND_PRINT ("socket error");
                // socket error
                // todo: error
            }
        }
        if (SUCCESS != rval)
        {
            MI_Context_PostResult (pContext, MI_RESULT_FAILED);
        }
    }
    else
    {
        MI_Context_PostResult (pContext, MI_RESULT_INVALID_CLASS);
    }
}


void
Server::ModifyInstance (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Instance const* pModifiedInstance,
    MI_PropertySet const* pPropertySet)
{
    SCX_BOOKEND ("Server::ModifyInstance");
    int rval = SUCCESS;
    MI_ClassDeclEx const* pClassDecl = findClassDecl (className);
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << "namespace: \"" << nameSpace << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    strm.str ("");
    strm.clear ();
    strm << "className: \"" << className << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    if (NULL == pClassDecl)
    {
        SCX_BOOKEND_PRINT ("classDecl was NOT found");
    }
#endif
    if (NULL != pModifiedInstance &&
        NULL != pClassDecl)
    {
        // skipping: nameSpace, pPropertySet
        if (socket_wrapper::SUCCESS == (
                rval = protocol::send_opcode (
                    protocol::MODIFY_INSTANCE, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (nameSpace, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (className, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (*pModifiedInstance, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (pPropertySet, *m_pSocket)))
        {
            protocol::opcode_t opcode;
            rval = protocol::recv_opcode (&opcode, *m_pSocket);
            if (socket_wrapper::SUCCESS == rval)
            {
                if (protocol::POST_RESULT == opcode)
                {
                    SCX_BOOKEND_PRINT ("rec'ved POST_RESULT");
                    rval = handle_post_result (pContext, *m_pSocket);
                }
                else
                {
                    SCX_BOOKEND_PRINT ("rec'd unhandled opcode");
                    // todo: error
                }
            }
            else
            {
                SCX_BOOKEND_PRINT ("socket error");
                // socket error
                // todo: error
            }
        }
        if (SUCCESS != rval)
        {
            MI_Context_PostResult (pContext, MI_RESULT_FAILED);
        }
    }
    else
    {
        MI_Context_PostResult (pContext, MI_RESULT_INVALID_CLASS);
    }
}


void
Server::DeleteInstance (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Instance const* pInstanceName)
{
    SCX_BOOKEND ("Server::DeleteInstance");
    int rval = SUCCESS;
    MI_ClassDeclEx const* pClassDecl = findClassDecl (className);
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << "namespace: \"" << nameSpace << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    strm.str ("");
    strm.clear ();
    strm << "className: \"" << className << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    if (NULL == pClassDecl)
    {
        SCX_BOOKEND_PRINT ("classDecl was NOT found");
    }
#endif
    if (NULL != pInstanceName &&
        NULL != pClassDecl)
    {
        // skipping: nameSpace
        if (socket_wrapper::SUCCESS == (
                rval = protocol::send_opcode (
                    protocol::DELETE_INSTANCE, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (nameSpace, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (className, *m_pSocket)) &&
            socket_wrapper::SUCCESS == (
                rval = protocol::send (*pInstanceName, *m_pSocket)))
        {
            protocol::opcode_t opcode;
            rval = protocol::recv_opcode (&opcode, *m_pSocket);
            if (socket_wrapper::SUCCESS == rval)
            {
                if (protocol::POST_RESULT == opcode)
                {
                    SCX_BOOKEND_PRINT ("rec'ved POST_RESULT");
                    rval = handle_post_result (pContext, *m_pSocket);
                }
                else
                {
                    SCX_BOOKEND_PRINT ("rec'd unhandled opcode");
                    // todo: error
                }
            }
            else
            {
                SCX_BOOKEND_PRINT ("socket error");
                // socket error
                // todo: error
            }
        }
        if (SUCCESS != rval)
        {
            MI_Context_PostResult (pContext, MI_RESULT_FAILED);
        }
    }
    else
    {
        MI_Context_PostResult (pContext, MI_RESULT_INVALID_CLASS);
    }
}


void
Server::Invoke (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Char const* methodName,
    MI_Instance const* pInstance,
    MI_Instance const* pInputParameters)
{
    SCX_BOOKEND ("Server::Invoke");
    int rval = SUCCESS;
    MI_ClassDeclEx const* pClassDecl = findClassDecl (className);
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << "namespace: \"" << nameSpace << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    strm.str ("");
    strm.clear ();
    strm << "className: \"" << className << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
    strm.str ("");
    strm.clear ();
    strm << "methodName: \"" << methodName << '\"';
    SCX_BOOKEND_PRINT (strm.str ());
#endif
    if (NULL != pClassDecl)
    {
        MI_MethodDecl const* pMethodDecl =
            findMethodDecl (pClassDecl, methodName);
        if (NULL != pMethodDecl)
        {
            SCX_BOOKEND_PRINT ("class and method where found");
            MI_Uint32 flags =
                (pInstance ? protocol::HAS_INSTANCE_FLAG : 0) |
                (pInputParameters ? protocol::HAS_INPUT_PARAMETERS_FLAG : 0);
            {
                SCX_BOOKEND ("send opcode");
                rval = protocol::send_opcode (protocol::INVOKE, *m_pSocket);
            }
            if (socket_wrapper::SUCCESS == rval)
            {
                SCX_BOOKEND ("send namespace");
                rval = protocol::send (nameSpace, *m_pSocket);
            }
            if (socket_wrapper::SUCCESS == rval)
            {
                SCX_BOOKEND ("send class name");
                rval = protocol::send (className, *m_pSocket);
            }
            if (socket_wrapper::SUCCESS == rval)
            {
                SCX_BOOKEND ("send method name");
                rval = protocol::send (methodName, *m_pSocket);
            }
            if (socket_wrapper::SUCCESS == rval)
            {
                SCX_BOOKEND ("send flags");
                rval = protocol::send (flags, *m_pSocket);
            }
            if (socket_wrapper::SUCCESS == rval)
            {
                SCX_BOOKEND ("send instance");
                if (NULL != pInstance)
                {
                    SCX_BOOKEND_PRINT ("pInstance is not NULL");
                    rval = protocol::send (*pInstance, *m_pSocket);
                }
                else
                {
                    SCX_BOOKEND_PRINT ("pInstance is NULL");
                }
            }
            if (socket_wrapper::SUCCESS == rval)
            {
                SCX_BOOKEND ("send input parameters");
                if (NULL != pInputParameters)
                {
                    SCX_BOOKEND_PRINT ("pInputParameters is not NULL");
                    rval = protocol::send (*pInputParameters, *m_pSocket);
                }
                else
                {
                    SCX_BOOKEND_PRINT ("pInputParameters is NULL");
                }
            }
            if (socket_wrapper::SUCCESS == rval)
            {
                {
                    rval = handle_return (pContext, m_pSchemaDecl.get (), NULL,
                                          *m_pSocket);
                }
                if (SUCCESS != rval)
                {
                    MI_Context_PostResult (pContext, MI_RESULT_FAILED);
                }
            }
            else
            {
                SCX_BOOKEND_PRINT ("something failed");
                MI_Context_PostResult (pContext, MI_RESULT_FAILED);
            }
        }
        else 
        {
            SCX_BOOKEND_PRINT ("methodDecl was NOT found");
            MI_Context_PostResult (pContext, MI_RESULT_NOT_SUPPORTED);
        }
        if (SUCCESS != rval)
        {
            MI_Context_PostResult (pContext, MI_RESULT_FAILED);
        }
    }
    else
    {
        SCX_BOOKEND_PRINT ("classDecl was NOT found");
        MI_Context_PostResult (pContext, MI_RESULT_INVALID_CLASS);
    }
}


MI_EXTERN_C void
MI_CALL EnumerateInstances (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_PropertySet const* pPropertySet,
    MI_Boolean keysOnly,
    MI_Filter const* pFilter)
{
    reinterpret_cast<MI_Module_Self*>(pSelf)->pServer->EnumerateInstances (
        pSelf, pContext, nameSpace, className, pPropertySet, keysOnly, pFilter);
}


MI_EXTERN_C void
MI_CALL GetInstance (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Instance const* pInstanceName,
    MI_PropertySet const* pPropertySet)
{
    reinterpret_cast<MI_Module_Self*>(pSelf)->pServer->GetInstance (
        pSelf, pContext, nameSpace, className, pInstanceName, pPropertySet);
}


MI_EXTERN_C void
MI_CALL CreateInstance (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Instance const* pNewInstance)
{
    reinterpret_cast<MI_Module_Self*>(pSelf)->pServer->CreateInstance (
        pSelf, pContext, nameSpace, className, pNewInstance);
}


MI_CALL void
MI_CALL ModifyInstance (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Instance const* pModifiedInstance,
    MI_PropertySet const* pPropertySet)
{
    reinterpret_cast<MI_Module_Self*>(pSelf)->pServer->ModifyInstance (
        pSelf, pContext, nameSpace, className, pModifiedInstance, pPropertySet);
}


MI_CALL void
MI_CALL DeleteInstance (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Instance const* pInstanceName)
{
    reinterpret_cast<MI_Module_Self*>(pSelf)->pServer->DeleteInstance (
        pSelf, pContext, nameSpace, className, pInstanceName);
}


MI_EXTERN_C void
MI_CALL AssociatorInstances (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Instance const* pInstance,
    MI_Char const* resultClass,
    MI_Char const* role,
    MI_Char const* resultRole,
    MI_PropertySet const* pPropertySet,
    MI_Boolean keysOnly,
    MI_Filter const* pFilter)
{
    SCX_BOOKEND ("AssociatorInstances: server.cpp");
    SCX_BOOKEND_PRINT ("Not implemented!");
    MI_Context_PostResult (pContext, MI_RESULT_NOT_SUPPORTED);
}


MI_EXTERN_C void
MI_CALL ReferenceInstances (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Instance const* pInstance,
    MI_Char const* role,
    MI_PropertySet const* pPropertySet,
    MI_Boolean keysOnly,
    MI_Filter const* pFilter)
{
    SCX_BOOKEND ("ReferenceInstances: server.cpp");
    SCX_BOOKEND_PRINT ("Not implemented!");
    MI_Context_PostResult (pContext, MI_RESULT_NOT_SUPPORTED);
}


MI_EXTERN_C void
MI_CALL EnableIndications (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className)
{
    SCX_BOOKEND ("EnableIndications: server.cpp");
    SCX_BOOKEND_PRINT ("Not implemented!");
    MI_Context_PostResult (pContext, MI_RESULT_NOT_SUPPORTED);
}


MI_EXTERN_C void
MI_CALL DisableIndications (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className)
{
    SCX_BOOKEND ("DisableIndications: server.cpp");
    SCX_BOOKEND_PRINT ("Not implemented!");
    MI_Context_PostResult (pContext, MI_RESULT_NOT_SUPPORTED);
}


MI_EXTERN_C void
MI_CALL Subscribe (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Filter const* pFilter,
    MI_Char const* bookmark,
    MI_Uint64 subscriptionID,
    void** ppSubscriptionSelf)
{
    SCX_BOOKEND ("Subscribe: server.cpp");
    SCX_BOOKEND_PRINT ("Not implemented!");
    MI_Context_PostResult (pContext, MI_RESULT_NOT_SUPPORTED);
}


MI_EXTERN_C void
MI_CALL Unsubscribe (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Uint64 subscriptionID,
    void* pSubscriptionSelf)
{
    SCX_BOOKEND ("Unsubscribe: server.cpp");
    SCX_BOOKEND_PRINT ("Not implemented!");
    MI_Context_PostResult (pContext, MI_RESULT_NOT_SUPPORTED);
}


MI_EXTERN_C void
MI_CALL Invoke (
    void* pSelf,
    MI_Context* pContext,
    MI_Char const* nameSpace,
    MI_Char const* className,
    MI_Char const* methodName,
    MI_Instance const* pInstance,
    MI_Instance const* pInputParameters)
{
    SCX_BOOKEND ("Invoke: server.cpp");
    reinterpret_cast<MI_Module_Self*>(pSelf)->pServer->Invoke (
        pSelf, pContext, nameSpace, className, methodName, pInstance,
        pInputParameters);
}


int
Server::init ()
{
    int rval = SUCCESS;
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << " Module: \"" << m_ModuleName << "\" (libScriptProvider)";
    SCX_BOOKEND_EX ("Server::open", strm.str ());
#endif
    // generate a key
    unsigned int key[4];
    generate_key (key);
    // bind a socket
    unsigned short port;
    int listenerFD = socket_wrapper::INVALID_SOCKET;
    rval = create_listener (&port, &listenerFD);
    if (SUCCESS == rval)
    {
        util::unique_ptr<int, void (*)(int*)> listener_holder (
            &listenerFD, close_listener_socket);
        // fork
        int pid = fork ();
        if (0 == pid)
        {
            // fork succeded, this is the child process
            SCX_BOOKEND_PRINT ("fork - succeeded: this is the client");
            // close the parent socket
            listener_holder.reset ();
            // create the argument list including (path, port, key)
            char portStr[6];
            sprintf (portStr, "%hu", port);
            char keyStr[33];
            sprintf (keyStr, "%08X%08X%08X%08X", key[0], key[1], key[2], key[3]);
            char* args[] = { const_cast<char*>(m_Interpreter.c_str ()),
                             const_cast<char*>(m_Startup.c_str ()),
                             const_cast<char*>(m_ModuleName.c_str ()),
                             portStr,
                             keyStr,
                             0 };
            // exec
            chdir (CONFIG_LIBDIR);
            execvp (args[0], args);
            SCX_BOOKEND_PRINT ("execvp - failed");
            // if we got here, exec failed!
            // check errno { EACCES, ENOEXEC }
            std::ostringstream strm;
            strm << "Server::open - exec failed: " << errno << ": \""
                 << errnoText << '\"';
            SCX_BOOKEND_PRINT (strm.str ());
            std::cerr << strm.str () << std::endl;
            rval = FORK_FAILED;
        }
        else if (-1 != pid)
        {
            // fork succeeded, this is the parent process
            SCX_BOOKEND_PRINT ("fork - succeeded: this is the parent");
            int fd = socket_wrapper::INVALID_SOCKET;
            rval = wait_for_client (listenerFD, key, &fd);
            if (SUCCESS == rval)
            {
                m_pSocket = new socket_wrapper (fd);
            }
        }
        else
        {
            // fork failed
            // error (check errno { EAGAIN, ENOMEM })
            std::ostringstream strm;
            strm << "Server::open - fork failed: " << errno
                 << ": \"" << errnoText << '\"';
            SCX_BOOKEND_PRINT (strm.str ());
            std::cerr << strm.str () << std::endl;
            rval = FORK_FAILED;
        }
    }
    return rval;
}
