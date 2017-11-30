// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include "client_wrapper.hpp"


#include "debug_tags.hpp"
#include "py_ptr.hpp"
#include "python_compatibility.hpp"
#include "shared.hpp"
#include "mi_module_wrapper.hpp"


#include <sstream>


#define VERBOSE 1


using namespace scx;


/*static*/ char const Client_Wrapper::NAME[] = "Client";
/*static*/ char const Client_Wrapper::OMI_NAME[] =
    "omi.Client";
/*static*/ char const Client_Wrapper::DOC[] =
    "omi.Client utility";
/*static*/ PyMethodDef Client_Wrapper::METHODS[] = {
    { "run", reinterpret_cast<PyCFunction>(Client_Wrapper::run),
      METH_NOARGS, "run the client" },
    { NULL, NULL, 0, NULL }
};


/*static*/ PyTypeObject Client_Wrapper::s_PyTypeObject = {};


/*static*/ void
Client_Wrapper::moduleInit (
    PyObject* const pModule)
{
    SCX_BOOKEND ("Client_Wrapper::moduleInit");
    Zero_PyTypeObject (&s_PyTypeObject);
    s_PyTypeObject.tp_name = OMI_NAME;
    s_PyTypeObject.tp_basicsize = sizeof (Client_Wrapper);
    s_PyTypeObject.tp_dealloc = dealloc;
    s_PyTypeObject.tp_flags = Py_TPFLAGS_DEFAULT;
    s_PyTypeObject.tp_doc = DOC;
    s_PyTypeObject.tp_init = init;
    s_PyTypeObject.tp_new = newObj;
    s_PyTypeObject.tp_alloc = PyType_GenericAlloc;
    s_PyTypeObject.tp_methods = METHODS;
    if (0 == PyType_Ready (&s_PyTypeObject))
    {
        Py_INCREF (&s_PyTypeObject);
        PyModule_AddObject (
            pModule, NAME, reinterpret_cast<PyObject*>(&s_PyTypeObject));
    }
}


/*static*/ void
Client_Wrapper::dealloc (
    PyObject* pObj)
{
    SCX_BOOKEND ("Client_Wrapper::dealloc");
    if (NULL != pObj)
    {
        Client_Wrapper* pDecl =
            reinterpret_cast<Client_Wrapper*>(pObj);
        pDecl->~Client_Wrapper ();
        Py_TYPE(pDecl)->tp_free (pObj);
    }
}


/*static*/ PyTypeObject const*
Client_Wrapper::getPyTypeObject ()
{
    return &s_PyTypeObject;
}


PyObject*
Client_Wrapper::newObj (
    PyTypeObject* pType,
    PyObject* args,
    PyObject* keywords)
{
    SCX_BOOKEND ("Client_Wrapper::newObj");
    PyObject* pObj = pType->tp_alloc (pType, 0);
    return pObj;
}


#if VERBOSE
#define CLIENT_INIT_VERBOSE 1
#else
#define CLIENT_INIT_VERBOSE 0
#endif

#if CLIENT_INIT_VERBOSE
#define CLIENT_INIT_BOOKEND(x) SCX_BOOKEND (x)
#define CLIENT_INIT_BOOKEND_PRINT(x) SCX_BOOKEND_PRINT (x)
#else
#define CLIENT_INIT_BOOKEND(x)
#define CLIENT_INIT_BOOKEND_PRINT(x)
#endif


