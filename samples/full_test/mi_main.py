import omi
from omi import *

import schema


def Load (module, context):
    context.PostResult (MI_RESULT_OK)


def Unload (module, context):
    context.PostResult (MI_RESULT_OK)


def Full_Test_Load (
    module, context):
    context.PostResult (MI_RESULT_OK)


def Full_Test_Unload (
    context):
    context.PostResult (MI_RESULT_OK)


def Full_Test_EnumerateInstances (
    context, nameSpace, className, propertySet, keysOnly):
    context.PostResult (MI_RESULT_OK)


def Full_Test_GetInstance (
    context, nameSpace, className, instanceName, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def Full_Test_CreateInstance (
    context, nameSpace, className, instance):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def Full_Test_ModifyInstance (
    context, nameSpace, className, instance, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def Full_Test_DeleteInstance (
    context, nameSpace, className, instanceName):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def mi_main ():
    r = MI_Module (schema.schema, Load, Unload)
    return r
