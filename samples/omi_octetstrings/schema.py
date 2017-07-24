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
## OMI_OctetStrings
##
##==============================================================================
OMI_OctetStrings_quals = [
    ]

OMI_OctetStrings_Key_quals = [
    ]

OMI_OctetStrings_Key_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY | MI_FLAG_KEY, # flags
    'Key', # name
    OMI_OctetStrings_Key_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'OMI_OctetStrings', # origin
    'OMI_OctetStrings', # propagator
    None # value
    )

OMI_OctetStrings_Data1_quals = [
    ]

OMI_OctetStrings_Data1_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'Data1', # name
    OMI_OctetStrings_Data1_quals, # qualifiers
    MI_UINT8A, # type
    None, # className
    'OMI_OctetStrings', # origin
    'OMI_OctetStrings', # propagator
    None # value
    )

OMI_OctetStrings_Data2_quals = [
    ]

OMI_OctetStrings_Data2_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'Data2', # name
    OMI_OctetStrings_Data2_quals, # qualifiers
    MI_STRINGA, # type
    None, # className
    'OMI_OctetStrings', # origin
    'OMI_OctetStrings', # propagator
    None # value
    )

OMI_OctetStrings_Str_quals = [
    ]

OMI_OctetStrings_Str_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'Str', # name
    OMI_OctetStrings_Str_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'OMI_OctetStrings', # origin
    'OMI_OctetStrings', # propagator
    None # value
    )

OMI_OctetStrings_properties = [
    OMI_OctetStrings_Key_prop,
    OMI_OctetStrings_Data1_prop,
    OMI_OctetStrings_Data2_prop,
    OMI_OctetStrings_Str_prop,
    ]

OMI_OctetStrings_methods = [
    ]

OMI_OctetStrings_functions = MI_FunctionTable (
    'OMI_OctetStrings_Load',
    'OMI_OctetStrings_Unload',
    'OMI_OctetStrings_GetInstance',
    'OMI_OctetStrings_EnumerateInstances',
    'OMI_OctetStrings_CreateInstance',
    'OMI_OctetStrings_ModifyInstance',
    'OMI_OctetStrings_DeleteInstance',
    None,
    None,
    None,
    None,
    None,
    None,
    None
    )

OMI_OctetStrings_class = MI_ClassDecl (
    MI_FLAG_CLASS, # flags
    'OMI_OctetStrings', # name
    OMI_OctetStrings_quals, # qualifiers
    OMI_OctetStrings_properties, # properties
    None, # superclass
    OMI_OctetStrings_methods, # method
    OMI_OctetStrings_functions, # FunctionTable
    None # owningclass
    )

classDecls = [
    OMI_OctetStrings_class,
    ]

schema = MI_SchemaDecl (
    qualifierDecls,
    classDecls
    )