int
Client_Wrapper::init (
    PyObject* pSelf,
    PyObject* args,
    PyObject* keywords)
{
    CLIENT_INIT_BOOKEND ("Create_Wrapper::init");
    int rval = 0;
#if (CLIENT_INIT_VERBOSE)
    std::ostringstream strm;
#endif
    // parse the args (path, port, key)
    char const* KEYWORDS[] = {
        "path",
        "port",
        "key",
        NULL
    };
    char const* path = NULL;
    unsigned int port = 0;
    char const* key = NULL;
    if (!PyArg_ParseTupleAndKeywords (
            args, keywords, "sIs", const_cast<char **>(KEYWORDS), &path, &port,
            &key))
    {
        CLIENT_INIT_BOOKEND_PRINT ("PyArg_ParseTuple failed");
        PyErr_SetString (PyExc_ValueError,
                         "ERROR: Client_Wrapper::init invalid arguments.");
        rval = -1;
    }
#if (CLIENT_INIT_VERBOSE)
    else
    {
        CLIENT_INIT_BOOKEND ("PyArg_ParseTuple succeeded");
        strm << "path: " << path;
        CLIENT_INIT_BOOKEND_PRINT (strm.str ().c_str ());
        strm.str ("");
        strm.clear ();
        strm << "port: " << port;
        CLIENT_INIT_BOOKEND_PRINT (strm.str ().c_str ());
        strm.str ("");
        strm.clear ();
        strm << "key: " << key;
        CLIENT_INIT_BOOKEND_PRINT (strm.str ().c_str ());
    }
#endif 
    // set the new path
    if (0 == rval)
    {
        PyObject* pSysPath = PySys_GetObject (const_cast<char *>("path"));
        PyObjPtr pNewPathItem (PyString_FromString (path));
        if (NULL == pSysPath ||
            0 > PyList_Append (pSysPath, pNewPathItem.release ()))
        {
            CLIENT_INIT_BOOKEND_PRINT ("ERROR: configuring sys.path");
            PyErr_SetString (PyExc_ValueError,
                             "ERROR: configuring sys.path");
            rval = -1;
        }
#if (CLIENT_INIT_VERBOSE)
        else
        {
            CLIENT_INIT_BOOKEND_PRINT ("sys.path:");
            strm.str ("");
            strm.clear ();
            for (Py_ssize_t i = 0, len = PyList_GET_SIZE (pSysPath);
                 i < len;
                 ++i)
            {
                PyObject* pPathItem = PyList_GET_ITEM (pSysPath, i);
                #if PY_MAJOR_VERSION >= 3
                    PyObject* tmp = PyUnicode_AsEncodedString (pPathItem, "utf-8", "strict");
                    strm << "    " << PyBytes_AsString (tmp);
                    Py_DECREF(tmp);
                #else
                    strm << "    " << PyString_AsString (pPathItem);
                #endif
                CLIENT_INIT_BOOKEND_PRINT (strm.str ().c_str ());
            }
        }
#endif
    }
    // open the module
    PyObjPtr pPythonModule;
    if (0 == rval)
    {
        pPythonModule.reset (PyImport_ImportModule ("mi_main"));
        if (!pPythonModule)
        {
            CLIENT_INIT_BOOKEND_PRINT ("ERROR: unable to import mi_main");
            PyErr_SetString (PyExc_ValueError,
                             "ERROR: unable to import mi_main");
            rval = -1;
        }
        else
        {
            CLIENT_INIT_BOOKEND_PRINT ("PyImport_ImportModule Succeeded");
        }
    }
    // find the entry point
    PyObject* pMain = NULL;
    if (0 == rval)
    {
        PyObject* pModuleDict = PyModule_GetDict (pPythonModule.get ());
        pMain = PyDict_GetItemString (pModuleDict, "mi_main");
        if (!pMain ||
            !PyCallable_Check (pMain))
        {
            if (!pMain)
            {
                CLIENT_INIT_BOOKEND_PRINT ("mi_main not found");
                PyErr_SetString (PyExc_ValueError, "mi_main not found");
            }
            else
            {
                CLIENT_INIT_BOOKEND_PRINT ("mi_main is not callable");
                PyErr_SetString (PyExc_ValueError,
                                 "mi_main object is not callable");
            }
            rval = -1;
        }
        else
        {
            CLIENT_INIT_BOOKEND_PRINT ("mi_main found and callable");
        }
    }
    // call the entry point to get the MI_Module_Wrapper
    PyObjPtr pModuleObj;
    if (0 == rval)
    {
        pModuleObj.reset (PyObject_CallObject (pMain, NULL));
        if (!pModuleObj ||
            !PyObject_TypeCheck (pModuleObj.get (),
                                 const_cast<PyTypeObject*>(
                                     MI_Module_Wrapper::getPyTypeObject ())))
        {
            CLIENT_INIT_BOOKEND_PRINT ("returned object is not MI_Module");
            PyErr_SetString (PyExc_ValueError,
                             "returned object is not MI_Module");
            rval = -1;
        }
        else
        {
            CLIENT_INIT_BOOKEND_PRINT ("returned object is MI_Module");
        }
    }
    // create the MI_Module
    scx::MI_Module::Ptr pModule;
    if (0 == rval)
    {
        MI_Module_Wrapper::PyPtr pModuleWrapper (
            reinterpret_cast<MI_Module_Wrapper*>(pModuleObj.get ()));
        pModule = pModuleWrapper->createModule (pPythonModule.get ());
        if (!pModule)
        {
            CLIENT_INIT_BOOKEND_PRINT ("MI_Module creation failed");
            PyErr_SetString (PyExc_ValueError, "MI_Module creation failed");
            rval = -1;
        }
        else
        {
            CLIENT_INIT_BOOKEND_PRINT ("MI_Module was created successfully");
        }
    }
    // parse the key
    unsigned int keyCode[4];
    if (0 == rval)
    {
        char keyText[9];
        keyText[8] = '\0';
        for (int i = 0; 0 == rval && i < 4; ++i)
        {
            strncpy (keyText, key + 8 * i, 8);
            char* pEnd = NULL;
            keyCode[i] = strtoul (keyText, &pEnd, 16);
            if (keyText + 8 != pEnd)
            {
                rval = -1;
                PyErr_SetString (PyExc_ValueError, "failed to parse key");
            }
        }
    }
    // finally create the client object
    if (0 == rval)
    {
        Client::Ptr pClient;
        if (EXIT_SUCCESS ==
            Client::create (static_cast<unsigned short>(port), keyCode, pModule,
                            &pClient))
        {
            CLIENT_INIT_BOOKEND_PRINT ("Client::create succeeded");
            new (pSelf) Client_Wrapper (pPythonModule.release (), pClient);
        }
        else
        {
            CLIENT_INIT_BOOKEND_PRINT ("Client::create failed");
            PyErr_SetString (PyExc_ValueError, "failed to create client");
            rval = -1;
        }
    }
    return rval;
}


/*static*/ PyObject*
Client_Wrapper::run (
    PyObject* pSelf)
{
    SCX_BOOKEND ("Client_Wrapper::run");
    Client_Wrapper* pClient = reinterpret_cast<Client_Wrapper*>(pSelf);
    pClient->m_pClient->run ();
    Py_RETURN_NONE;
}


/*ctor*/
Client_Wrapper::Client_Wrapper (
    PyObject* const pPythonModule,
    Client::Ptr const& pClient)
    : m_pPythonModule (pPythonModule)
    , m_pClient (pClient)
{
    SCX_BOOKEND ("Client_Wrapper::ctor");
}

    
/*dtor*/
Client_Wrapper::~Client_Wrapper ()
{
    SCX_BOOKEND ("Client_Wrapper::dtor");
}
