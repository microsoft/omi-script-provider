# @migen@
##==============================================================================
##
## WARNING: THIS FILE WAS AUTOMATICALLY GENERATED. PLEASE DO NOT EDIT.
##
##==============================================================================
import omi
from omi import *

##==============================================================================
##
## Qualifier declarations
##
##==============================================================================
Weak_qual_decl_value = MI_Boolean (
    False)

Weak_qual_decl = MI_QualifierDecl (
    'Weak', # name
    MI_BOOLEAN, # type
    MI_FLAG_REFERENCE, # scope
    MI_FLAG_DISABLEOVERRIDE | MI_FLAG_TOSUBCLASS, # flavor
    Weak_qual_decl_value # value
    )

Write_qual_decl_value = MI_Boolean (
    False)

Write_qual_decl = MI_QualifierDecl (
    'Write', # name
    MI_BOOLEAN, # type
    MI_FLAG_PROPERTY, # scope
    0, # flavor
    Write_qual_decl_value # value
    )

qualifierDecls = [
    Weak_qual_decl,
    Write_qual_decl,
    ]

##==============================================================================
##
## Full_Test
##
##==============================================================================
Full_Test_quals = [
    ]

Full_Test_Id_quals = [
    ]

Full_Test_Id_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY | MI_FLAG_KEY, # flags
    'Id', # name
    Full_Test_Id_quals, # qualifiers
    MI_UINT32, # type
    None, # className
    'Full_Test', # origin
    'Full_Test', # propagator
    None # value
    )

Full_Test_BooleanTest_quals = [
    ]

Full_Test_BooleanTest_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'BooleanTest', # name
    Full_Test_BooleanTest_quals, # qualifiers
    MI_BOOLEAN, # type
    None, # className
    'Full_Test', # origin
    'Full_Test', # propagator
    None # value
    )

Full_Test_DateTimeTest_quals = [
    ]

Full_Test_DateTimeTest_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'DateTimeTest', # name
    Full_Test_DateTimeTest_quals, # qualifiers
    MI_DATETIME, # type
    None, # className
    'Full_Test', # origin
    'Full_Test', # propagator
    None # value
    )

Full_Test_RealTest_quals = [
    ]

Full_Test_RealTest_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'RealTest', # name
    Full_Test_RealTest_quals, # qualifiers
    MI_REAL32, # type
    None, # className
    'Full_Test', # origin
    'Full_Test', # propagator
    None # value
    )

Full_Test_IntTest_quals = [
    ]

Full_Test_IntTest_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'IntTest', # name
    Full_Test_IntTest_quals, # qualifiers
    MI_UINT32, # type
    None, # className
    'Full_Test', # origin
    'Full_Test', # propagator
    None # value
    )

Full_Test_StringTest_quals = [
    ]

Full_Test_StringTest_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'StringTest', # name
    Full_Test_StringTest_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'Full_Test', # origin
    'Full_Test', # propagator
    None # value
    )

Full_Test_properties = [
    Full_Test_Id_prop,
    Full_Test_BooleanTest_prop,
    Full_Test_DateTimeTest_prop,
    Full_Test_RealTest_prop,
    Full_Test_IntTest_prop,
    Full_Test_StringTest_prop,
    ]

Full_Test_methods = [
    ]

Full_Test_functions = MI_FunctionTable (
    'Full_Test_Load',
    'Full_Test_Unload',
    'Full_Test_GetInstance',
    'Full_Test_EnumerateInstances',
    'Full_Test_CreateInstance',
    'Full_Test_ModifyInstance',
    'Full_Test_DeleteInstance',
    None,
    None,
    None,
    None,
    None,
    None,
    None
    )

Full_Test_class = MI_ClassDecl (
    MI_FLAG_CLASS, # flags
    'Full_Test', # name
    Full_Test_quals, # qualifiers
    Full_Test_properties, # properties
    None, # superclass
    Full_Test_methods, # method
    Full_Test_functions, # FunctionTable
    None # owningclass
    )

classDecls = [
    Full_Test_class,
    ]

schema = MI_SchemaDecl (
    qualifierDecls,
    classDecls
    )
