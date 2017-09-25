import omi
from omi import *

import schema


def Load (module, context):
    context.PostResult (MI_RESULT_OK)


def Unload (module, context):
    context.PostResult (MI_RESULT_OK)


def XYZ_Number_Load (
    module, context):
    context.PostResult (MI_RESULT_OK)


def XYZ_Number_Unload (
    context):
    context.PostResult (MI_RESULT_OK)


def XYZ_Number_EnumerateInstances (
    context, nameSpace, className, propertySet, keysOnly):
    instance = context.NewInstance ('XYZ_Number')
    instance.SetValue ('Description',
                       MI_String ('This is a long long long long string'))
    for i in range (1000):
        instance.SetValue ('Number', MI_Uint32 (i))
        instance.SetValue ('NumberString', MI_String (str (i)))
        context.PostInstance (instance)
    context.PostResult (MI_RESULT_OK)


def XYZ_Number_GetInstance (
    context, nameSpace, className, instanceName, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_Number_CreateInstance (
    context, nameSpace, className, instance):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_Number_ModifyInstance (
    context, nameSpace, className, instance, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def XYZ_Number_DeleteInstance (
    context, nameSpace, className, instanceName):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def mi_main ():
    r = MI_Module (schema.schema, Load, Unload)
    return r
