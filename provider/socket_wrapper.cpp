// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include "socket_wrapper.hpp"


#include "debug_tags.hpp"
#include "server.hpp"


#include <errno.h>
#include <fcntl.h>
#include <sstream>
#include <sys/socket.h>
#include <unistd.h>


namespace
{


}


/*ctor*/
socket_wrapper::socket_wrapper (
    int fd)
    : m_FD (fd)
{
    SCX_BOOKEND ("socket_wrapper::ctor");
}


/*dtor*/
socket_wrapper::~socket_wrapper ()
{
    SCX_BOOKEND ("socket_wrapper::dtor");
    if (INVALID_SOCKET != m_FD)
    {
        close ();
    }
}


int
socket_wrapper::send (
    byte_t const* const pData,
    size_t const& nBytes)
{
    //SCX_BOOKEND ("socket_wrapper::send");
    int rval = SUCCESS;
    if (INVALID_SOCKET != m_FD)
    {
        ssize_t nBytesSent = 0;
        while (SUCCESS == rval &&
               nBytes > static_cast<size_t> (nBytesSent))
        {
            ssize_t nSent = write (m_FD, pData + nBytesSent,
                                   nBytes - nBytesSent);
            if (-1 != nSent)
            {
                nBytesSent += nSent;
            }
            else if (EINTR != errno)
            {
                // error (check errno { EACCESS, EAGAIN, EWOULDBLOCK, EBADF,
                //                      ECONNRESET, EDESTADDRREQ, EFAULT,
                //                      EINVAL, EISCONN, EMSGSIZE, ENOBUFS,
                //                      ENOMEM, ENOTCONN, ENOTSOCK, EOPNOTSUPP,
                //                      EPIPE })
                close ();
                rval = SEND_FAILED;
                std::ostringstream strm;
                strm << "error on socket: (" << errno << ") \"" << errnoText
                     << '\"';
                SCX_BOOKEND_PRINT (strm.str ());
                std::cerr << strm.str () << std::endl;
            }
        }
    }
    else
    {
        SCX_BOOKEND_PRINT ("socket_wrapper::send called on closed socket");
        rval = SOCKET_CLOSED;
    }
    return rval;
}


int
socket_wrapper::recv (
    byte_t* const pDataOut,
    size_t const& nBytes)
{
    //SCX_BOOKEND ("socket_wrapper::recv");
    int rval = SUCCESS;
    if (INVALID_SOCKET != m_FD)
    {
        ssize_t nBytesRead = 0;
        while (SUCCESS == rval &&
               nBytes > static_cast<size_t> (nBytesRead))
        {
            ssize_t nRead = read (m_FD, pDataOut + nBytesRead,
                                  nBytes - nBytesRead);
            if (0 < nRead)
            {
                nBytesRead += nRead;
            }
            else if (0 == nRead)
            {
                // socket closed
                close ();
                rval = SOCKET_CLOSED;
                SCX_BOOKEND_PRINT ("recv - zero byte read");
            }
            else if (EINTR != errno)
            {
                // Error - check errno { EAGAIN, EBADF, EFAULT, EINVAL, EIO,
                //                       EISDIR }
                close ();
                rval = RECV_FAILED;
                std::ostringstream strm;
                strm << "error on socket: (" << errno << ") \"" << errnoText
                     << '\"';
                SCX_BOOKEND_PRINT (strm.str ());
                std::cerr << strm.str () << std::endl;
            }
    }
    }
    else
    {
        SCX_BOOKEND_PRINT ("socket_wrapper::recv called on closed socket");
        rval = SOCKET_CLOSED;
    }
    return rval;
}


void
socket_wrapper::close ()
{
    SCX_BOOKEND ("socket_wrapper::close");
    if (INVALID_SOCKET != m_FD)
    {
        ::close (m_FD);
        m_FD = INVALID_SOCKET;
    }
}
