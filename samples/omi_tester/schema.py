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
## OMI_Tester
##
##==============================================================================
OMI_Tester_quals = [
    ]

OMI_Tester_Key_quals = [
    ]

OMI_Tester_Key_prop = MI_PropertyDecl (
    MI_FLAG_PROPERTY | MI_FLAG_KEY, # flags
    'Key', # name
    OMI_Tester_Key_quals, # qualifiers
    MI_STRING, # type
    None, # className
    'OMI_Tester', # origin
    'OMI_Tester', # propagator
    None # value
    )

OMI_Tester_properties = [
    OMI_Tester_Key_prop,
    ]

OMI_Tester_Func1_quals = [
    ]

OMI_Tester_Func1_In1_quals = [
    ]

OMI_Tester_Func1_In1_param = MI_ParameterDecl (
    MI_FLAG_PARAMETER | MI_FLAG_IN, # flags
    'In1', # name
    OMI_Tester_Func1_In1_quals, # qualifiers
    MI_STRING, # type
    None # className
    )

OMI_Tester_Func1_In2_quals = [
    ]

OMI_Tester_Func1_In2_param = MI_ParameterDecl (
    MI_FLAG_PARAMETER | MI_FLAG_IN, # flags
    'In2', # name
    OMI_Tester_Func1_In2_quals, # qualifiers
    MI_UINT32, # type
    None # className
    )

OMI_Tester_Func1_In3_quals = [
    ]

OMI_Tester_Func1_In3_param = MI_ParameterDecl (
    MI_FLAG_PARAMETER | MI_FLAG_IN, # flags
    'In3', # name
    OMI_Tester_Func1_In3_quals, # qualifiers
    MI_BOOLEAN, # type
    None # className
    )

OMI_Tester_Func1_Out1_quals = [
    ]

OMI_Tester_Func1_Out1_param = MI_ParameterDecl (
    MI_FLAG_PARAMETER | MI_FLAG_OUT, # flags
    'Out1', # name
    OMI_Tester_Func1_Out1_quals, # qualifiers
    MI_STRING, # type
    None # className
    )

OMI_Tester_Func1_Out2_quals = [
    ]

OMI_Tester_Func1_Out2_param = MI_ParameterDecl (
    MI_FLAG_PARAMETER | MI_FLAG_OUT, # flags
    'Out2', # name
    OMI_Tester_Func1_Out2_quals, # qualifiers
    MI_UINT32, # type
    None # className
    )

OMI_Tester_Func1_Out3_quals = [
    ]

OMI_Tester_Func1_Out3_param = MI_ParameterDecl (
    MI_FLAG_PARAMETER | MI_FLAG_OUT, # flags
    'Out3', # name
    OMI_Tester_Func1_Out3_quals, # qualifiers
    MI_BOOLEAN, # type
    None # className
    )

OMI_Tester_Func1_MIReturn_quals = [
    ]

OMI_Tester_Func1_MIReturn_param = MI_ParameterDecl (
    MI_FLAG_PARAMETER | MI_FLAG_OUT, # flags
    'MIReturn', # name
    OMI_Tester_Func1_MIReturn_quals, # qualifiers
    MI_UINT32, # type
    None # className
    )

OMI_Tester_Func1_params = [
    OMI_Tester_Func1_In1_param,
    OMI_Tester_Func1_In2_param,
    OMI_Tester_Func1_In3_param,
    OMI_Tester_Func1_Out1_param,
    OMI_Tester_Func1_Out2_param,
    OMI_Tester_Func1_Out3_param,
    OMI_Tester_Func1_MIReturn_param,
    ]

OMI_Tester_Func1_method = MI_MethodDecl (
    MI_FLAG_METHOD | MI_FLAG_STATIC, # flags
    'Func1', # name
    OMI_Tester_Func1_quals, # qualifiers
    OMI_Tester_Func1_params, # parameters
    MI_UINT32, # returnType
    'OMI_Tester', # origin
    'OMI_Tester', # propagator
    'OMI_Tester_Func1' # method
    )

OMI_Tester_methods = [
    OMI_Tester_Func1_method,
    ]

OMI_Tester_functions = MI_FunctionTable (
    'OMI_Tester_Load',
    'OMI_Tester_Unload',
    'OMI_Tester_GetInstance',
    'OMI_Tester_EnumerateInstances',
    'OMI_Tester_CreateInstance',
    'OMI_Tester_ModifyInstance',
    'OMI_Tester_DeleteInstance',
    None,
    None,
    None,
    None,
    None,
    None,
    None
    )

OMI_Tester_class = MI_ClassDecl (
    MI_FLAG_CLASS, # flags
    'OMI_Tester', # name
    OMI_Tester_quals, # qualifiers
    OMI_Tester_properties, # properties
    None, # superclass
    OMI_Tester_methods, # method
    OMI_Tester_functions, # FunctionTable
    None # owningclass
    )

classDecls = [
    OMI_Tester_class,
    ]

schema = MI_SchemaDecl (
    qualifierDecls,
    classDecls
    )
