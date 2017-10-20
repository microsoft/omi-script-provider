import sys

import omi
from omi import *
import schema

import os

cwd = os.getcwd()
print(cwd)

RECORD_FILE_NAME = "FullTestOMI_Record"

InstancesRecord = []

def StringValue(instance, member_name):
    member = instance.GetValue(member_name)
    if member == None:
        return ""
    return str(member.value)


def StringInstance(instance):
    ret = ""
    members = ["Id", "BooleanTest", "RealTest", "IntTest", "StringTest"]
    for index, member in enumerate(members):
        if index != 0:
            ret += ', '
        ret += StringValue(instance, member)
    return ret


def ReplaceInstance(oldInstance, newInstance):
    booleanTest = newInstance.GetValue('BooleanTest')
    if booleanTest != None:
        oldInstance.SetValue('BooleanTest', MI_Boolean(booleanTest.value))

    realTest = newInstance.GetValue('RealTest')
    if realTest != None:
        oldInstance.SetValue('RealTest', MI_Real32(realTest.value))

    intTest = newInstance.GetValue('IntTest')
    if intTest != None:
        oldInstance.SetValue('IntTest', MI_Uint32(intTest.value))

    stringTest = newInstance.GetValue('StringTest')
    if stringTest != None:
        oldInstance.SetValue('StringTest', MI_String(stringTest.value))

    return oldInstance


def FindInstanceById(id):
    for entry in InstancesRecord:
        if entry.GetValue('Id').value == id:
            return entry
    return None


def DeleteInstanceById(id):
    for index, entry in enumerate(InstancesRecord):
        if entry.GetValue('Id').value == id:
            InstancesRecord.pop(index)
            return True

    return False


def GetNewId():
    maxId = -1
    for entry in InstancesRecord:
        valueId = entry.GetValue('Id').value
        if valueId > maxId:
            maxId = valueId
    return maxId + 1


def Load (module, context):
    context.PostResult (MI_RESULT_OK)


def Unload (module, context):
    context.PostResult (MI_RESULT_OK)


def Full_Test_Load (
    module, context):
    try:
        f = open(RECORD_FILE_NAME, "r")
        lines = f.read().splitlines()

        instance = context.NewInstance('Full_Test')
        for line in lines:
            members = line.split(', ')
            id = members[0]
            booleanTest = members[1]
            realTest = members[2]
            intTest = members[3]
            stringTest = members[4]

            instance.SetValue('Id', MI_Uint32(int(id)))

            if booleanTest != "":
                if booleanTest == "True":
                    booleanTest = True
                else:
                    booleanTest = False
            instance.SetValue('BooleanTest', MI_Boolean(booleanTest))

            if realTest != "":
                instance.SetValue('RealTest', MI_Real32(float(realTest)))

            if intTest != "":
                instance.SetValue('IntTest', MI_Uint32(int(intTest)))

            if stringTest != "":
                instance.SetValue('StringTest', MI_String(stringTest))
            InstancesRecord.append(instance)

            instance = context.NewInstance('Full_Test')
        f.close()
    except IOError as e:
        print(e)
        f.close()
    except:
        print(sys.exc_info()[0])
        f.close()
    context.PostResult (MI_RESULT_OK)


def Full_Test_Unload (
    context):
    try:
        f = open(RECORD_FILE_NAME, "w")
        for entry in InstancesRecord:
            f.write(StringInstance(entry) + "\n")
        f.close()
    except IOError as e:
        print(e)
        f.close()
    except:
        print(sys.exc_info()[0])
        f.close()
    context.PostResult (MI_RESULT_OK)


def Full_Test_EnumerateInstances (
    context, nameSpace, className, propertySet, keysOnly):

    instance = context.NewInstance('Full_Test')

    for entry in InstancesRecord:
        context.PostInstance(entry)

    context.PostResult (MI_RESULT_OK)


def Full_Test_GetInstance (
    context, nameSpace, className, instanceName, propertySet):
    id = instanceName.GetValue('Id').value

    foundInstance = FindInstanceById(id)

    if id == None:
        context.PostResult(MI_RESULT_FAILED)
        return

    if foundInstance == None:
        context.PostResult(MI_RESULT_NOT_FOUND)
        return

    context.PostInstance (foundInstance)

    context.PostResult (MI_RESULT_OK)


def Full_Test_CreateInstance (
    context, nameSpace, className, instance):

    #print(StringValue(instance, "DateTimeTest")

    #context.PostResult (MI_RESULT_OK)
    #return

    id = GetNewId()
    instance.SetValue('Id', MI_Uint32(id))
    InstancesRecord.append(instance)
    context.PostResult (MI_RESULT_OK)


def Full_Test_ModifyInstance (
    context, nameSpace, className, instance, propertySet):
    id = instance.GetValue('Id').value

    if id == None:
        context.PostResult(MI_RESULT_FAILED)
        return

    oldInstance = FindInstanceById(id)
    if oldInstance == None:
        context.PostResult(MI_RESULT_NOT_FOUND)
        return

    newInstance = ReplaceInstance(oldInstance, instance)

    InstancesRecord[id] = newInstance

    context.PostResult (MI_RESULT_OK)


def Full_Test_DeleteInstance (
    context, nameSpace, className, instanceName):
    id = instanceName.GetValue('Id').value

    if id == None:
        context.PostResult(MI_RESULT_FAILED)
        return

    if DeleteInstanceById(id) == False:
        context.PostResult(MI_RESULT_NOT_FOUND)
        return

    context.PostResult (MI_RESULT_OK)


def mi_main ():
    r = MI_Module (schema.schema, Load, Unload)
    return r
