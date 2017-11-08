// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include "mi_module_self.hpp"


#include "debug_tags.hpp"
#include "server.hpp"


#include <sstream>


#if (1)
#define PRINT_MI_MODULE_SELF (PRINT_BOOKENDS)
#else
#define PRINT_MI_MODULE_SELF (0)
#endif

#if (PRINT_MI_MODULE_SELF)
#define MODULE_BOOKEND_EX(X,Y) SCX_BOOKEND_EX (X,Y)
#else
#define MODULE_BOOKEND_EX(X,Y)
#endif

/*ctor*/
_MI_Module_Self::_MI_Module_Self (
    std::string const& module_name)
    : ModuleName (module_name)
{
#if (PRINT_MI_MODULE_SELF)
    std::ostringstream strm;
    strm << " ModuleName=\"" << ModuleName << "\"";
    MODULE_BOOKEND_EX ("_MI_Module_Self::ctor", strm.str ().c_str ());
#endif
}


/*dtor*/
_MI_Module_Self::~_MI_Module_Self ()
{
#if (PRINT_MI_MODULE_SELF)
    std::ostringstream strm;
    strm << " ModuleName=\"" << ModuleName << "\"";
    MODULE_BOOKEND_EX ("_MI_Module_Self::dtor", strm.str ().c_str ());
#endif
}
