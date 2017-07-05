from distutils.core import setup, Extension
from distutils import ccompiler

import os
cwd = os.getcwd ()
root_dir = cwd[:-len('/scriptprovider/python')]

module1 = Extension (
    'omi',
    sources = ['bookend_wrapper.cpp',
               'client_wrapper.cpp',
               'functor.cpp',
               'mi_context_wrapper.cpp',
               'mi_function_table_placeholder.cpp',
               'mi_instance_wrapper.cpp',
               'mi_module_wrapper.cpp',
               'mi_schema_wrapper.cpp',
               'mi_wrapper.cpp',
               'omi_module.cpp',
               'py_converter.cpp',
               'shared.cpp'],
    include_dirs = [root_dir,
                    root_dir + '/scriptprovider/provider',
                    root_dir + '/omi/Unix/output/include',
                    root_dir + '/omi/Unix/common'],
    library_dirs = [root_dir + '/scriptprovider/bin'],
    libraries = ['OMIScriptProvider'],
    define_macros = [('PRINT_BOOKENDS','1')],
    )

print module1.__dict__


foo = ccompiler.get_default_compiler

print foo.__dict__


setup (name = 'omi',
       version = '1.0',
       description = 'The Python OMI interface',
       ext_modules = [module1])
