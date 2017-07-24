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
## XYZ_ColorBase
##
##==============================================================================
XYZ_ColorBase_quals = [
    ]

XYZ_ColorBase_Id_quals = [
    ]

XYZ_ColorBase_Id_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY | MI_FLAG_KEY, # flags
    'Id', # name
    XYZ_ColorBase_Id_quals, # qualifiers
    MI_UINT32, # type
    None, # className
    'XYZ_ColorBase', # origin
    'XYZ_ColorBase', # propagator
    None # value
    )

XYZ_ColorBase_properties = [
    XYZ_ColorBase_Id_prop,
    ]

XYZ_ColorBase_methods = [
    ]

XYZ_ColorBase_functions = MI_FunctionTable (
    'XYZ_ColorBase_Load',
    'XYZ_ColorBase_Unload',
    'XYZ_ColorBase_GetInstance',
    'XYZ_ColorBase_EnumerateInstances',
    'XYZ_ColorBase_CreateInstance',
    'XYZ_ColorBase_ModifyInstance',
    'XYZ_ColorBase_DeleteInstance',
    None,
    None,
    None,
    None,
    None,
    None,
    None
    )

XYZ_ColorBase_class = MI_ClassDecl (
    MI_FLAG_CLASS, # flags
    'XYZ_ColorBase', # name
    XYZ_ColorBase_quals, # qualifiers
    XYZ_ColorBase_properties, # properties
    None, # superclass
    XYZ_ColorBase_methods, # method
    XYZ_ColorBase_functions, # FunctionTable
    None # owningclass
    )

##==============================================================================
##
## XYZ_Color
##
##==============================================================================
XYZ_Color_quals = [
    ]

XYZ_Color_Caption_quals = [
    ]

XYZ_Color_Caption_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'Caption', # name
    XYZ_Color_Caption_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'XYZ_Color', # origin
    'XYZ_Color', # propagator
    None # value
    )

XYZ_Color_Name_quals = [
    ]

XYZ_Color_Name_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'Name', # name
    XYZ_Color_Name_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'XYZ_Color', # origin
    'XYZ_Color', # propagator
    None # value
    )

XYZ_Color_properties = [
    XYZ_ColorBase_Id_prop,
    XYZ_Color_Caption_prop,
    XYZ_Color_Name_prop,
    ]

XYZ_Color_methods = [
    ]

XYZ_Color_functions = MI_FunctionTable (
    'XYZ_Color_Load',
    'XYZ_Color_Unload',
    'XYZ_Color_GetInstance',
    'XYZ_Color_EnumerateInstances',
    'XYZ_Color_CreateInstance',
    'XYZ_Color_ModifyInstance',
    'XYZ_Color_DeleteInstance',
    None,
    None,
    None,
    None,
    None,
    None,
    None
    )

XYZ_Color_class = MI_ClassDecl (
    MI_FLAG_CLASS, # flags
    'XYZ_Color', # name
    XYZ_Color_quals, # qualifiers
    XYZ_Color_properties, # properties
    'XYZ_ColorBase', # superclass
    XYZ_Color_methods, # method
    XYZ_Color_functions, # FunctionTable
    None # owningclass
    )

classDecls = [
    XYZ_ColorBase_class,
    XYZ_Color_class,
    ]

schema = MI_SchemaDecl (
    qualifierDecls,
    classDecls
    )
