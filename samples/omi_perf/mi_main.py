import omi
from omi import *

import schema


def Load (module, context):
    context.PostResult (MI_RESULT_OK)


def Unload (module, context):
    context.PostResult (MI_RESULT_OK)


def OMI_Perf_Load (
    module, context):
    context.PostResult (MI_RESULT_OK)


def OMI_Perf_Unload (
    context):
    context.PostResult (MI_RESULT_OK)


def OMI_Perf_EnumerateInstances (
    context, nameSpace, className, propertySet, keysOnly):
    text = MI_String ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    instance = context.NewInstance ('OMI_Perf')
    instance.SetValue ('Prop01', text)
    instance.SetValue ('Prop02', text)
    instance.SetValue ('Prop03', text)
    instance.SetValue ('Prop04', text)
    instance.SetValue ('Prop05', text)
    instance.SetValue ('Prop06', text)
    instance.SetValue ('Prop07', text)
    instance.SetValue ('Prop08', text)
    instance.SetValue ('Prop09', text)
    instance.SetValue ('Prop10', text)
    instance.SetValue ('Prop11', text)
    instance.SetValue ('Prop12', text)
    instance.SetValue ('Prop13', text)
    instance.SetValue ('Prop14', text)
    instance.SetValue ('Prop15', text)
    instance.SetValue ('Prop16', text)
    instance.SetValue ('Prop17', text)
    instance.SetValue ('Prop18', text)
    instance.SetValue ('Prop19', text)
    instance.SetValue ('Prop20', text)
    for i in range (1000000):
        instance.SetValue ('Key', MI_Uint32 (i))
        context.PostInstance (instance)

    context.PostResult (MI_RESULT_OK)


def OMI_Perf_GetInstance (
    context, nameSpace, className, instanceName, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_Perf_CreateInstance (
    context, nameSpace, className, instance):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_Perf_ModifyInstance (
    context, nameSpace, className, instance, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_Perf_DeleteInstance (
    context, nameSpace, className, instanceName):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def mi_main ():
    r = MI_Module (schema.schema, Load, Unload)
    return r
