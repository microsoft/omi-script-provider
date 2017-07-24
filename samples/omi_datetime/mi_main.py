import omi
from omi import *

import schema

import random


def Load (module, context):
    context.PostResult (MI_RESULT_OK)


def Unload (module, context):
    context.PostResult (MI_RESULT_OK)


def OMI_Datetime_Load (
    module, context):
    context.PostResult (MI_RESULT_OK)


def OMI_Datetime_Unload (
    context):
    context.PostResult (MI_RESULT_OK)


def OMI_Datetime_EnumerateInstances (
    context, nameSpace, className, propertySet, keysOnly):
    be = BookEnd ('OMI_Datetime_EnumerateInstances')
    instance = context.NewInstance ('OMI_Datetime')
    instance.SetValue ('Key', MI_String ('Dates'))
    ts = MI_Timestamp ( \
        random.randint (1900, 2017), \
        random.randint (1, 12), \
        random.randint (1, 28), \
        random.randint (0, 23), \
        random.randint (0, 59), \
        random.randint (0, 59), \
        random.randint (0, 999999), \
        0)
    BookEndPrint ('{0}-{1}-{2},{3}:{4}:{5}.{6},{7}'.format ( \
        ts.year, ts.month, ts.day, ts.hour, ts.minute, ts.second, \
        ts.microseconds, ts.utc))
    instance.SetValue ('timestamp', ts)
    int = MI_Interval ( \
        random.randint (0, 1000), \
        random.randint (0, 59), \
        random.randint (0, 59), \
        random.randint (0, 59), \
        random.randint (0, 999999))
    BookEndPrint ('{0}-{1}:{2}:{3}.{4}'.format ( \
        int.days, int.hours, int.minutes, int.seconds, int.microseconds))
    instance.SetValue ('interval', int)
    tsArray = MI_DatetimeA ()
    for i in range (4):
        ts = MI_Timestamp ( \
            random.randint (1900, 2017), \
            random.randint (1, 12), \
            random.randint (1, 28), \
            random.randint (0, 23), \
            random.randint (0, 59), \
            random.randint (0, 59), \
            random.randint (0, 999999), \
            0)
        BookEndPrint ('{0}-{1}-{2},{3}:{4}:{5}.{6},{7}'.format ( \
            ts.year, ts.month, ts.day, ts.hour, ts.minute, ts.second, \
            ts.microseconds, ts.utc))
        tsArray.append (ts)
    instance.SetValue ('timestamps', tsArray)
    intArray = MI_DatetimeA ()
    for i in range (4):
        int = MI_Interval ( \
            random.randint (0, 1000), \
            random.randint (0, 59), \
            random.randint (0, 59), \
            random.randint (0, 59), \
            random.randint (0, 999999))
        BookEndPrint ('{0}-{1}:{2}:{3}.{4}'.format ( \
            int.days, int.hours, int.minutes, int.seconds, int.microseconds))
        intArray.append (int)
    instance.SetValue ('intervals', intArray)
    mixedArray = MI_DatetimeA ()
    for i in range (8):
        val = None
        if 0 == random.randint (0, 1):
            val = MI_Timestamp ( \
                random.randint (1900, 2017), \
                random.randint (1, 12), \
                random.randint (1, 28), \
                random.randint (0, 23), \
                random.randint (0, 59), \
                random.randint (0, 59), \
                random.randint (0, 999999), \
                0)
            BookEndPrint ('{0}-{1}-{2},{3}:{4}:{5}.{6},{7}'.format ( \
                ts.year, ts.month, ts.day, ts.hour, ts.minute, ts.second, \
                ts.microseconds, ts.utc))
        else:
            val = MI_Interval ( \
                random.randint (0, 1000), \
                random.randint (0, 59), \
                random.randint (0, 59), \
                random.randint (0, 59), \
                random.randint (0, 999999))
            BookEndPrint ('{0}-{1}:{2}:{3}.{4}'.format ( \
                int.days, int.hours, int.minutes, int.seconds, \
                int.microseconds))
        mixedArray.append (val)
    instance.SetValue ('mixed', mixedArray);
    context.PostInstance (instance)
    context.PostResult (MI_RESULT_OK)


def OMI_Datetime_GetInstance (
    context, nameSpace, className, instanceName, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_Datetime_CreateInstance (
    context, nameSpace, className, instance):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_Datetime_ModifyInstance (
    context, nameSpace, className, instance, propertySet):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def OMI_Datetime_DeleteInstance (
    context, nameSpace, className, instanceName):
    context.PostResult (MI_RESULT_NOT_SUPPORTED)


def mi_main ():
    r = MI_Module (schema.schema, Load, Unload)
    return r
