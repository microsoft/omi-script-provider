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
qualifierDecls = [
    ]

##==============================================================================
##
## XYZ_Number
##
##==============================================================================
XYZ_Number_quals = [
    ]

XYZ_Number_Description_quals = [
    ]

XYZ_Number_Description_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'Description', # name
    XYZ_Number_Description_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'XYZ_Number', # origin
    'XYZ_Number', # propagator
    None # value
    )

XYZ_Number_Number_quals = [
    ]

XYZ_Number_Number_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY | MI_FLAG_KEY, # flags
    'Number', # name
    XYZ_Number_Number_quals, # qualifiers
    MI_UINT32, # type
    None, # className
    'XYZ_Number', # origin
    'XYZ_Number', # propagator
    None # value
    )

XYZ_Number_NumberString_quals = [
    ]

XYZ_Number_NumberString_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'NumberString', # name
    XYZ_Number_NumberString_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'XYZ_Number', # origin
    'XYZ_Number', # propagator
    None # value
    )

XYZ_Number_properties = [
    XYZ_Number_Description_prop,
    XYZ_Number_Number_prop,
    XYZ_Number_NumberString_prop,
    ]

XYZ_Number_methods = [
    ]

XYZ_Number_functions = MI_FunctionTable (
    'XYZ_Number_Load',
    'XYZ_Number_Unload',
    'XYZ_Number_GetInstance',
    'XYZ_Number_EnumerateInstances',
    'XYZ_Number_CreateInstance',
    'XYZ_Number_ModifyInstance',
    'XYZ_Number_DeleteInstance',
    None,
    None,
    None,
    None,
    None,
    None,
    None
    )

XYZ_Number_class = MI_ClassDecl (
    MI_FLAG_CLASS, # flags
    'XYZ_Number', # name
    XYZ_Number_quals, # qualifiers
    XYZ_Number_properties, # properties
    None, # superclass
    XYZ_Number_methods, # method
    XYZ_Number_functions, # FunctionTable
    None # owningclass
    )

classDecls = [
    XYZ_Number_class,
    ]

schema = MI_SchemaDecl (
    qualifierDecls,
    classDecls
    )
