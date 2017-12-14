from omi import *

try:
    from utils import *
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from utils import *


def instance_test():
    be = BookEnd('instance_test')

    rval = True

    inst0 = MI_Instance()

    # bool
    boolValIn = MI_Boolean(True)
    inst0.SetValue('bool', boolValIn)
    boolValOut = inst0.GetValue('bool')
    if boolValIn.value != boolValOut.value:
        BookEndPrint('----- bool SetValue/GetValue failed')
        rval = False
    boolValIn.value = False
    if not boolValOut.value:
        BookEndPrint('----- bool SetValue/GetValue reference')
        rval = False
    boolValOut.value = False
    if not inst0.GetValue('bool').value:
        BookEndPrint('----- bool SetValue/GetValue stored a reference')
        rval = False

    # uint8
    uint8_0 = random.randint(0, 0xFF)
    uint8_1 = random.randint(0, 0xFF)
    uint8_2 = random.randint(0, 0xFF)
    while uint8_1 == uint8_0:
        uint8_1 = random.randint(0, 0xFF)
    while uint8_2 == uint8_0 or \
            uint8_2 == uint8_1:
        uint8_2 = random.randint(0, 0xFF)

    uint8_in = MI_Uint8(uint8_0)
    inst1 = MI_Instance()

    inst1.SetValue('uint8', uint8_in)
    uint8_out = inst1.GetValue('uint8')

    if uint8_out is not None:
        if uint8_in.value != uint8_0 or \
                inst1.GetValue('uint8').value != uint8_0 or \
                uint8_out.value != uint8_0:
            BookEndPrint('----- uint8 SetValue/GetValue failed')
            rval = False
        else:
            uint8_in.value = uint8_1
            if uint8_in.value != uint8_1 or \
                    inst1.GetValue('uint8').value != uint8_0 or \
                    uint8_out.value != uint8_0:
                BookEndPrint(
                    '----- uint8 SetValue/GetValue stored a reference')
                rval = False
            else:
                uint8_out.value = uint8_2
                if uint8_in.value != uint8_1 or \
                        inst1.GetValue('uint8').value != uint8_0 or \
                        uint8_out.value != uint8_2:
                    BookEndPrint(
                        '----- uint8 SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- uint8 SetValue/GetValue returned None')
        rval = False

    inst2 = MI_Instance()
    inst2.SetValue('uint8', inst1.GetValue('uint8'))
    if inst2.GetValue('uint8').value == inst1.GetValue('uint8').value:
        inst2.SetValue('uint8', MI_Uint8(uint8_1))
        if inst2.GetValue('uint8').value != uint8_1:
            BookEndPrint("----- uint8  SetValue failed")
            rval = False
        if inst1.GetValue('uint8').value == uint8_1:
            BookEndPrint('----- uint8 SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- uint8 SetValue/GetValue failed')
        rval = False

    # sint8
    sint8_0 = random.randint(-0x80, 0x7F)
    sint8_1 = random.randint(-0x80, 0x7F)
    sint8_2 = random.randint(-0x80, 0x7F)
    while sint8_1 == sint8_0:
        sint8_1 = random.randint(-0x80, 0x7F)
    while sint8_2 == sint8_0 or \
            sint8_2 == sint8_1:
        sint8_2 = random.randint(-0x80, 0x7F)

    sint8_in = MI_Sint8(sint8_0)
    inst3 = MI_Instance()

    inst3.SetValue('sint8', sint8_in)
    sint8_out = inst3.GetValue('sint8')

    if sint8_out is not None:
        if sint8_in.value != sint8_0 or \
                inst3.GetValue('sint8').value != sint8_0 or \
                sint8_out.value != sint8_0:
            BookEndPrint('----- sint8 SetValue/GetValue failed')
            rval = False
        else:
            sint8_in.value = sint8_1
            if sint8_in.value != sint8_1 or \
                    inst3.GetValue('sint8').value != sint8_0 or \
                    sint8_out.value != sint8_0:
                BookEndPrint(
                    '----- sint8 SetValue/GetValue stored a reference')
                rval = False
            else:
                sint8_out.value = sint8_2
                if sint8_in.value != sint8_1 or \
                        inst3.GetValue('sint8').value != sint8_0 or \
                        sint8_out.value != sint8_2:
                    BookEndPrint(
                        '----- sint8 SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- sint8 SetValue/GetValue returned None')
        rval = False

    inst4 = MI_Instance()
    inst4.SetValue('sint8', inst3.GetValue('sint8'))
    if inst4.GetValue('sint8').value == inst3.GetValue('sint8').value:
        inst4.SetValue('sint8', MI_Sint8(sint8_1))
        if inst4.GetValue('sint8').value != sint8_1:
            BookEndPrint("----- sint8  SetValue failed")
            rval = False
        if inst3.GetValue('sint8').value == sint8_1:
            BookEndPrint('----- sint8 SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- sint8 SetValue/GetValue failed')
        rval = False

    # uint16
    uint16_0 = random.randint(0, 0xFFFF)
    uint16_1 = random.randint(0, 0xFFFF)
    uint16_2 = random.randint(0, 0xFFFF)
    while uint16_1 == uint16_0:
        uint16_1 = random.randint(0, 0xFFFF)
    while uint16_2 == uint16_0 or \
            uint16_2 == uint16_1:
        uint16_2 = random.randint(0, 0xFFFF)

    uint16_in = MI_Uint16(uint16_0)
    inst5 = MI_Instance()

    inst5.SetValue('uint16', uint16_in)
    uint16_out = inst5.GetValue('uint16')

    if uint16_out is not None:
        if uint16_in.value != uint16_0 or \
                inst5.GetValue('uint16').value != uint16_0 or \
                uint16_out.value != uint16_0:
            BookEndPrint('----- uint16 SetValue/GetValue failed')
            rval = False
        else:
            uint16_in.value = uint16_1
            if uint16_in.value != uint16_1 or \
                    inst5.GetValue('uint16').value != uint16_0 or \
                    uint16_out.value != uint16_0:
                BookEndPrint(
                    '----- uint16 SetValue/GetValue stored a reference')
                rval = False
            else:
                uint16_out.value = uint16_2
                if uint16_in.value != uint16_1 or \
                        inst5.GetValue('uint16').value != uint16_0 or \
                        uint16_out.value != uint16_2:
                    BookEndPrint(
                        '----- uint16 SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- uint16 SetValue/GetValue returned None')
        rval = False

    inst6 = MI_Instance()
    inst6.SetValue('uint16', inst5.GetValue('uint16'))
    if inst6.GetValue('uint16').value == inst5.GetValue('uint16').value:
        inst6.SetValue('uint16', MI_Uint16(uint16_1))
        if inst6.GetValue('uint16').value != uint16_1:
            BookEndPrint("----- uint16  SetValue failed")
            rval = False
        if inst5.GetValue('uint16').value == uint16_1:
            BookEndPrint('----- uint16 SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- uint16 SetValue/GetValue failed')
        rval = False

    # sint16
    sint16_0 = random.randint(-0x8000, 0x7FFF)
    sint16_1 = random.randint(-0x8000, 0x7FFF)
    sint16_2 = random.randint(-0x8000, 0x7FFF)
    while sint16_1 == sint16_0:
        sint16_1 = random.randint(-0x8000, 0x7FFF)
    while sint16_2 == sint16_0 or \
            sint16_2 == sint16_1:
        sint16_2 = random.randint(-0x8000, 0x7FFF)

    sint16_in = MI_Sint16(sint16_0)
    inst7 = MI_Instance()

    inst7.SetValue('sint16', sint16_in)
    sint16_out = inst7.GetValue('sint16')

    if sint16_out is not None:
        if sint16_in.value != sint16_0 or \
                inst7.GetValue('sint16').value != sint16_0 or \
                sint16_out.value != sint16_0:
            BookEndPrint('----- sint16 SetValue/GetValue failed')
            rval = False
        else:
            sint16_in.value = sint16_1
            if sint16_in.value != sint16_1 or \
                    inst7.GetValue('sint16').value != sint16_0 or \
                    sint16_out.value != sint16_0:
                BookEndPrint(
                    '----- sint16 SetValue/GetValue stored a reference')
                rval = False
            else:
                sint16_out.value = sint16_2
                if sint16_in.value != sint16_1 or \
                        inst7.GetValue('sint16').value != sint16_0 or \
                        sint16_out.value != sint16_2:
                    BookEndPrint(
                        '----- sint16 SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- sint16 SetValue/GetValue returned None')
        rval = False

    inst8 = MI_Instance()
    inst8.SetValue('sint16', inst7.GetValue('sint16'))
    if inst8.GetValue('sint16').value == inst7.GetValue('sint16').value:
        inst8.SetValue('sint16', MI_Sint16(sint16_1))
        if inst8.GetValue('sint16').value != sint16_1:
            BookEndPrint("----- sint16  SetValue failed")
            rval = False
        if inst7.GetValue('sint16').value == sint16_1:
            BookEndPrint('----- sint16 SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- sint16 SetValue/GetValue failed')
        rval = False

    # uint32
    uint32_0 = random.randint(0, 0xFFFFFFFF)
    uint32_1 = random.randint(0, 0xFFFFFFFF)
    uint32_2 = random.randint(0, 0xFFFFFFFF)
    while uint32_1 == uint32_0:
        uint32_1 = random.randint(0, 0xFFFFFFFF)
    while uint32_2 == uint32_0 or \
            uint32_2 == uint32_1:
        uint32_2 = random.randint(0, 0xFFFFFFFF)

    uint32_in = MI_Uint32(uint32_0)
    inst9 = MI_Instance()

    inst9.SetValue('uint32', uint32_in)
    uint32_out = inst9.GetValue('uint32')

    if uint32_out is not None:
        if uint32_in.value != uint32_0 or \
                inst9.GetValue('uint32').value != uint32_0 or \
                uint32_out.value != uint32_0:
            BookEndPrint('----- uint32 SetValue/GetValue failed')
            rval = False
        else:
            uint32_in.value = uint32_1
            if uint32_in.value != uint32_1 or \
                    inst9.GetValue('uint32').value != uint32_0 or \
                    uint32_out.value != uint32_0:
                BookEndPrint(
                    '----- uint32 SetValue/GetValue stored a reference')
                rval = False
            else:
                uint32_out.value = uint32_2
                if uint32_in.value != uint32_1 or \
                        inst9.GetValue('uint32').value != uint32_0 or \
                        uint32_out.value != uint32_2:
                    BookEndPrint(
                        '----- uint32 SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- uint32 SetValue/GetValue returned None')
        rval = False

    inst10 = MI_Instance()
    inst10.SetValue('uint32', inst9.GetValue('uint32'))
    if inst10.GetValue('uint32').value == inst9.GetValue('uint32').value:
        inst10.SetValue('uint32', MI_Uint32(uint32_1))
        if inst10.GetValue('uint32').value != uint32_1:
            BookEndPrint("----- uint32  SetValue failed")
            rval = False
        if inst9.GetValue('uint32').value == uint32_1:
            BookEndPrint('----- uint32 SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- uint32 SetValue/GetValue failed')
        rval = False

    # sint32
    sint32_0 = random.randint(0, 0xFF)
    sint32_1 = random.randint(0, 0xFF)
    sint32_2 = random.randint(0, 0xFF)
    while sint32_1 == sint32_0:
        sint32_1 = random.randint(0, 0xFF)
    while sint32_2 == sint32_0 or \
            sint32_2 == sint32_1:
        sint32_2 = random.randint(0, 0xFF)

    sint32_in = MI_Sint32(sint32_0)
    inst11 = MI_Instance()

    inst11.SetValue('sint32', sint32_in)
    sint32_out = inst11.GetValue('sint32')

    if sint32_out is not None:
        if sint32_in.value != sint32_0 or \
                inst11.GetValue('sint32').value != sint32_0 or \
                sint32_out.value != sint32_0:
            BookEndPrint('----- sint32 SetValue/GetValue failed')
            rval = False
        else:
            sint32_in.value = sint32_1
            if sint32_in.value != sint32_1 or \
                    inst11.GetValue('sint32').value != sint32_0 or \
                    sint32_out.value != sint32_0:
                BookEndPrint(
                    '----- sint32 SetValue/GetValue stored a reference')
                rval = False
            else:
                sint32_out.value = sint32_2
                if sint32_in.value != sint32_1 or \
                        inst11.GetValue('sint32').value != sint32_0 or \
                        sint32_out.value != sint32_2:
                    BookEndPrint(
                        '----- sint32 SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- sint32 SetValue/GetValue returned None')
        rval = False

    inst12 = MI_Instance()
    inst12.SetValue('sint32', inst11.GetValue('sint32'))
    if inst12.GetValue('sint32').value == inst11.GetValue('sint32').value:
        inst12.SetValue('sint32', MI_Sint32(sint32_1))
        if inst12.GetValue('sint32').value != sint32_1:
            BookEndPrint("----- sint32  SetValue failed")
            rval = False
        if inst11.GetValue('sint32').value == sint32_1:
            BookEndPrint('----- sint32 SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- sint32 SetValue/GetValue failed')
        rval = False

    # uint64
    uint64_0 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    uint64_1 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    uint64_2 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    while uint64_1 == uint64_0:
        uint64_1 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    while uint64_2 == uint64_0 or \
            uint64_2 == uint64_1:
        uint64_2 = random.randint(0, 0xFFFFFFFFFFFFFFFF)

    uint64_in = MI_Uint64(uint64_0)
    inst13 = MI_Instance()

    inst13.SetValue('uint64', uint64_in)
    uint64_out = inst13.GetValue('uint64')

    if uint64_out is not None:
        if uint64_in.value != uint64_0 or \
                inst13.GetValue('uint64').value != uint64_0 or \
                uint64_out.value != uint64_0:
            BookEndPrint('----- uint64 SetValue/GetValue failed')
            rval = False
        else:
            uint64_in.value = uint64_1
            if uint64_in.value != uint64_1 or \
                    inst13.GetValue('uint64').value != uint64_0 or \
                    uint64_out.value != uint64_0:
                BookEndPrint(
                    '----- uint64 SetValue/GetValue stored a reference')
                rval = False
            else:
                uint64_out.value = uint64_2
                if uint64_in.value != uint64_1 or \
                        inst13.GetValue('uint64').value != uint64_0 or \
                        uint64_out.value != uint64_2:
                    BookEndPrint(
                        '----- uint64 SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- uint64 SetValue/GetValue returned None')
        rval = False

    inst14 = MI_Instance()
    inst14.SetValue('uint64', inst13.GetValue('uint64'))
    if inst14.GetValue('uint64').value == inst13.GetValue('uint64').value:
        inst14.SetValue('uint64', MI_Uint64(uint64_1))
        if inst14.GetValue('uint64').value != uint64_1:
            BookEndPrint("----- uint64  SetValue failed")
            rval = False
        if inst13.GetValue('uint64').value == uint64_1:
            BookEndPrint('----- uint64 SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- uint64 SetValue/GetValue failed')
        rval = False

    # sint64
    sint64_0 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    sint64_1 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    sint64_2 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    while sint64_1 == sint64_0:
        sint64_1 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    while sint64_2 == sint64_0 or \
            sint64_2 == sint64_1:
        sint64_2 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)

    sint64_in = MI_Sint64(sint64_0)
    inst15 = MI_Instance()

    inst15.SetValue('sint64', sint64_in)
    sint64_out = inst15.GetValue('sint64')

    if sint64_out is not None:
        if sint64_in.value != sint64_0 or \
                inst15.GetValue('sint64').value != sint64_0 or \
                sint64_out.value != sint64_0:
            BookEndPrint('----- sint64 SetValue/GetValue failed')
            rval = False
        else:
            sint64_in.value = sint64_1
            if sint64_in.value != sint64_1 or \
                    inst15.GetValue('sint64').value != sint64_0 or \
                    sint64_out.value != sint64_0:
                BookEndPrint(
                    '----- sint64 SetValue/GetValue stored a reference')
                rval = False
            else:
                sint64_out.value = sint64_2
                if sint64_in.value != sint64_1 or \
                        inst15.GetValue('sint64').value != sint64_0 or \
                        sint64_out.value != sint64_2:
                    BookEndPrint(
                        '----- sint64 SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- sint64 SetValue/GetValue returned None')
        rval = False

    inst16 = MI_Instance()
    inst16.SetValue('sint64', inst15.GetValue('sint64'))
    if inst16.GetValue('sint64').value == inst15.GetValue('sint64').value:
        inst16.SetValue('sint64', MI_Sint64(sint64_1))
        if inst16.GetValue('sint64').value != sint64_1:
            BookEndPrint("----- sint64  SetValue failed")
            rval = False
        if inst15.GetValue('sint64').value == sint64_1:
            BookEndPrint('----- sint64 SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- sint64 SetValue/GetValue failed')
        rval = False

    # real32
    real32_0 = ctypes.c_float(random.uniform(-1e37, 1e37))
    real32_1 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(real32_0.value, real32_1.value):
        real32_1 = ctypes.c_float(random.uniform(-1e37, 1e37))
    real32_2 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(real32_0.value, real32_2.value) or \
            float_eq(real32_1.value, real32_2.value):
        real32_2 = ctypes.c_float(random.uniform(-1e37, 1e37))

    real32_in = MI_Real32(real32_0.value)
    inst17 = MI_Instance()

    inst17.SetValue('real32', real32_in)
    real32_out = inst17.GetValue('real32')

    if real32_out is not None:
        if not float_eq(real32_in.value, real32_0.value) or \
                not float_eq(inst17.GetValue('real32').value, real32_0.value) or \
                not float_eq(real32_out.value, real32_0.value):
            BookEndPrint('----- real32 SetValue/GetValue failed')
            rval = False
        else:
            real32_in.value = real32_1.value
            if not float_eq(real32_in.value, real32_1.value) or \
                    not float_eq(inst17.GetValue('real32').value, real32_0.value) or \
                    not float_eq(real32_out.value, real32_0.value):
                BookEndPrint(
                    '----- real32 SetValue/GetValue stored a reference')
                rval = False
            else:
                real32_out.value = real32_2.value
                if not float_eq(real32_in.value, real32_1.value) or \
                        not float_eq(inst17.GetValue('real32').value, real32_0.value) or \
                        not float_eq(real32_out.value, real32_2.value):
                    BookEndPrint(
                        '----- real32 SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- real32 SetValue/GetValue returned None')
        rval = False

    inst18 = MI_Instance()
    inst18.SetValue('real32', inst17.GetValue('real32'))
    if float_eq(inst18.GetValue('real32').value, inst17.GetValue('real32').value):
        inst18.SetValue('real32', MI_Real32(real32_1.value))
        if not float_eq(inst18.GetValue('real32').value, real32_1.value):
            BookEndPrint("----- real32  SetValue failed")
            rval = False
        if float_eq(inst17.GetValue('real32').value, real32_1.value):
            BookEndPrint('----- real32 SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- real32 SetValue/GetValue failed')
        rval = False

    # real64
    real64_0 = random.uniform(-1e307, 1e307)
    real64_1 = random.uniform(-1e307, 1e307)
    while float_eq(real64_0, real64_1):
        real64_1 = random.uniform(-1e307, 1e307)
    real64_2 = random.uniform(-1e307, 1e307)
    while float_eq(real64_0, real64_2) or \
            float_eq(real64_1, real64_2):
        real64_2 = random.uniform(-1e307, 1e307)

    real64_in = MI_Real64(real64_0)
    inst19 = MI_Instance()

    inst19.SetValue('real64', real64_in)
    real64_out = inst19.GetValue('real64')

    if real64_out is not None:
        if not float_eq(real64_in.value, real64_0) or \
                not float_eq(inst19.GetValue('real64').value, real64_0) or \
                not float_eq(real64_out.value, real64_0):
            BookEndPrint('----- real64 SetValue/GetValue failed')
            rval = False
        else:
            real64_in.value = real64_1
            if not float_eq(real64_in.value, real64_1) or \
                    not float_eq(inst19.GetValue('real64').value, real64_0) or \
                    not float_eq(real64_out.value, real64_0):
                BookEndPrint(
                    '----- real64 SetValue/GetValue stored a reference')
                rval = False
            else:
                real64_out.value = real64_2
                if not float_eq(real64_in.value, real64_1) or \
                        not float_eq(inst19.GetValue('real64').value, real64_0) or \
                        not float_eq(real64_out.value, real64_2):
                    BookEndPrint(
                        '----- real64 SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- real64 SetValue/GetValue returned None')
        rval = False

    inst20 = MI_Instance()
    inst20.SetValue('real64', inst19.GetValue('real64'))
    if float_eq(inst20.GetValue('real64').value, inst19.GetValue('real64').value):
        inst20.SetValue('real64', MI_Real64(real64_1))
        if not float_eq(inst20.GetValue('real64').value, real64_1):
            BookEndPrint("----- real64  SetValue failed")
            rval = False
        if float_eq(inst19.GetValue('real64').value, real64_1):
            BookEndPrint('----- real64 SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- real64 SetValue/GetValue failed')
        rval = False

    # char16
    char16_0 = random.randint(0, 0xFFFF)
    char16_1 = random.randint(0, 0xFFFF)
    char16_2 = random.randint(0, 0xFFFF)
    while char16_1 == char16_0:
        char16_1 = random.randint(0, 0xFFFF)
    while char16_2 == char16_0 or \
            char16_2 == char16_1:
        char16_2 = random.randint(0, 0xFFFF)

    char16_in = MI_Char16(char16_0)
    inst21 = MI_Instance()

    inst21.SetValue('char16', char16_in)
    char16_out = inst21.GetValue('char16')

    if char16_out is not None:
        if char16_in.value != char16_0 or \
                inst21.GetValue('char16').value != char16_0 or \
                char16_out.value != char16_0:
            BookEndPrint('----- char16 SetValue/GetValue failed')
            rval = False
        else:
            char16_in.value = char16_1
            if char16_in.value != char16_1 or \
                    inst21.GetValue('char16').value != char16_0 or \
                    char16_out.value != char16_0:
                BookEndPrint(
                    '----- char16 SetValue/GetValue stored a reference')
                rval = False
            else:
                char16_out.value = char16_2
                if char16_in.value != char16_1 or \
                        inst21.GetValue('char16').value != char16_0 or \
                        char16_out.value != char16_2:
                    BookEndPrint(
                        '----- char16 SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- char16 SetValue/GetValue returned None')
        rval = False

    inst22 = MI_Instance()
    inst22.SetValue('char16', inst21.GetValue('char16'))
    if inst22.GetValue('char16').value == inst21.GetValue('char16').value:
        inst22.SetValue('char16', MI_Char16(char16_1))
        if inst22.GetValue('char16').value != char16_1:
            BookEndPrint("----- char16  SetValue failed")
            rval = False
        if inst21.GetValue('char16').value == char16_1:
            BookEndPrint('----- char16 SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- char16 SetValue/GetValue failed')
        rval = False

    # timestamp
    datetime_0 = MI_Timestamp(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49),
        random.randint(50, 59),
        random.randint(60, 69),
        random.randint(70, 79))
    datetime_1 = MI_Interval(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49))
    datetime_2 = MI_Timestamp(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49),
        random.randint(50, 59),
        random.randint(60, 69),
        random.randint(70, 79))

    datetime_in = datetime_0
    inst23 = MI_Instance()

    inst23.SetValue('datetime', datetime_in)
    datetime_out = inst23.GetValue('datetime')

    if datetime_out is not None:
        if not datetime_eq(datetime_in, datetime_0) or \
                not datetime_eq(inst23.GetValue('datetime'), datetime_0) or \
                not datetime_eq(datetime_out, datetime_0):
            BookEndPrint('----- datetime SetValue/GetValue failed')
            rval = False
        else:
            datetime_in = datetime_1
            if not datetime_eq(datetime_in, datetime_1) or \
                    not datetime_eq(inst23.GetValue('datetime'), datetime_0) or \
                    not datetime_eq(datetime_out, datetime_0):
                BookEndPrint(
                    '----- datetime SetValue/GetValue stored a reference')
                rval = False
            else:
                datetime_out = datetime_2
                if not datetime_eq(datetime_in, datetime_1) or \
                        not datetime_eq(inst23.GetValue('datetime'), datetime_0) or \
                        not datetime_eq(datetime_out, datetime_2):
                    BookEndPrint(
                        '----- datetime SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- datetime SetValue/GetValue returned None')
        rval = False

    inst24 = MI_Instance()
    inst24.SetValue('datetime', inst23.GetValue('datetime'))
    if datetime_eq(inst24.GetValue('datetime'), inst23.GetValue('datetime')):
        inst24.SetValue('datetime', datetime_1)
        if not datetime_eq(inst24.GetValue('datetime'), datetime_1):
            BookEndPrint("----- datetime  SetValue failed")
            rval = False
        if datetime_eq(inst23.GetValue('datetime'), datetime_1):
            BookEndPrint('----- datetime SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- datetime SetValue/GetValue failed')
        rval = False

    # string
    string_vals = [
        'apple', 'banana', 'peach', 'pear', 'orange',
        'watermelon', 'lemon', 'grapefruit', 'kiwi', 'plum',
        'chicken', 'dog', 'cat', 'goat', 'sheep',
        'rabbit', 'cow', 'horse', 'llama', 'pig'
    ]
    string_0 = random.randint(0, len(string_vals) - 1)
    string_1 = random.randint(0, len(string_vals) - 1)
    while string_0 == string_1:
        string_1 = random.randint(0, len(string_vals) - 1)
    string_2 = random.randint(0, len(string_vals) - 1)
    while string_0 == string_2 or string_1 == string_2:
        string_2 = random.randint(0, len(string_vals) - 1)

    string_0 = string_vals[string_0]
    string_1 = string_vals[string_1]
    string_2 = string_vals[string_2]

    uint8_0 = random.randint(0, 0xFF)
    uint8_1 = random.randint(0, 0xFF)
    uint8_2 = random.randint(0, 0xFF)
    while uint8_1 == uint8_0:
        uint8_1 = random.randint(0, 0xFF)
    while uint8_2 == uint8_0 or \
            uint8_2 == uint8_1:
        uint8_2 = random.randint(0, 0xFF)

    string_in = MI_String(string_0)
    inst25 = MI_Instance()

    inst25.SetValue('string', string_in)
    string_out = inst25.GetValue('string')

    if string_out is not None:
        if string_in.value != string_0 or \
                inst25.GetValue('string').value != string_0 or \
                string_out.value != string_0:
            BookEndPrint('----- string SetValue/GetValue failed')
            rval = False
        else:
            string_in.value = string_1
            if string_in.value != string_1 or \
                    inst25.GetValue('string').value != string_0 or \
                    string_out.value != string_0:
                BookEndPrint(
                    '----- string SetValue/GetValue stored a reference')
                rval = False
            else:
                string_out.value = string_2
                if string_in.value != string_1 or \
                        inst25.GetValue('string').value != string_0 or \
                        string_out.value != string_2:
                    BookEndPrint(
                        '----- string SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- string SetValue/GetValue returned None')
        rval = False

    inst26 = MI_Instance()
    inst26.SetValue('string', inst25.GetValue('string'))
    if inst26.GetValue('string').value == inst25.GetValue('string').value:
        inst26.SetValue('string', MI_String(string_1))
        if inst26.GetValue('string').value != string_1:
            BookEndPrint("----- string  SetValue failed")
            rval = False
        if inst25.GetValue('string').value == string_1:
            BookEndPrint('----- string SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- string SetValue/GetValue failed')
        rval = False

    # uint8a
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
                    uint8a_out = inst27.GetValue('uint8a')
                    uint8a_out.setValueAt(0, uint8_2)
                    if array_eq(uint8a_out, inst27.GetValue('uint8a')) or \
                       array_eq(uint8a_out, uint8a_2):
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

    # sint8a
    sint8_3 = random.randint(-0x80, 0x7F)
    while sint8_0 == sint8_3 or \
            sint8_1 == sint8_3 or \
            sint8_2 == sint8_3:
        sint8_3 = random.randint(-0x80, 0x7F)
    sint8_4 = random.randint(-0x80, 0x7F)
    while sint8_0 == sint8_4 or \
            sint8_1 == sint8_4 or \
            sint8_2 == sint8_4 or \
            sint8_3 == sint8_4:
        sint8_4 = random.randint(-0x80, 0x7F)
    sint8_5 = random.randint(-0x80, 0x7F)
    while sint8_0 == sint8_5 or \
            sint8_1 == sint8_5 or \
            sint8_2 == sint8_5 or \
            sint8_3 == sint8_5 or \
            sint8_4 == sint8_5:
        sint8_5 = random.randint(-0x80, 0x7F)
    sint8_6 = random.randint(-0x80, 0x7F)
    while sint8_0 == sint8_6 or \
            sint8_1 == sint8_6 or \
            sint8_2 == sint8_6 or \
            sint8_3 == sint8_6 or \
            sint8_4 == sint8_6 or \
            sint8_5 == sint8_6:
        sint8_6 = random.randint(-0x80, 0x7F)
    sint8_7 = random.randint(-0x80, 0x7F)
    while sint8_0 == sint8_7 or \
            sint8_1 == sint8_7 or \
            sint8_2 == sint8_7 or \
            sint8_3 == sint8_7 or \
            sint8_4 == sint8_7 or \
            sint8_5 == sint8_7 or \
            sint8_6 == sint8_7:
        sint8_7 = random.randint(-0x80, 0x7F)
    sint8_8 = random.randint(-0x80, 0x7F)
    while sint8_0 == sint8_8 or \
            sint8_1 == sint8_8 or \
            sint8_2 == sint8_8 or \
            sint8_3 == sint8_8 or \
            sint8_4 == sint8_8 or \
            sint8_5 == sint8_8 or \
            sint8_6 == sint8_8 or \
            sint8_7 == sint8_8:
        sint8_8 = random.randint(-0x80, 0x7F)

    sint8a_0 = MI_Sint8A((sint8_0, sint8_1, sint8_2))
    sint8a_1 = MI_Sint8A((sint8_3, sint8_4, sint8_5))
    sint8a_2 = MI_Sint8A((sint8_6, sint8_7, sint8_8))

    sint8a_in = sint8a_0
    inst29 = MI_Instance()

    inst29.SetValue('sint8a', sint8a_in)
    sint8a_out = inst29.GetValue('sint8a')

    if sint8a_out is not None:
        if not array_eq(sint8a_in, sint8a_0) or \
                not array_eq(inst29.GetValue('sint8a'), sint8a_0) or \
                not array_eq(sint8a_out, sint8a_0):
            BookEndPrint('----- sint8a SetValue/GetValue failed')
            rval = False
        else:
            sint8a_in = sint8a_1
            if not array_eq(sint8a_in, sint8a_1) or \
                    not array_eq(inst29.GetValue('sint8a'), sint8a_0) or \
                    not array_eq(sint8a_out, sint8a_0):
                BookEndPrint(
                    '----- sint8a SetValue/GetValue stored a reference')
                rval = False
            else:
                sint8a_out = sint8a_2
                if not array_eq(sint8a_in, sint8a_1) or \
                        not array_eq(inst29.GetValue('sint8a'), sint8a_0) or \
                        not array_eq(sint8a_out, sint8a_2):
                    BookEndPrint(
                        '----- sint8a SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- sint8a SetValue/GetValue returned None')
        rval = False

    inst30 = MI_Instance()
    inst30.SetValue('sint8a', inst29.GetValue('sint8a'))
    if array_eq(inst30.GetValue('sint8a'), inst29.GetValue('sint8a')):
        inst30.SetValue('sint8a', sint8a_1)
        if not array_eq(inst30.GetValue('sint8a'), sint8a_1):
            BookEndPrint("----- sint8a  SetValue failed")
            rval = False
        if array_eq(inst29.GetValue('sint8a'), sint8a_1):
            BookEndPrint('----- sint8a SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- sint8a SetValue/GetValue failed')
        rval = False

    # uint16a
    uint16_3 = random.randint(0, 0xFFFF)
    while uint16_0 == uint16_3 or \
            uint16_1 == uint16_3 or \
            uint16_2 == uint16_3:
        uint16_3 = random.randint(0, 0xFFFF)
    uint16_4 = random.randint(0, 0xFFFF)
    while uint16_0 == uint16_4 or \
            uint16_1 == uint16_4 or \
            uint16_2 == uint16_4 or \
            uint16_3 == uint16_4:
        uint16_4 = random.randint(0, 0xFFFF)
    uint16_5 = random.randint(0, 0xFFFF)
    while uint16_0 == uint16_5 or \
            uint16_1 == uint16_5 or \
            uint16_2 == uint16_5 or \
            uint16_3 == uint16_5 or \
            uint16_4 == uint16_5:
        uint16_5 = random.randint(0, 0xFFFF)
    uint16_6 = random.randint(0, 0xFFFF)
    while uint16_0 == uint16_6 or \
            uint16_1 == uint16_6 or \
            uint16_2 == uint16_6 or \
            uint16_3 == uint16_6 or \
            uint16_4 == uint16_6 or \
            uint16_5 == uint16_6:
        uint16_6 = random.randint(0, 0xFFFF)
    uint16_7 = random.randint(0, 0xFFFF)
    while uint16_0 == uint16_7 or \
            uint16_1 == uint16_7 or \
            uint16_2 == uint16_7 or \
            uint16_3 == uint16_7 or \
            uint16_4 == uint16_7 or \
            uint16_5 == uint16_7 or \
            uint16_6 == uint16_7:
        uint16_7 = random.randint(0, 0xFFFF)
    uint16_8 = random.randint(0, 0xFFFF)
    while uint16_0 == uint16_8 or \
            uint16_1 == uint16_8 or \
            uint16_2 == uint16_8 or \
            uint16_3 == uint16_8 or \
            uint16_4 == uint16_8 or \
            uint16_5 == uint16_8 or \
            uint16_6 == uint16_8 or \
            uint16_7 == uint16_8:
        uint16_8 = random.randint(0, 0xFFFF)

    uint16a_0 = MI_Uint16A((uint16_0, uint16_1, uint16_2))
    uint16a_1 = MI_Uint16A((uint16_3, uint16_4, uint16_5))
    uint16a_2 = MI_Uint16A((uint16_6, uint16_7, uint16_8))

    uint16a_in = uint16a_0
    inst31 = MI_Instance()

    inst31.SetValue('uint16a', uint16a_in)
    uint16a_out = inst31.GetValue('uint16a')

    if uint16a_out is not None:
        if not array_eq(uint16a_in, uint16a_0) or \
                not array_eq(inst31.GetValue('uint16a'), uint16a_0) or \
                not array_eq(uint16a_out, uint16a_0):
            BookEndPrint('----- uint16a SetValue/GetValue failed')
            rval = False
        else:
            uint16a_in = uint16a_1
            if not array_eq(uint16a_in, uint16a_1) or \
                    not array_eq(inst31.GetValue('uint16a'), uint16a_0) or \
                    not array_eq(uint16a_out, uint16a_0):
                BookEndPrint(
                    '----- uint16a SetValue/GetValue stored a reference')
                rval = False
            else:
                uint16a_out = uint16a_2
                if not array_eq(uint16a_in, uint16a_1) or \
                        not array_eq(inst31.GetValue('uint16a'), uint16a_0) or \
                        not array_eq(uint16a_out, uint16a_2):
                    BookEndPrint(
                        '----- uint16a SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- uint16a SetValue/GetValue returned None')
        rval = False

    inst32 = MI_Instance()
    inst32.SetValue('uint16a', inst31.GetValue('uint16a'))
    if array_eq(inst32.GetValue('uint16a'), inst31.GetValue('uint16a')):
        inst32.SetValue('uint16a', uint16a_1)
        if not array_eq(inst32.GetValue('uint16a'), uint16a_1):
            BookEndPrint("----- uint16a  SetValue failed")
            rval = False
        if array_eq(inst31.GetValue('uint16a'), uint16a_1):
            BookEndPrint('----- uint16a SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- uint16a SetValue/GetValue failed')
        rval = False

    # sint16a
    sint16_3 = random.randint(-0x8000, 0x7FFF)
    while sint16_0 == sint16_3 or \
            sint16_1 == sint16_3 or \
            sint16_2 == sint16_3:
        sint16_3 = random.randint(-0x8000, 0x7FFF)
    sint16_4 = random.randint(-0x8000, 0x7FFF)
    while sint16_0 == sint16_4 or \
            sint16_1 == sint16_4 or \
            sint16_2 == sint16_4 or \
            sint16_3 == sint16_4:
        sint16_4 = random.randint(-0x8000, 0x7FFF)
    sint16_5 = random.randint(-0x8000, 0x7FFF)
    while sint16_0 == sint16_5 or \
            sint16_1 == sint16_5 or \
            sint16_2 == sint16_5 or \
            sint16_3 == sint16_5 or \
            sint16_4 == sint16_5:
        sint16_5 = random.randint(-0x8000, 0x7FFF)
    sint16_6 = random.randint(-0x8000, 0x7FFF)
    while sint16_0 == sint16_6 or \
            sint16_1 == sint16_6 or \
            sint16_2 == sint16_6 or \
            sint16_3 == sint16_6 or \
            sint16_4 == sint16_6 or \
            sint16_5 == sint16_6:
        sint16_6 = random.randint(-0x8000, 0x7FFF)
    sint16_7 = random.randint(-0x8000, 0x7FFF)
    while sint16_0 == sint16_7 or \
            sint16_1 == sint16_7 or \
            sint16_2 == sint16_7 or \
            sint16_3 == sint16_7 or \
            sint16_4 == sint16_7 or \
            sint16_5 == sint16_7 or \
            sint16_6 == sint16_7:
        sint16_7 = random.randint(-0x8000, 0x7FFF)
    sint16_8 = random.randint(-0x8000, 0x7FFF)
    while sint16_0 == sint16_8 or \
            sint16_1 == sint16_8 or \
            sint16_2 == sint16_8 or \
            sint16_3 == sint16_8 or \
            sint16_4 == sint16_8 or \
            sint16_5 == sint16_8 or \
            sint16_6 == sint16_8 or \
            sint16_7 == sint16_8:
        sint16_8 = random.randint(-0x8000, 0x7FFF)

    sint16a_0 = MI_Sint16A((sint16_0, sint16_1, sint16_2))
    sint16a_1 = MI_Sint16A((sint16_3, sint16_4, sint16_5))
    sint16a_2 = MI_Sint16A((sint16_6, sint16_7, sint16_8))

    sint16a_in = sint16a_0
    inst33 = MI_Instance()

    inst33.SetValue('sint16a', sint16a_in)
    sint16a_out = inst33.GetValue('sint16a')

    if sint16a_out is not None:
        if not array_eq(sint16a_in, sint16a_0) or \
                not array_eq(inst33.GetValue('sint16a'), sint16a_0) or \
                not array_eq(sint16a_out, sint16a_0):
            BookEndPrint('----- sint16a SetValue/GetValue failed')
            rval = False
        else:
            sint16a_in = sint16a_1
            if not array_eq(sint16a_in, sint16a_1) or \
                    not array_eq(inst33.GetValue('sint16a'), sint16a_0) or \
                    not array_eq(sint16a_out, sint16a_0):
                BookEndPrint(
                    '----- sint16a SetValue/GetValue stored a reference')
                rval = False
            else:
                sint16a_out = sint16a_2
                if not array_eq(sint16a_in, sint16a_1) or \
                        not array_eq(inst33.GetValue('sint16a'), sint16a_0) or \
                        not array_eq(sint16a_out, sint16a_2):
                    BookEndPrint(
                        '----- sint16a SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- sint16a SetValue/GetValue returned None')
        rval = False

    inst34 = MI_Instance()
    inst34.SetValue('sint16a', inst33.GetValue('sint16a'))
    if array_eq(inst34.GetValue('sint16a'), inst33.GetValue('sint16a')):
        inst34.SetValue('sint16a', sint16a_1)
        if not array_eq(inst34.GetValue('sint16a'), sint16a_1):
            BookEndPrint("----- sint16a  SetValue failed")
            rval = False
        if array_eq(inst33.GetValue('sint16a'), sint16a_1):
            BookEndPrint('----- sint16a SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- sint16a SetValue/GetValue failed')
        rval = False

    # uint32a
    uint32_3 = random.randint(0, 0xFFFFFFFF)
    while uint32_0 == uint32_3 or \
            uint32_1 == uint32_3 or \
            uint32_2 == uint32_3:
        uint32_3 = random.randint(0, 0xFFFFFFFF)
    uint32_4 = random.randint(0, 0xFFFFFFFF)
    while uint32_0 == uint32_4 or \
            uint32_1 == uint32_4 or \
            uint32_2 == uint32_4 or \
            uint32_3 == uint32_4:
        uint32_4 = random.randint(0, 0xFFFFFFFF)
    uint32_5 = random.randint(0, 0xFFFFFFFF)
    while uint32_0 == uint32_5 or \
            uint32_1 == uint32_5 or \
            uint32_2 == uint32_5 or \
            uint32_3 == uint32_5 or \
            uint32_4 == uint32_5:
        uint32_5 = random.randint(0, 0xFFFFFFFF)
    uint32_6 = random.randint(0, 0xFFFFFFFF)
    while uint32_0 == uint32_6 or \
            uint32_1 == uint32_6 or \
            uint32_2 == uint32_6 or \
            uint32_3 == uint32_6 or \
            uint32_4 == uint32_6 or \
            uint32_5 == uint32_6:
        uint32_6 = random.randint(0, 0xFFFFFFFF)
    uint32_7 = random.randint(0, 0xFFFFFFFF)
    while uint32_0 == uint32_7 or \
            uint32_1 == uint32_7 or \
            uint32_2 == uint32_7 or \
            uint32_3 == uint32_7 or \
            uint32_4 == uint32_7 or \
            uint32_5 == uint32_7 or \
            uint32_6 == uint32_7:
        uint32_7 = random.randint(0, 0xFFFFFFFF)
    uint32_8 = random.randint(0, 0xFFFFFFFF)
    while uint32_0 == uint32_8 or \
            uint32_1 == uint32_8 or \
            uint32_2 == uint32_8 or \
            uint32_3 == uint32_8 or \
            uint32_4 == uint32_8 or \
            uint32_5 == uint32_8 or \
            uint32_6 == uint32_8 or \
            uint32_7 == uint32_8:
        uint32_8 = random.randint(0, 0xFFFFFFFF)

    uint32a_0 = MI_Uint32A((uint32_0, uint32_1, uint32_2))
    uint32a_1 = MI_Uint32A((uint32_3, uint32_4, uint32_5))
    uint32a_2 = MI_Uint32A((uint32_6, uint32_7, uint32_8))

    uint32a_in = uint32a_0
    inst35 = MI_Instance()

    inst35.SetValue('uint32a', uint32a_in)
    uint32a_out = inst35.GetValue('uint32a')

    if uint32a_out is not None:
        if not array_eq(uint32a_in, uint32a_0) or \
                not array_eq(inst35.GetValue('uint32a'), uint32a_0) or \
                not array_eq(uint32a_out, uint32a_0):
            BookEndPrint('----- uint32a SetValue/GetValue failed')
            rval = False
        else:
            uint32a_in = uint32a_1
            if not array_eq(uint32a_in, uint32a_1) or \
                    not array_eq(inst35.GetValue('uint32a'), uint32a_0) or \
                    not array_eq(uint32a_out, uint32a_0):
                BookEndPrint(
                    '----- uint32a SetValue/GetValue stored a reference')
                rval = False
            else:
                uint32a_out = uint32a_2
                if not array_eq(uint32a_in, uint32a_1) or \
                        not array_eq(inst35.GetValue('uint32a'), uint32a_0) or \
                        not array_eq(uint32a_out, uint32a_2):
                    BookEndPrint(
                        '----- uint32a SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- uint32a SetValue/GetValue returned None')
        rval = False

    inst36 = MI_Instance()
    inst36.SetValue('uint32a', inst35.GetValue('uint32a'))
    if array_eq(inst36.GetValue('uint32a'), inst35.GetValue('uint32a')):
        inst36.SetValue('uint32a', uint32a_1)
        if not array_eq(inst36.GetValue('uint32a'), uint32a_1):
            BookEndPrint("----- uint32a  SetValue failed")
            rval = False
        if array_eq(inst35.GetValue('uint32a'), uint32a_1):
            BookEndPrint('----- uint32a SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- uint32a SetValue/GetValue failed')
        rval = False

    # sint32a
    sint32_3 = random.randint(-0x80000000, 0x7FFFFFFF)
    while sint32_0 == sint32_3 or \
            sint32_1 == sint32_3 or \
            sint32_2 == sint32_3:
        sint32_3 = random.randint(-0x80000000, 0x7FFFFFFF)
    sint32_4 = random.randint(-0x80000000, 0x7FFFFFFF)
    while sint32_0 == sint32_4 or \
            sint32_1 == sint32_4 or \
            sint32_2 == sint32_4 or \
            sint32_3 == sint32_4:
        sint32_4 = random.randint(-0x80000000, 0x7FFFFFFF)
    sint32_5 = random.randint(-0x80000000, 0x7FFFFFFF)
    while sint32_0 == sint32_5 or \
            sint32_1 == sint32_5 or \
            sint32_2 == sint32_5 or \
            sint32_3 == sint32_5 or \
            sint32_4 == sint32_5:
        sint32_5 = random.randint(-0x80000000, 0x7FFFFFFF)
    sint32_6 = random.randint(-0x80000000, 0x7FFFFFFF)
    while sint32_0 == sint32_6 or \
            sint32_1 == sint32_6 or \
            sint32_2 == sint32_6 or \
            sint32_3 == sint32_6 or \
            sint32_4 == sint32_6 or \
            sint32_5 == sint32_6:
        sint32_6 = random.randint(-0x80000000, 0x7FFFFFFF)
    sint32_7 = random.randint(-0x80000000, 0x7FFFFFFF)
    while sint32_0 == sint32_7 or \
            sint32_1 == sint32_7 or \
            sint32_2 == sint32_7 or \
            sint32_3 == sint32_7 or \
            sint32_4 == sint32_7 or \
            sint32_5 == sint32_7 or \
            sint32_6 == sint32_7:
        sint32_7 = random.randint(-0x80000000, 0x7FFFFFFF)
    sint32_8 = random.randint(-0x80000000, 0x7FFFFFFF)
    while sint32_0 == sint32_8 or \
            sint32_1 == sint32_8 or \
            sint32_2 == sint32_8 or \
            sint32_3 == sint32_8 or \
            sint32_4 == sint32_8 or \
            sint32_5 == sint32_8 or \
            sint32_6 == sint32_8 or \
            sint32_7 == sint32_8:
        sint32_8 = random.randint(-0x80000000, 0x7FFFFFFF)

    sint32a_0 = MI_Sint32A((sint32_0, sint32_1, sint32_2))
    sint32a_1 = MI_Sint32A((sint32_3, sint32_4, sint32_5))
    sint32a_2 = MI_Sint32A((sint32_6, sint32_7, sint32_8))

    sint32a_in = sint32a_0
    inst37 = MI_Instance()

    inst37.SetValue('sint32a', sint32a_in)
    sint32a_out = inst37.GetValue('sint32a')

    if sint32a_out is not None:
        if not array_eq(sint32a_in, sint32a_0) or \
                not array_eq(inst37.GetValue('sint32a'), sint32a_0) or \
                not array_eq(sint32a_out, sint32a_0):
            BookEndPrint('----- sint32a SetValue/GetValue failed')
            rval = False
        else:
            sint32a_in = sint32a_1
            if not array_eq(sint32a_in, sint32a_1) or \
                    not array_eq(inst37.GetValue('sint32a'), sint32a_0) or \
                    not array_eq(sint32a_out, sint32a_0):
                BookEndPrint(
                    '----- sint32a SetValue/GetValue stored a reference')
                rval = False
            else:
                sint32a_out = sint32a_2
                if not array_eq(sint32a_in, sint32a_1) or \
                        not array_eq(inst37.GetValue('sint32a'), sint32a_0) or \
                        not array_eq(sint32a_out, sint32a_2):
                    BookEndPrint(
                        '----- sint32a SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- sint32a SetValue/GetValue returned None')
        rval = False

    inst38 = MI_Instance()
    inst38.SetValue('sint32a', inst37.GetValue('sint32a'))
    if array_eq(inst38.GetValue('sint32a'), inst37.GetValue('sint32a')):
        inst38.SetValue('sint32a', sint32a_1)
        if not array_eq(inst38.GetValue('sint32a'), sint32a_1):
            BookEndPrint("----- sint32a  SetValue failed")
            rval = False
        if array_eq(inst37.GetValue('sint32a'), sint32a_1):
            BookEndPrint('----- sint32a SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- sint32a SetValue/GetValue failed')
        rval = False

    # uint64a
    uint64_3 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    while uint64_0 == uint64_3 or \
            uint64_1 == uint64_3 or \
            uint64_2 == uint64_3:
        uint64_3 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    uint64_4 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    while uint64_0 == uint64_4 or \
            uint64_1 == uint64_4 or \
            uint64_2 == uint64_4 or \
            uint64_3 == uint64_4:
        uint64_4 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    uint64_5 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    while uint64_0 == uint64_5 or \
            uint64_1 == uint64_5 or \
            uint64_2 == uint64_5 or \
            uint64_3 == uint64_5 or \
            uint64_4 == uint64_5:
        uint64_5 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    uint64_6 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    while uint64_0 == uint64_6 or \
            uint64_1 == uint64_6 or \
            uint64_2 == uint64_6 or \
            uint64_3 == uint64_6 or \
            uint64_4 == uint64_6 or \
            uint64_5 == uint64_6:
        uint64_6 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    uint64_7 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    while uint64_0 == uint64_7 or \
            uint64_1 == uint64_7 or \
            uint64_2 == uint64_7 or \
            uint64_3 == uint64_7 or \
            uint64_4 == uint64_7 or \
            uint64_5 == uint64_7 or \
            uint64_6 == uint64_7:
        uint64_7 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    uint64_8 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    while uint64_0 == uint64_8 or \
            uint64_1 == uint64_8 or \
            uint64_2 == uint64_8 or \
            uint64_3 == uint64_8 or \
            uint64_4 == uint64_8 or \
            uint64_5 == uint64_8 or \
            uint64_6 == uint64_8 or \
            uint64_7 == uint64_8:
        uint64_8 = random.randint(0, 0xFFFFFFFFFFFFFFFF)

    uint64a_0 = MI_Uint64A((uint64_0, uint64_1, uint64_2))
    uint64a_1 = MI_Uint64A((uint64_3, uint64_4, uint64_5))
    uint64a_2 = MI_Uint64A((uint64_6, uint64_7, uint64_8))

    uint64a_in = uint64a_0
    inst39 = MI_Instance()

    inst39.SetValue('uint64a', uint64a_in)
    uint64a_out = inst39.GetValue('uint64a')

    if uint64a_out is not None:
        if not array_eq(uint64a_in, uint64a_0) or \
                not array_eq(inst39.GetValue('uint64a'), uint64a_0) or \
                not array_eq(uint64a_out, uint64a_0):
            BookEndPrint('----- uint64a SetValue/GetValue failed')
            rval = False
        else:
            uint64a_in = uint64a_1
            if not array_eq(uint64a_in, uint64a_1) or \
                    not array_eq(inst39.GetValue('uint64a'), uint64a_0) or \
                    not array_eq(uint64a_out, uint64a_0):
                BookEndPrint(
                    '----- uint64a SetValue/GetValue stored a reference')
                rval = False
            else:
                uint64a_out = uint64a_2
                if not array_eq(uint64a_in, uint64a_1) or \
                        not array_eq(inst39.GetValue('uint64a'), uint64a_0) or \
                        not array_eq(uint64a_out, uint64a_2):
                    BookEndPrint(
                        '----- uint64a SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- uint64a SetValue/GetValue returned None')
        rval = False

    inst40 = MI_Instance()
    inst40.SetValue('uint64a', inst39.GetValue('uint64a'))
    if array_eq(inst40.GetValue('uint64a'), inst39.GetValue('uint64a')):
        inst40.SetValue('uint64a', uint64a_1)
        if not array_eq(inst40.GetValue('uint64a'), uint64a_1):
            BookEndPrint("----- uint64a  SetValue failed")
            rval = False
        if array_eq(inst39.GetValue('uint64a'), uint64a_1):
            BookEndPrint('----- uint64a SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- uint64a SetValue/GetValue failed')
        rval = False

    # sint64a
    sint64_3 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    while sint64_0 == sint64_3 or \
            sint64_1 == sint64_3 or \
            sint64_2 == sint64_3:
        sint64_3 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    sint64_4 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    while sint64_0 == sint64_4 or \
            sint64_1 == sint64_4 or \
            sint64_2 == sint64_4 or \
            sint64_3 == sint64_4:
        sint64_4 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    sint64_5 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    while sint64_0 == sint64_5 or \
            sint64_1 == sint64_5 or \
            sint64_2 == sint64_5 or \
            sint64_3 == sint64_5 or \
            sint64_4 == sint64_5:
        sint64_5 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    sint64_6 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    while sint64_0 == sint64_6 or \
            sint64_1 == sint64_6 or \
            sint64_2 == sint64_6 or \
            sint64_3 == sint64_6 or \
            sint64_4 == sint64_6 or \
            sint64_5 == sint64_6:
        sint64_6 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    sint64_7 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    while sint64_0 == sint64_7 or \
            sint64_1 == sint64_7 or \
            sint64_2 == sint64_7 or \
            sint64_3 == sint64_7 or \
            sint64_4 == sint64_7 or \
            sint64_5 == sint64_7 or \
            sint64_6 == sint64_7:
        sint64_7 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    sint64_8 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    while sint64_0 == sint64_8 or \
            sint64_1 == sint64_8 or \
            sint64_2 == sint64_8 or \
            sint64_3 == sint64_8 or \
            sint64_4 == sint64_8 or \
            sint64_5 == sint64_8 or \
            sint64_6 == sint64_8 or \
            sint64_7 == sint64_8:
        sint64_8 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)

    sint64a_0 = MI_Sint64A((sint64_0, sint64_1, sint64_2))
    sint64a_1 = MI_Sint64A((sint64_3, sint64_4, sint64_5))
    sint64a_2 = MI_Sint64A((sint64_6, sint64_7, sint64_8))

    sint64a_in = sint64a_0
    inst41 = MI_Instance()

    inst41.SetValue('sint64a', sint64a_in)
    sint64a_out = inst41.GetValue('sint64a')

    if sint64a_out is not None:
        if not array_eq(sint64a_in, sint64a_0) or \
                not array_eq(inst41.GetValue('sint64a'), sint64a_0) or \
                not array_eq(sint64a_out, sint64a_0):
            BookEndPrint('----- sint64a SetValue/GetValue failed')
            rval = False
        else:
            sint64a_in = sint64a_1
            if not array_eq(sint64a_in, sint64a_1) or \
                    not array_eq(inst41.GetValue('sint64a'), sint64a_0) or \
                    not array_eq(sint64a_out, sint64a_0):
                BookEndPrint(
                    '----- sint64a SetValue/GetValue stored a reference')
                rval = False
            else:
                sint64a_out = sint64a_2
                if not array_eq(sint64a_in, sint64a_1) or \
                        not array_eq(inst41.GetValue('sint64a'), sint64a_0) or \
                        not array_eq(sint64a_out, sint64a_2):
                    BookEndPrint(
                        '----- sint64a SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- sint64a SetValue/GetValue returned None')
        rval = False

    inst42 = MI_Instance()
    inst42.SetValue('sint64a', inst41.GetValue('sint64a'))
    if array_eq(inst42.GetValue('sint64a'), inst41.GetValue('sint64a')):
        inst42.SetValue('sint64a', sint64a_1)
        if not array_eq(inst42.GetValue('sint64a'), sint64a_1):
            BookEndPrint("----- sint64a  SetValue failed")
            rval = False
        if array_eq(inst41.GetValue('sint64a'), sint64a_1):
            BookEndPrint('----- sint64a SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- sint64a SetValue/GetValue failed')
        rval = False

    # real32a
    real32_3 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(real32_0.value, real32_3.value) or \
            float_eq(real32_1.value, real32_3.value) or \
            float_eq(real32_2.value, real32_3.value):
        real32_3 = ctypes.c_float(random.uniform(-1e37, 1e37))
    real32_4 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(real32_0.value, real32_4.value) or \
            float_eq(real32_1.value, real32_4.value) or \
            float_eq(real32_2.value, real32_4.value) or \
            float_eq(real32_3.value, real32_4.value):
        real32_4 = ctypes.c_float(random.uniform(-1e37, 1e37))
    real32_5 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(real32_0.value, real32_5.value) or \
            float_eq(real32_1.value, real32_5.value) or \
            float_eq(real32_2.value, real32_5.value) or \
            float_eq(real32_3.value, real32_5.value) or \
            float_eq(real32_4.value, real32_5.value):
        real32_5 = ctypes.c_float(random.uniform(-1e37, 1e37))
    real32_6 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(real32_0.value, real32_6.value) or \
            float_eq(real32_1.value, real32_6.value) or \
            float_eq(real32_2.value, real32_6.value) or \
            float_eq(real32_3.value, real32_6.value) or \
            float_eq(real32_4.value, real32_6.value) or \
            float_eq(real32_5.value, real32_6.value):
        real32_6 = ctypes.c_float(random.uniform(-1e37, 1e37))
    real32_7 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(real32_0.value, real32_7.value) or \
            float_eq(real32_1.value, real32_7.value) or \
            float_eq(real32_2.value, real32_7.value) or \
            float_eq(real32_3.value, real32_7.value) or \
            float_eq(real32_4.value, real32_7.value) or \
            float_eq(real32_5.value, real32_7.value) or \
            float_eq(real32_6.value, real32_7.value):
        real32_7 = ctypes.c_float(random.uniform(-1e37, 1e37))
    real32_8 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(real32_0.value, real32_8.value) or \
            float_eq(real32_1.value, real32_8.value) or \
            float_eq(real32_2.value, real32_8.value) or \
            float_eq(real32_3.value, real32_8.value) or \
            float_eq(real32_4.value, real32_8.value) or \
            float_eq(real32_5.value, real32_8.value) or \
            float_eq(real32_6.value, real32_8.value) or \
            float_eq(real32_7.value, real32_8.value):
        real32_8 = ctypes.c_float(random.uniform(-1e37, 1e37))

    real32a_0 = MI_Real32A((real32_0.value, real32_1.value, real32_2.value))
    real32a_1 = MI_Real32A((real32_3.value, real32_4.value, real32_5.value))
    real32a_2 = MI_Real32A((real32_6.value, real32_7.value, real32_8.value))

    real32a_in = real32a_0
    inst43 = MI_Instance()

    inst43.SetValue('real32a', real32a_in)
    real32a_out = inst43.GetValue('real32a')

    if real32a_out is not None:
        if not float_array_eq(real32a_in, real32a_0) or \
                not float_array_eq(inst43.GetValue('real32a'), real32a_0) or \
                not float_array_eq(real32a_out, real32a_0):
            BookEndPrint('----- real32a SetValue/GetValue failed')
            rval = False
        else:
            real32a_in = real32a_1
            if not float_array_eq(real32a_in, real32a_1) or \
                    not float_array_eq(inst43.GetValue('real32a'), real32a_0) or \
                    not float_array_eq(real32a_out, real32a_0):
                BookEndPrint(
                    '----- real32a SetValue/GetValue stored a reference')
                rval = False
            else:
                real32a_out = real32a_2
                if not float_array_eq(real32a_in, real32a_1) or \
                        not float_array_eq(inst43.GetValue('real32a'), real32a_0) or \
                        not float_array_eq(real32a_out, real32a_2):
                    BookEndPrint(
                        '----- real32a SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- real32a SetValue/GetValue returned None')
        rval = False

    inst44 = MI_Instance()
    inst44.SetValue('real32a', inst43.GetValue('real32a'))
    if float_array_eq(inst44.GetValue('real32a'), inst43.GetValue('real32a')):
        inst44.SetValue('real32a', real32a_1)
        if not float_array_eq(inst44.GetValue('real32a'), real32a_1):
            BookEndPrint("----- real32a  SetValue failed")
            rval = False
        if float_array_eq(inst43.GetValue('real32a'), real32a_1):
            BookEndPrint('----- real32a SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- real32a SetValue/GetValue failed')
        rval = False

    # real64a
    real64_3 = random.uniform(-1e307, 1e307)
    while float_eq(real64_0, real64_3) or \
            float_eq(real64_1, real64_3) or \
            float_eq(real64_2, real64_3):
        real64_3 = random.uniform(-1e307, 1e307)
    real64_4 = random.uniform(-1e307, 1e307)
    while float_eq(real64_0, real64_4) or \
            float_eq(real64_1, real64_4) or \
            float_eq(real64_2, real64_4) or \
            float_eq(real64_3, real64_4):
        real64_4 = random.uniform(-1e307, 1e307)
    real64_5 = random.uniform(-1e307, 1e307)
    while float_eq(real64_0, real64_5) or \
            float_eq(real64_1, real64_5) or \
            float_eq(real64_2, real64_5) or \
            float_eq(real64_3, real64_5) or \
            float_eq(real64_4, real64_5):
        real64_5 = random.uniform(-1e307, 1e307)
    real64_6 = random.uniform(-1e307, 1e307)
    while float_eq(real64_0, real64_6) or \
            float_eq(real64_1, real64_6) or \
            float_eq(real64_2, real64_6) or \
            float_eq(real64_3, real64_6) or \
            float_eq(real64_4, real64_6) or \
            float_eq(real64_5, real64_6):
        real64_6 = random.uniform(-1e307, 1e307)
    real64_7 = random.uniform(-1e307, 1e307)
    while float_eq(real64_0, real64_7) or \
            float_eq(real64_1, real64_7) or \
            float_eq(real64_2, real64_7) or \
            float_eq(real64_3, real64_7) or \
            float_eq(real64_4, real64_7) or \
            float_eq(real64_5, real64_7) or \
            float_eq(real64_6, real64_7):
        real64_7 = random.uniform(-1e307, 1e307)
    real64_8 = random.uniform(-1e307, 1e307)
    while float_eq(real64_0, real64_8) or \
            float_eq(real64_1, real64_8) or \
            float_eq(real64_2, real64_8) or \
            float_eq(real64_3, real64_8) or \
            float_eq(real64_4, real64_8) or \
            float_eq(real64_5, real64_8) or \
            float_eq(real64_6, real64_8) or \
            float_eq(real64_7, real64_8):
        real64_8 = random.uniform(-1e307, 1e307)

    real64a_0 = MI_Real64A((real64_0, real64_1, real64_2))
    real64a_1 = MI_Real64A((real64_3, real64_4, real64_5))
    real64a_2 = MI_Real64A((real64_6, real64_7, real64_8))

    real64a_in = real64a_0
    inst45 = MI_Instance()

    inst45.SetValue('real64a', real64a_in)
    real64a_out = inst45.GetValue('real64a')

    if real64a_out is not None:
        if not float_array_eq(real64a_in, real64a_0) or \
                not float_array_eq(inst45.GetValue('real64a'), real64a_0) or \
                not float_array_eq(real64a_out, real64a_0):
            BookEndPrint('----- real64a SetValue/GetValue failed')
            rval = False
        else:
            real64a_in = real64a_1
            if not float_array_eq(real64a_in, real64a_1) or \
                    not float_array_eq(inst45.GetValue('real64a'), real64a_0) or \
                    not float_array_eq(real64a_out, real64a_0):
                BookEndPrint(
                    '----- real64a SetValue/GetValue stored a reference')
                rval = False
            else:
                real64a_out = real64a_2
                if not float_array_eq(real64a_in, real64a_1) or \
                        not float_array_eq(inst45.GetValue('real64a'), real64a_0) or \
                        not float_array_eq(real64a_out, real64a_2):
                    BookEndPrint(
                        '----- real64a SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- real64a SetValue/GetValue returned None')
        rval = False

    inst46 = MI_Instance()
    inst46.SetValue('real64a', inst45.GetValue('real64a'))
    if float_array_eq(inst46.GetValue('real64a'), inst45.GetValue('real64a')):
        inst46.SetValue('real64a', real64a_1)
        if not float_array_eq(inst46.GetValue('real64a'), real64a_1):
            BookEndPrint("----- real64a  SetValue failed")
            rval = False
        if float_array_eq(inst45.GetValue('real64a'), real64a_1):
            BookEndPrint('----- real64a SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- real64a SetValue/GetValue failed')
        rval = False

    # char16a
    char16_3 = random.randint(0, 0xFFFF)
    while char16_0 == char16_3 or \
            char16_1 == char16_3 or \
            char16_2 == char16_3:
        char16_3 = random.randint(0, 0xFFFF)
    char16_4 = random.randint(0, 0xFFFF)
    while char16_0 == char16_4 or \
            char16_1 == char16_4 or \
            char16_2 == char16_4 or \
            char16_3 == char16_4:
        char16_4 = random.randint(0, 0xFFFF)
    char16_5 = random.randint(0, 0xFFFF)
    while char16_0 == char16_5 or \
            char16_1 == char16_5 or \
            char16_2 == char16_5 or \
            char16_3 == char16_5 or \
            char16_4 == char16_5:
        char16_5 = random.randint(0, 0xFFFF)
    char16_6 = random.randint(0, 0xFFFF)
    while char16_0 == char16_6 or \
            char16_1 == char16_6 or \
            char16_2 == char16_6 or \
            char16_3 == char16_6 or \
            char16_4 == char16_6 or \
            char16_5 == char16_6:
        char16_6 = random.randint(0, 0xFFFF)
    char16_7 = random.randint(0, 0xFFFF)
    while char16_0 == char16_7 or \
            char16_1 == char16_7 or \
            char16_2 == char16_7 or \
            char16_3 == char16_7 or \
            char16_4 == char16_7 or \
            char16_5 == char16_7 or \
            char16_6 == char16_7:
        char16_7 = random.randint(0, 0xFFFF)
    char16_8 = random.randint(0, 0xFFFF)
    while char16_0 == char16_8 or \
            char16_1 == char16_8 or \
            char16_2 == char16_8 or \
            char16_3 == char16_8 or \
            char16_4 == char16_8 or \
            char16_5 == char16_8 or \
            char16_6 == char16_8 or \
            char16_7 == char16_8:
        char16_8 = random.randint(0, 0xFFFF)

    char16a_0 = MI_Char16A((char16_0, char16_1, char16_2))
    char16a_1 = MI_Char16A((char16_3, char16_4, char16_5))
    char16a_2 = MI_Char16A((char16_6, char16_7, char16_8))

    char16a_in = char16a_0
    inst47 = MI_Instance()

    inst47.SetValue('char16a', char16a_in)
    char16a_out = inst47.GetValue('char16a')

    if char16a_out is not None:
        if not array_eq(char16a_in, char16a_0) or \
                not array_eq(inst47.GetValue('char16a'), char16a_0) or \
                not array_eq(char16a_out, char16a_0):
            BookEndPrint('----- char16a SetValue/GetValue failed')
            rval = False
        else:
            char16a_in = char16a_1
            if not array_eq(char16a_in, char16a_1) or \
                    not array_eq(inst47.GetValue('char16a'), char16a_0) or \
                    not array_eq(char16a_out, char16a_0):
                BookEndPrint(
                    '----- char16a SetValue/GetValue stored a reference')
                rval = False
            else:
                char16a_out = char16a_2
                if not array_eq(char16a_in, char16a_1) or \
                        not array_eq(inst47.GetValue('char16a'), char16a_0) or \
                        not array_eq(char16a_out, char16a_2):
                    BookEndPrint(
                        '----- char16a SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- char16a SetValue/GetValue returned None')
        rval = False

    inst48 = MI_Instance()
    inst48.SetValue('char16a', inst47.GetValue('char16a'))
    if array_eq(inst48.GetValue('char16a'), inst47.GetValue('char16a')):
        inst48.SetValue('char16a', char16a_1)
        if not array_eq(inst48.GetValue('char16a'), char16a_1):
            BookEndPrint("----- char16a  SetValue failed")
            rval = False
        if array_eq(inst47.GetValue('char16a'), char16a_1):
            BookEndPrint('----- char16a SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- char16a SetValue/GetValue failed')
        rval = False

    # datetimea
    datetime_3 = MI_Interval(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49))
    datetime_4 = MI_Timestamp(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49),
        random.randint(50, 59),
        random.randint(60, 69),
        random.randint(70, 79))
    datetime_5 = MI_Interval(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49))
    datetime_6 = MI_Timestamp(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49),
        random.randint(50, 59),
        random.randint(60, 69),
        random.randint(70, 79))
    datetime_7 = MI_Interval(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49))
    datetime_8 = MI_Timestamp(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49),
        random.randint(50, 59),
        random.randint(60, 69),
        random.randint(70, 79))

    datetimea_0 = MI_DatetimeA((datetime_0, datetime_1, datetime_2))
    datetimea_1 = MI_DatetimeA((datetime_3, datetime_4, datetime_5))
    datetimea_2 = MI_DatetimeA((datetime_6, datetime_7, datetime_8))

    datetimea_in = datetimea_0
    inst49 = MI_Instance()

    inst49.SetValue('datetimea', datetimea_in)
    datetimea_out = inst49.GetValue('datetimea')

    if datetimea_out is not None:
        if not datetime_array_eq(datetimea_in, datetimea_0) or \
                not datetime_array_eq(inst49.GetValue('datetimea'), datetimea_0) or \
                not datetime_array_eq(datetimea_out, datetimea_0):
            BookEndPrint('----- datetimea SetValue/GetValue failed')
            rval = False
        else:
            datetimea_in = datetimea_1
            if not datetime_array_eq(datetimea_in, datetimea_1) or \
                    not datetime_array_eq(inst49.GetValue('datetimea'), datetimea_0) or \
                    not datetime_array_eq(datetimea_out, datetimea_0):
                BookEndPrint(
                    '----- datetimea SetValue/GetValue stored a reference')
                rval = False
            else:
                datetimea_out = datetimea_2
                if not datetime_array_eq(datetimea_in, datetimea_1) or \
                        not datetime_array_eq(inst49.GetValue('datetimea'), datetimea_0) or \
                        not datetime_array_eq(datetimea_out, datetimea_2):
                    BookEndPrint(
                        '----- datetimea SetValue/GetValue stored a reference')
                    rval = False
                else:
                    datetimea_out = inst49.GetValue('datetimea')
                    datetimea_out.setValueAt(0, datetime_2)
                    if datetime_array_eq(datetimea_out, inst49.GetValue('datetimea')) or \
                       datetime_array_eq(datetimea_out, datetimea_2):
                        BookEndPrint(
                            '----- datetimea SetValue/GetValue stored a reference')
                        rval = False
    else:
        BookEndPrint('----- datetimea SetValue/GetValue returned None')
        rval = False

    inst50 = MI_Instance()
    inst50.SetValue('datetimea', inst49.GetValue('datetimea'))
    if datetime_array_eq(inst50.GetValue('datetimea'), inst49.GetValue('datetimea')):
        inst50.SetValue('datetimea', datetimea_1)
        if not datetime_array_eq(inst50.GetValue('datetimea'), datetimea_1):
            BookEndPrint("----- datetimea  SetValue failed")
            rval = False
        if datetime_array_eq(inst49.GetValue('datetimea'), datetimea_1):
            BookEndPrint(
                '----- datetimea SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- datettimea SetValue/GetValue failed')
        rval = False

    # stringa
    string_0 = random.randint(0, len(string_vals) - 1)
    temp = string_vals[0]
    string_vals[0] = string_vals[string_0]
    string_vals[string_0] = temp
    string_1 = random.randint(1, len(string_vals) - 1)
    temp = string_vals[1]
    string_vals[1] = string_vals[string_1]
    string_vals[string_1] = temp
    string_2 = random.randint(2, len(string_vals) - 1)
    temp = string_vals[2]
    string_vals[2] = string_vals[string_2]
    string_vals[string_2] = temp
    string_3 = random.randint(3, len(string_vals) - 1)
    temp = string_vals[3]
    string_vals[3] = string_vals[string_3]
    string_vals[string_3] = temp
    string_4 = random.randint(4, len(string_vals) - 1)
    temp = string_vals[4]
    string_vals[4] = string_vals[string_4]
    string_vals[string_4] = temp
    string_5 = random.randint(5, len(string_vals) - 1)
    temp = string_vals[5]
    string_vals[5] = string_vals[string_5]
    string_vals[string_5] = temp
    string_6 = random.randint(6, len(string_vals) - 1)
    temp = string_vals[6]
    string_vals[6] = string_vals[string_6]
    string_vals[string_6] = temp
    string_7 = random.randint(7, len(string_vals) - 1)
    temp = string_vals[7]
    string_vals[7] = string_vals[string_7]
    string_vals[string_7] = temp
    string_8 = random.randint(8, len(string_vals) - 1)
    temp = string_vals[8]
    string_vals[8] = string_vals[string_8]
    string_vals[string_8] = temp

    stringa_0 = MI_StringA([string_vals[string_0], string_vals[string_1],
                            string_vals[string_2]])
    stringa_1 = MI_StringA([string_vals[string_3], string_vals[string_4],
                            string_vals[string_5]])
    stringa_2 = MI_StringA([string_vals[string_6], string_vals[string_7],
                            string_vals[string_8]])

    stringa_in = stringa_0
    inst51 = MI_Instance()

    inst51.SetValue('stringa', stringa_in)
    stringa_out = inst51.GetValue('stringa')

    if stringa_out is not None:
        if not array_eq(stringa_in, stringa_0) or \
                not array_eq(inst51.GetValue('stringa'), stringa_0) or \
                not array_eq(stringa_out, stringa_0):
            BookEndPrint('----- stringa SetValue/GetValue failed')
            rval = False
        else:
            stringa_in = stringa_1
            if not array_eq(stringa_in, stringa_1) or \
                    not array_eq(inst51.GetValue('stringa'), stringa_0) or \
                    not array_eq(stringa_out, stringa_0):
                BookEndPrint(
                    '----- stringa SetValue/GetValue stored a reference')
                rval = False
            else:
                stringa_out = stringa_2
                if not array_eq(stringa_in, stringa_1) or \
                        not array_eq(inst51.GetValue('stringa'), stringa_0) or \
                        not array_eq(stringa_out, stringa_2):
                    BookEndPrint(
                        '----- stringa SetValue/GetValue stored a reference')
                    rval = False
    else:
        BookEndPrint('----- stringa SetValue/GetValue returned None')
        rval = False

    inst52 = MI_Instance()
    inst52.SetValue('stringa', inst51.GetValue('stringa'))
    if array_eq(inst52.GetValue('stringa'), inst51.GetValue('stringa')):
        inst52.SetValue('stringa', stringa_1)
        if not array_eq(inst52.GetValue('stringa'), stringa_1):
            BookEndPrint("----- stringa  SetValue failed")
            rval = False
        if array_eq(inst51.GetValue('stringa'), stringa_1):
            BookEndPrint('----- stringa SetValue/GetValue stored a reference')
            rval = False
    else:
        BookEndPrint('----- stringa SetValue/GetValue failed')
        rval = False

    # MI_Uint8A
    # uint8a
    # inst27
    # inst28

    return rval
