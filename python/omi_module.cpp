// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include "Python.h"
#include <MI.h>


#include "debug_tags.hpp"
#include "mi_instance_wrapper.hpp"
#include "shared.hpp"


#include <iostream>
#include <new>
#include <sstream>
#include <string>


namespace {


PyMethodDefContainer_t g_methods;


}


using namespace scx;


extern "C" {


#if PY_MAJOR_VERSION >= 3
    // Python 3 requires the init function to be named PyInit_<module_name>
    #define initomi PyInit_omi
#endif


PyMODINIT_FUNC
initomi ()
{
    SCX_BOOKEND ("initomi");
    // global methods
    get_BookEnd_global_methods (g_methods);
    PyMethodDef const sentinel = { NULL, NULL, 0, NULL };
    g_methods.push_back (sentinel);
    PyObject* pModule;
    const char* m_name = "omi";
    const char* m_doc = "Module that creates the Foo extension type.";

    #if PY_MAJOR_VERSION >= 3
        static struct PyModuleDef moduledef = {
            PyModuleDef_HEAD_INIT,
            m_name,              /* m_name */
            m_doc,               /* m_doc */
            -1,                  /* m_size */
            &(g_methods[0]),     /* m_methods */
            NULL,                /* m_reload */
            NULL,                /* m_traverse */
            NULL,                /* m_clear */
            NULL,                /* m_free */
        };
        pModule = PyModule_Create (&moduledef);
    #else
        pModule = Py_InitModule3 (m_name, &(g_methods[0]), m_doc);
    #endif

    // classes
    init_BookEnd_wrapper (pModule);
    init_MI_wrapper (pModule);

    #if PY_MAJOR_VERSION >= 3
        // Python 3 should return the module
        return pModule;
    #endif
}


}
