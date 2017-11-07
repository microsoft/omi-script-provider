// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#ifndef INCLUDED_MI_MODULE_SELF_HPP
#define INCLUDED_MI_MODULE_SELF_HPP


#include "unique_ptr.hpp"


#include <MI.h>
#include <string>


class Server;


struct _MI_Module_Self
{
    /*ctor*/ _MI_Module_Self (std::string const& module_name);
    /*dtor*/ ~_MI_Module_Self ();

    std::string ModuleName;
    util::unique_ptr<Server> pServer;
    MI_Module Module;
};


#endif // INCLUDED_MI_MODULE_SELF_HPP
