// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#ifndef INCLUDED_CLIENT_HPP
#define INCLUDED_CLIENT_HPP


#include "internal_counted_ptr.hpp"


#include <cstdlib>


#define EXPORT_PUBLIC __attribute__ ((visibility ("default")))


class socket_wrapper;


namespace scx
{


class MI_Context;
class MI_Module;


class Client : public util::ref_counted_obj
{
public:
    typedef util::internal_counted_ptr<Client> Ptr;
    
    enum {
        SUCCESS = EXIT_SUCCESS,
    };

    EXPORT_PUBLIC static int create (
        unsigned short const& port,
        unsigned int (&key)[4],
        util::internal_counted_ptr<MI_Module> const& pModule,
        Ptr* ppClientOut);
    EXPORT_PUBLIC virtual /*dtor*/ ~Client ();

    EXPORT_PUBLIC int run ();

private:
    /*ctor*/ Client (
        util::internal_counted_ptr<socket_wrapper> const& pSocket,
        util::internal_counted_ptr<MI_Module> const& pModule);

    int handle_module_load ();
    int handle_module_unload ();
    int handle_class_load ();
    int handle_class_unload ();
    int handle_enumerate_instances ();
    bool handle_get_instance ();
    bool handle_create_instance ();
    bool handle_modify_instance ();
    bool handle_delete_instance ();

    bool handle_invoke ();

    /*ctor*/ Client (Client const&); // = delete
    Client& operator = (Client const&); // = delete
    
    util::internal_counted_ptr<socket_wrapper> const m_pSocket;
    util::internal_counted_ptr<MI_Module> const m_pModule;
    util::internal_counted_ptr<MI_Context> const m_pContext;
};


} // namespace scx


#undef EXPORT_PUBLIC


#endif // INCLUDED_CLIENT_HPP
