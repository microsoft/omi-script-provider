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
## OMI_Datetime
##
##==============================================================================
OMI_Datetime_quals = [
    ]

OMI_Datetime_Key_quals = [
    ]

OMI_Datetime_Key_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY | MI_FLAG_KEY, # flags
    'Key', # name
    OMI_Datetime_Key_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'OMI_Datetime', # origin
    'OMI_Datetime', # propagator
    None # value
    )

OMI_Datetime_timestamp_quals = [
    ]

OMI_Datetime_timestamp_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'timestamp', # name
    OMI_Datetime_timestamp_quals, # qualifiers
    MI_DATETIME, # type
    None, # className
    'OMI_Datetime', # origin
    'OMI_Datetime', # propagator
    None # value
    )

OMI_Datetime_interval_quals = [
    ]

OMI_Datetime_interval_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'interval', # name
    OMI_Datetime_interval_quals, # qualifiers
    MI_DATETIME, # type
    None, # className
    'OMI_Datetime', # origin
    'OMI_Datetime', # propagator
    None # value
    )

OMI_Datetime_timestamps_quals = [
    ]

OMI_Datetime_timestamps_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'timestamps', # name
    OMI_Datetime_timestamps_quals, # qualifiers
    MI_DATETIMEA, # type
    None, # className
    'OMI_Datetime', # origin
    'OMI_Datetime', # propagator
    None # value
    )

OMI_Datetime_intervals_quals = [
    ]

OMI_Datetime_intervals_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'intervals', # name
    OMI_Datetime_intervals_quals, # qualifiers
    MI_DATETIMEA, # type
    None, # className
    'OMI_Datetime', # origin
    'OMI_Datetime', # propagator
    None # value
    )

OMI_Datetime_mixed_quals = [
    ]

OMI_Datetime_mixed_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY, # flags
    'mixed', # name
    OMI_Datetime_mixed_quals, # qualifiers
    MI_DATETIMEA, # type
    None, # className
    'OMI_Datetime', # origin
    'OMI_Datetime', # propagator
    None # value
    )

OMI_Datetime_properties = [
    OMI_Datetime_Key_prop,
    OMI_Datetime_timestamp_prop,
    OMI_Datetime_interval_prop,
    OMI_Datetime_timestamps_prop,
    OMI_Datetime_intervals_prop,
    OMI_Datetime_mixed_prop,
    ]

OMI_Datetime_methods = [
    ]

OMI_Datetime_functions = MI_FunctionTable (
    'OMI_Datetime_Load',
    'OMI_Datetime_Unload',
    'OMI_Datetime_GetInstance',
    'OMI_Datetime_EnumerateInstances',
    'OMI_Datetime_CreateInstance',
    'OMI_Datetime_ModifyInstance',
    'OMI_Datetime_DeleteInstance',
    None,
    None,
    None,
    None,
    None,
    None,
    None
    )

OMI_Datetime_class = MI_ClassDecl (
    MI_FLAG_CLASS, # flags
    'OMI_Datetime', # name
    OMI_Datetime_quals, # qualifiers
    OMI_Datetime_properties, # properties
    None, # superclass
    OMI_Datetime_methods, # method
    OMI_Datetime_functions, # FunctionTable
    None # owningclass
    )

classDecls = [
    OMI_Datetime_class,
    ]

schema = MI_SchemaDecl (
    qualifierDecls,
    classDecls
    )
