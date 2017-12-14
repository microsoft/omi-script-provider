from omi import *

# Import test functions
from array_types_tests.array_boolean import booleana_test
from array_types_tests.array_char import char16a_test
from array_types_tests.array_datetime import datetimea_test
from array_types_tests.array_int16 import uint16a_test, sint16a_test
from array_types_tests.array_int32 import uint32a_test, sint32a_test
from array_types_tests.array_int64 import uint64a_test, sint64a_test
from array_types_tests.array_int8 import uint8a_test, sint8a_test
from array_types_tests.array_real32 import real32a_test
from array_types_tests.array_real64 import real64a_test
from array_types_tests.array_strings import stringa_test
from types_tests.bool_type import bool_test
from types_tests.char_type import char16_test
from types_tests.instance_type import instance_test
from types_tests.int16_type import uint16_test, sint16_test
from types_tests.int32_type import uint32_test, sint32_test
from types_tests.int64_type import uint64_test, sint64_test
from types_tests.int8_type import uint8_test, sint8_test
from types_tests.real32_type import real32_test
from types_tests.real64_type import real64_test
from types_tests.strings_type import string_test
from types_tests.timestamp_interval_types import timestamp_test, interval_test
from utils import *


def fn1():
    be = BookEnd('fn1')

    #qualDecl0 = MI_QualifierDecl ('alpha', MI_STRING, 2, 3, 'monkey')
    #qual0 = MI_Qualifier ('bravo', MI_STRING, 2, 'taco')

    #qualifiers = [MI_Qualifier ('charlie', MI_STRING, 3, 'cheese')]

    #propDecl0 = MI_PropertyDecl (3, 4, 'delta', qualifiers, MI_STRING, 'echo')

    #parameters = [MI_ParameterDecl (5, 6, 'fox', qualifiers, MI_STRING, 'golf')]

    # meth0 = MI_MethodDecl (7, 8, 'hotel', qualifiers, parameters, MI_UINT32,
    #                       'origin', 'propagator')

    #val = MI_Uint32 (1)
    #BookEndPrint ('val: {0}'.format (val))

    # uint8a
    uint8_0 = random.randint(0, 0xFF)
    uint8_1 = random.randint(0, 0xFF)
    while uint8_1 == uint8_0:
        uint8_1 = random.randint(0, 0xFF)
    uint8_2 = random.randint(0, 0xFF)
    while uint8_2 == uint8_0 or \
            uint8_2 == uint8_1:
        uint8_2 = random.randint(0, 0xFF)
    uint8_3 = random.randint(0, 0xFF)
    while uint8_0 == uint8_3 or \
            uint8_1 == uint8_3 or \
            uint8_2 == uint8_3:
        uint8_3 = random.randint(0, 0xFF)
    uint8_4 = random.randint(0, 0xFF)
    while uint8_0 == uint8_4 or \
            uint8_1 == uint8_4 or \
            uint8_2 == uint8_4 or \
            uint8_3 == uint8_4:
        uint8_4 = random.randint(0, 0xFF)
    uint8_5 = random.randint(0, 0xFF)
    while uint8_0 == uint8_5 or \
            uint8_1 == uint8_5 or \
            uint8_2 == uint8_5 or \
            uint8_3 == uint8_5 or \
            uint8_4 == uint8_5:
        uint8_5 = random.randint(0, 0xFF)
    uint8_6 = random.randint(0, 0xFF)
    while uint8_0 == uint8_6 or \
            uint8_1 == uint8_6 or \
            uint8_2 == uint8_6 or \
            uint8_3 == uint8_6 or \
            uint8_4 == uint8_6 or \
            uint8_5 == uint8_6:
        uint8_6 = random.randint(0, 0xFF)
    uint8_7 = random.randint(0, 0xFF)
    while uint8_0 == uint8_7 or \
            uint8_1 == uint8_7 or \
            uint8_2 == uint8_7 or \
            uint8_3 == uint8_7 or \
            uint8_4 == uint8_7 or \
            uint8_5 == uint8_7 or \
            uint8_6 == uint8_7:
        uint8_7 = random.randint(0, 0xFF)
    uint8_8 = random.randint(0, 0xFF)
    while uint8_0 == uint8_8 or \
            uint8_1 == uint8_8 or \
            uint8_2 == uint8_8 or \
            uint8_3 == uint8_8 or \
            uint8_4 == uint8_8 or \
            uint8_5 == uint8_8 or \
            uint8_6 == uint8_8 or \
            uint8_7 == uint8_8:
        uint8_8 = random.randint(0, 0xFF)

    uint8a_0 = MI_Uint8A((uint8_0, uint8_1, uint8_2))
    uint8a_1 = MI_Uint8A((uint8_3, uint8_4, uint8_5))
    uint8a_2 = MI_Uint8A((uint8_6, uint8_7, uint8_8))

    uint8a_in = uint8a_0
    inst27 = MI_Instance()

    inst27.SetValue('uint8a', uint8a_in)
    uint8a_out = inst27.GetValue('uint8a')

    if uint8a_out is not None:
        if not array_eq(uint8a_in, uint8a_0) or \
                not array_eq(inst27.GetValue('uint8a'), uint8a_0) or \
                not array_eq(uint8a_out, uint8a_0):
            BookEndPrint('----- uint8a SetValue/GetValue failed')
            rval = False
        else:
            uint8a_in = uint8a_1
            if not array_eq(uint8a_in, uint8a_1) or \
                    not array_eq(inst27.GetValue('uint8a'), uint8a_0) or \
                    not array_eq(uint8a_out, uint8a_0):
                BookEndPrint(
                    '----- uint8a SetValue/GetValue stored a reference')
                rval = False
            else:
                uint8a_out = uint8a_2
                if not array_eq(uint8a_in, uint8a_1) or \
                        not array_eq(inst27.GetValue('uint8a'), uint8a_0) or \
                        not array_eq(uint8a_out, uint8a_2):
                    BookEndPrint(
                        '----- uint8a SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- uint8a SetValue/GetValue returned None')
        rval = False

    inst28 = MI_Instance()
    inst28.SetValue('uint8a', inst27.GetValue('uint8a'))
    if array_eq(inst28.GetValue('uint8a'), inst27.GetValue('uint8a')):
        inst28.SetValue('uint8a', uint8a_1)
        if not array_eq(inst28.GetValue('uint8a'), uint8a_1):
            BookEndPrint("----- uint8a  SetValue failed")
            rval = False
        if array_eq(inst27.GetValue('uint8a'), uint8a_1):
            BookEndPrint('----- uint8a SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- uint8a SetValue/GetValue failed')
        rval = False


