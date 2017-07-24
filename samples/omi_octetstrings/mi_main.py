import omi
from omi import *

import schema


def Load (module, context):
    context.PostResult (MI_RESULT_OK)


def Unload (module, context):
    context.PostResult (MI_RESULT_OK)


def OMI_OctetStrings_Load (
    module, context):
    context.PostResult (MI_RESULT_OK)


def OMI_OctetStrings_Unload (
    context):
    context.PostResult (MI_RESULT_OK)


def OMI_OctetStrings_EnumerateInstances (
    context, nameSpace, className, propertySet, keysOnly):
    instance = context.NewInstance ('OMI_OctetStrings')
    instance.SetValue ('Key', MI_String ('OMI_OctetStrings.1'))
    instance.SetValue ('Data1', MI_Uint8A (
        [0, 0, 0, 9, ord ('h'), ord ('e'), ord ('l'), ord ('l'), ord ('o')]))
    instance.SetValue ('Str', MI_String (' &\'"><'))
    context.PostInstance (instance)
    context.PostResult (MI_RESULT_OK)


def OMI_OctetStrings_GetInstance (
    context, nameSpace, className, instanceName, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_OctetStrings_CreateInstance (
    context, nameSpace, className, instance):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_OctetStrings_ModifyInstance (
    context, nameSpace, className, instance, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_OctetStrings_DeleteInstance (
    context, nameSpace, className, instanceName):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def mi_main ():
    r = MI_Module (schema.schema, Load, Unload)
    return r
