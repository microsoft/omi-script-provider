// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include "mi_module_self.hpp"


#include "debug_tags.hpp"
#include "server.hpp"


#include <sstream>


/*ctor*/
_MI_Module_Self::_MI_Module_Self (
    std::string const& module_name)
    : ModuleName (module_name)
{
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << " ModuleName=\"" << ModuleName << "\"";
    SCX_BOOKEND_EX ("_MI_Module_Self::ctor", strm.str ().c_str ());
#endif
}


/*dtor*/
_MI_Module_Self::~_MI_Module_Self ()
{
#if (PRINT_BOOKENDS)
    std::ostringstream strm;
    strm << " ModuleName=\" << ModuleName << \"";
    SCX_BOOKEND_EX ("_MI_Module_Self::dtor", strm.str ().c_str ());
#endif
}
