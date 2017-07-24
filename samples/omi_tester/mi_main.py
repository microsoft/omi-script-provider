import omi
from omi import *

import schema


def Load (module, context):
    be = BookEnd ('Load (OMI_Tester module)')
    context.PostResult (MI_RESULT_OK)


def Unload (module, context):
    be = BookEnd ('Unload (OMI_Tester module)')
    context.PostResult (MI_RESULT_OK)


def OMI_Tester_Load (
    module, context):
    be = BookEnd ('OMI_Tester_Load')
    context.PostResult (MI_RESULT_OK)


def OMI_Tester_Unload (
    context):
    be = BookEnd ('OMI_Tester_Unload')
    context.PostResult (MI_RESULT_OK)


def OMI_Tester_EnumerateInstances (
    context, nameSpace, className, propertySet, keysOnly):
    be = BookEnd ('OMI_Tester_EnumerateInstances')
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_Tester_GetInstance (
    context, nameSpace, className, instanceName, propertySet):
    be = BookEnd ('OMI_Tester_GetInstance')
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_Tester_CreateInstance (
    context, nameSpace, className, instance):
    be = BookEnd ('OMI_Tester_CreateInstance')
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_Tester_ModifyInstance (
    context, nameSpace, className, instance, propertySet):
    be = BookEnd ('OMI_Tester_ModifyInstance')
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_Tester_DeleteInstance (
    context, nameSpace, className, instanceName):
    be = BookEnd ('OMI_Tester_DeleteInstance')
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_Tester_Func1 (
    context, nameSpace, className, methodName, instanceName, parameters):
    be = BookEnd ('OMI_Tester_Func1')
    BookEndPrint ('**********')
    BookEndPrint ('**********')
    BookEndPrint ('**********')
    BookEndPrint ('**********')
    BookEndPrint ('**********')

    outParams = context.NewParameters ('OMI_Tester', 'Func1')
    outParams.SetValue ('Out1', MI_String ('ONE'))
    outParams.SetValue ('Out2', MI_Uint32 (1))
    outParams.SetValue ('Out3', MI_Boolean (True))
    outParams.SetValue ('MIReturn', MI_Uint32 (0))
    context.PostInstance (outParams)
    context.PostResult (MI_RESULT_OK)

    BookEndPrint ('**********')
    BookEndPrint ('**********')
    BookEndPrint ('**********')
    BookEndPrint ('**********')
    BookEndPrint ('**********')
    
    #OMI_Tester_Func1_Class out;

    #out.Out1_value(MI_T("ONE"));
    #out.Out2_value(1);
    #out.Out3_value(MI_TRUE);
    #out.MIReturn_value(0);

    #context.Post(out);
    #context.Post(MI_RESULT_OK);

    #context.PostResult (MI_RESULT_NOT_SUPPORTED)


def mi_main ():
    r = MI_Module (schema.schema, Load, Unload)
    return r
