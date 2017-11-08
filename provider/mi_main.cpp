// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include "debug_tags.hpp"
#include "server_protocol.hpp"
#include "server.hpp"
#include "unique_ptr.hpp"
#include "mi_module_self.hpp"
#include "mi_value.hpp"


#include <MI.h>
#include <sstream>


void
MI_CALL Load (
    MI_Module_Self** ppSelf,
    struct _MI_Context* pContext)
{
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << " ModuleName=\"" << (*ppSelf)->ModuleName << "\"";
    SCX_BOOKEND_EX ("Load: mi_main.cpp", strm.str ().c_str ());
#endif
    (*ppSelf)->pServer->Module_Load (ppSelf, pContext);
}


void
MI_CALL Unload (
    MI_Module_Self* pSelf,
    struct _MI_Context* pContext)
{
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << " ModuleName=\"" << pSelf->ModuleName << "\"";
    SCX_BOOKEND_EX ("Unload: mi_main.cpp", strm.str ().c_str ());
#endif
    pSelf->pServer->Module_Unload (pSelf, pContext);
    delete pSelf;
}


MI_EXTERN_C MI_EXPORT MI_Module*
Start (
    MI_Server* const pServer,
    char const* const interpreter,
    char const* const startup,
    char const* const moduleName,
    MI_Module_Self** ppSelf)
{
    SCX_BOOKEND ("Start: mi_main.cpp");
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << "interpreter: \"" << interpreter << "\"";
    SCX_BOOKEND_PRINT (strm.str ());
    strm.str ("");
    strm.clear ();
    strm << "startup: \"" << startup << "\"";
    SCX_BOOKEND_PRINT (strm.str ());
    strm.str ("");
    strm.clear ();
    strm << "moduleName: \"" << moduleName << "\"";
    SCX_BOOKEND_PRINT (strm.str ());
#endif
    util::unique_ptr<MI_Module_Self> pSelf (new MI_Module_Self (moduleName));
    pSelf->Module.version = MI_VERSION;
    pSelf->Module.generatorVersion = MI_MAKE_VERSION (1,0,8);
    pSelf->Module.flags =
        MI_MODULE_FLAG_STANDARD_QUALIFIERS |
        MI_MODULE_FLAG_CPLUSPLUS;
    pSelf->Module.charSize = sizeof (MI_Char);
    pSelf->Module.schemaDecl = NULL;
    pSelf->Module.Load = Load;
    pSelf->Module.Unload = Unload;
    pSelf->Module.dynamicProviderFT = NULL;
    pSelf->pServer.reset (new Server (interpreter, startup, moduleName));
    if (Server::SUCCESS == pSelf->pServer->open () &&
        socket_wrapper::SUCCESS ==
            protocol::recv (&(pSelf->Module.schemaDecl),
                            *(pSelf->pServer->getSocket ())))
    {
        pSelf->pServer->setSchema (pSelf->Module.schemaDecl);
        *ppSelf = pSelf.release ();
        return &((*ppSelf)->Module);
    }
    return NULL;
}
