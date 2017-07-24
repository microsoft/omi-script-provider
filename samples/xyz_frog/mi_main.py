import omi
from omi import *

import schema


def Load (module, context):
    context.PostResult (MI_RESULT_OK)


def Unload (module, context):
    context.PostResult (MI_RESULT_OK)


def XYZ_Frog_Load (
    module, context):
    context.PostResult (MI_RESULT_OK)


def XYZ_Frog_Unload (
    context):
    context.PostResult (MI_RESULT_OK)


def XYZ_Frog_EnumerateInstances (
    context, nameSpace, className, propertySet, keysOnly):
    frog1 = context.NewInstance ('XYZ_Frog')
    frog1.SetValue ('Name', MI_String ('Fred'))
    frog1.SetValue ('Weight', MI_Uint32 (55))
    frog1.SetValue ('Color', MI_String ('Green'))
    context.PostInstance (frog1)
    frog2 = context.NewInstance ('XYZ_Frog')
    frog2.SetValue ('Name', MI_String ('Same'))
    frog2.SetValue ('Weight', MI_Uint32 (65))
    frog2.SetValue ('Color', MI_String ('Blue'))
    context.PostInstance (frog2)
    context.PostResult (MI_RESULT_OK)


def XYZ_Frog_GetInstance (
    context, nameSpace, className, instanceName, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_Frog_CreateInstance (
    context, nameSpace, className, instance):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_Frog_ModifyInstance (
    context, nameSpace, className, instance, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_Frog_DeleteInstance (
    context, nameSpace, className, instanceName):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def mi_main ():
    r = MI_Module (schema.schema, Load, Unload)
    return r
