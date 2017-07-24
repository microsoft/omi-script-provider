import omi
from omi import *

import schema


def Load (module, context):
    be = BookEnd ('XYZ_Load (XYZ_Color module)')
    context.PostResult (MI_RESULT_OK)


def Unload (module, context):
    be = BookEnd ('XYZ_Unload (XYZ_Color module)')
    context.PostResult (MI_RESULT_OK)


def XYZ_ColorBase_Load (
    module, context):
    be = BookEnd ('XYZ_ColorBase_Load')
    context.PostResult (MI_RESULT_OK)


def XYZ_ColorBase_Unload (
    context):
    be = BookEnd ('XYZ_ColorBase_Unload')
    context.PostResult (MI_RESULT_OK)


def XYZ_ColorBase_EnumerateInstances (
    context, nameSpace, className, propertySet, keysOnly):
    be = BookEnd ('XYZ_ColorBase_EnumerateInstances')
    instance = context.NewInstance ('XYZ_ColorBase')
    instance.SetValue ('Id', MI_Uint32 (1000))
    context.PostInstance (instance)
    context.PostResult (MI_RESULT_OK)


def XYZ_ColorBase_GetInstance (
    context, nameSpace, className, instanceName, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_ColorBase_CreateInstance (
    context, nameSpace, className, instance):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_ColorBase_ModifyInstance (
    context, nameSpace, className, instance, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_ColorBase_DeleteInstance (
    context, nameSpace, className, instanceName):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_Color_Load (
    module, context):
    be = BookEnd ('XYZ_Color_Load')
    context.PostResult (MI_RESULT_OK)


def XYZ_Color_Unload (
    context):
    be = BookEnd ('XYZ_ColorBase_Unload')
    context.PostResult (MI_RESULT_OK)


def XYZ_Color_EnumerateInstances (
    context, nameSpace, className, propertySet, keysOnly):
    be = BookEnd ('XYZ_Color_EnumerateInstances')

    instance = context.NewInstance ('XYZ_Color')
    
    instance.SetValue ('Id', MI_Uint32 (1001))
    instance.SetValue ('Caption', MI_String ('This is Red'))
    instance.SetValue ('Name', MI_String ('Red'))
    context.PostInstance (instance)

    instance.SetValue ('Id', MI_Uint32 (1002))
    instance.SetValue ('Caption', MI_String ('This is Green'))
    instance.SetValue ('Name', MI_String ('Green'))
    context.PostInstance (instance)

    instance.SetValue ('Id', MI_Uint32 (1003))
    instance.SetValue ('Caption', MI_String ('This is Blue'))
    instance.SetValue ('Name', MI_String ('Blue'))
    context.PostInstance (instance)

    instance.SetValue ('Id', MI_Uint32 (1004))
    instance.SetValue ('Caption', MI_String ('This is Yellow'))
    instance.SetValue ('Name', MI_String ('Yellow'))
    context.PostInstance (instance)

    context.PostResult (MI_RESULT_OK)


def XYZ_Color_GetInstance (
    context, nameSpace, className, instanceName, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_Color_CreateInstance (
    context, nameSpace, className, instance):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_Color_ModifyInstance (
    context, nameSpace, className, instance, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_Color_DeleteInstance (
    context, nameSpace, className, instanceName):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def mi_main ():
    be = BookEnd ('MI_Main (XYZ_Color module)')
    r = MI_Module (schema.schema, Load, Unload)
    return r