def main(argv=None):
    be = BookEnd('main')

    rval = True

    if bool_test() is False:
        rval = False
    if uint8_test() is False:
        rval = False
    if sint8_test() is False:
        rval = False
    if uint16_test() is False:
        rval = False
    if sint16_test() is False:
        rval = False
    if uint32_test() is False:
        rval = False
    if sint32_test() is False:
        rval = False
    if uint64_test() is False:
        rval = False
    if sint64_test() is False:
        rval = False
    if real32_test() is False:
        rval = False
    if real64_test() is False:
        rval = False
    if char16_test() is False:
        rval = False
    if timestamp_test() is False:
        rval = False
    if interval_test() is False:
        rval = False
    if string_test() is False:
        rval = False

    if booleana_test() is False:
        rval = False
    if uint8a_test() is False:
        rval = False
    if sint8a_test() is False:
        rval = False
    if uint16a_test() is False:
        rval = False
    if sint16a_test() is False:
        rval = False
    if uint32a_test() is False:
        rval = False
    if sint32a_test() is False:
        rval = False
    if uint64a_test() is False:
        rval = False
    if sint64a_test() is False:
        rval = False
    if real32a_test() is False:
        rval = False
    if real64a_test() is False:
        rval = False
    if char16a_test() is False:
        rval = False
    if datetimea_test() is False:
        rval = False
    if stringa_test() is False:
        rval = False

    if instance_test() is False:
        rval = False

    BookEndPrint('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    BookEndPrint('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    if not rval:
        BookEndPrint('!!!!!  Tests have failed!  !!!!!')
    else:
        BookEndPrint('!!!!!  All tests passed!   !!!!!')
    BookEndPrint('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    BookEndPrint('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    #fn1 ()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
