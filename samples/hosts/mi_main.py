import omi
from omi import *

import schema


def Load (module, context):
    context.PostResult (MI_RESULT_OK)


def Unload (module, context):
    context.PostResult (MI_RESULT_OK)


def Hosts_Load (
    module, context):
    context.PostResult (MI_RESULT_OK)


def Hosts_Unload (
    context):
    context.PostResult (MI_RESULT_OK)


def Hosts_EnumerateInstances (
    context, nameSpace, className, propertySet, keysOnly):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def Hosts_GetInstance (
    context, nameSpace, className, instanceName, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def Hosts_CreateInstance (
    context, nameSpace, className, instance):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def Hosts_ModifyInstance (
    context, nameSpace, className, instance, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def Hosts_DeleteInstance (
    context, nameSpace, className, instanceName):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def Hosts_Ping (
    context, nameSpace, className, methodName, instanceName, parameters):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def mi_main ():
    r = MI_Module (schema.schema, Load, Unload)
    return r
