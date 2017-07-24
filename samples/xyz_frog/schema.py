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
## XYZ_Frog
##
##==============================================================================
XYZ_Frog_quals = [
    ]

XYZ_Frog_Name_quals = [
    ]

XYZ_Frog_Name_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY | MI_FLAG_KEY, # flags
    'Name', # name
    XYZ_Frog_Name_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'XYZ_Frog', # origin
    'XYZ_Frog', # propagator
    None # value
    )

XYZ_Frog_Weight_quals = [
    ]

XYZ_Frog_Weight_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'Weight', # name
    XYZ_Frog_Weight_quals, # qualifiers
    MI_UINT32, # type
    None, # className
    'XYZ_Frog', # origin
    'XYZ_Frog', # propagator
    None # value
    )

XYZ_Frog_Color_quals = [
    ]

XYZ_Frog_Color_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'Color', # name
    XYZ_Frog_Color_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'XYZ_Frog', # origin
    'XYZ_Frog', # propagator
    None # value
    )

XYZ_Frog_properties = [
    XYZ_Frog_Name_prop,
    XYZ_Frog_Weight_prop,
    XYZ_Frog_Color_prop,
    ]
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
## XYZ_Frog
##
##==============================================================================
XYZ_Frog_quals = [
    ]

XYZ_Frog_Name_quals = [
    ]

XYZ_Frog_Name_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY | MI_FLAG_KEY, # flags
    'Name', # name
    XYZ_Frog_Name_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'XYZ_Frog', # origin
    'XYZ_Frog', # propagator
    None # value
    )

XYZ_Frog_Weight_quals = [
    ]

XYZ_Frog_Weight_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'Weight', # name
    XYZ_Frog_Weight_quals, # qualifiers
    MI_UINT32, # type
    None, # className
    'XYZ_Frog', # origin
    'XYZ_Frog', # propagator
    None # value
    )

XYZ_Frog_methods = [
    ]

XYZ_Frog_functions = MI_FunctionTable (
    'XYZ_Frog_Load',
    'XYZ_Frog_Unload',
    'XYZ_Frog_GetInstance',
    'XYZ_Frog_EnumerateInstances',
    'XYZ_Frog_CreateInstance',
    'XYZ_Frog_ModifyInstance',
    'XYZ_Frog_DeleteInstance',
    None,
    None,
    None,
    None,
    None,
    None,
    None
    )

XYZ_Frog_class = MI_ClassDecl (
    MI_FLAG_CLASS, # flags
    'XYZ_Frog', # name
    XYZ_Frog_quals, # qualifiers
    XYZ_Frog_properties, # properties
    None, # superclass
    XYZ_Frog_methods, # method
    XYZ_Frog_functions, # FunctionTable
    None # owningclass
    )

classDecls = [
    XYZ_Frog_class,
    ]

schema = MI_SchemaDecl (
    qualifierDecls,
    classDecls
    )
