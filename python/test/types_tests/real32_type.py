from omi import *

try:
    from utils import *
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from utils import *


def real32_test():
    be = BookEnd('real32_test')

    rval = True

    # init (empty)
    v0 = MI_Real32()
    if v0.getType() != MI_REAL32:
        BookEndPrint('----- getType failed')
        rval = False
    if v0.value is not None:
        BookEndPrint('----- empty init failed')
        rval = False

    # init to None
    v1 = MI_Real32(None)
    if v1.value is not None:
        BookEndPrint('----- NULL init failed')
        rval = False

    # init to value
    r2 = ctypes.c_float(random.uniform(-1e37, 1e37))
    v2 = MI_Real32(r2.value)
    if not float_eq(v2.value, r2.value):
        BookEndPrint('----- value init failed')
        rval = False

    # init to MI_Real32 (None)
    t3 = MI_Real32()
    if COPY_CTOR:
        v3 = MI_Real32(t3)
        if v3.value != t3.value:
            BookEndPrint('----- MI_Real32 (None) init failed')
            rval = False
    else:
        try:
            v3 = MI_Real32(t3)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to MI_Real32
    r4 = ctypes.c_float(random.uniform(-1e37, 1e37))
    t4 = MI_Real32(r4.value)
    if COPY_CTOR:
        v4 = MI_Real32(t4)
        if not float_eq(t4.value, v4.value):
            BookEndPrint('----- MI_Real32 init failed')
            rval = False
    else:
        try:
            v4 = MI_Real32(t4)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to a different MI type (None) **error**
    t5 = MI_Boolean()
    try:
        v5 = MI_Real32(t5)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type (None) failed')
        rval = False

    # init to a different MI type **error**
    t6 = MI_Boolean(True)
    try:
        v6 = MI_Real32(t6)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type failed')
        rval = False

    # init to invalid literal value **error**
    try:
        v7 = MI_Real32('seven')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to invalid literal failed')
        rval = False

    # init to under-range value **error**
    try:
        v8 = MI_Real32(-1e39)
    except:
        pass
    else:
        BookEndPrint('----- init to under-range value failed')
        rval = False

    # init to over-range value **error**
    try:
        v9 = MI_Real32(1e39)
    except:
        pass
    else:
        BookEndPrint('----- init to over-range value failed')
        rval = False

    # assign None to None
    v10 = MI_Real32()
    v10.value = None
    if v10.value is not None:
        BookEndPrint('----- None assignment to None failed')
        rval = False

    # assign a value to None
    r11 = ctypes.c_float(random.uniform(-1e37, 1e37))
    v11 = MI_Real32()
    v11.value = r11.value
    if not float_eq(v11.value, r11.value):
        BookEndPrint('----- literal value assignment to None failed')
        rval = False

    # assign MI_Real32 (None) to None
    v12 = MI_Real32()
    t12 = MI_Real32()
    if ASSIGN_OP:
        v12.value = t12
        if v12.value != t12.value:
            BookEndPrint('----- MI_Real32 (None) assignment to None failed')
            rval = False
    else:
        try:
            v12.value = t12
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Real32 to None
    r13 = ctypes.c_float(random.uniform(-1e37, 1e37))
    v13 = MI_Real32()
    t13 = MI_Real32(r13.value)
    if ASSIGN_OP:
        v13.value = t13
        if not float_eq(v13.value, t13.value):
            BookEndPrint('----- MI_Real32 assignment to None failed')
            rval = False
    else:
        try:
            v13.value = t13
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign a different MI type (None) to None **error**
    v14 = MI_Real32()
    t14 = MI_Boolean()
    try:
        v14.value = t14
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type to None **error**
    v15 = MI_Real32()
    t15 = MI_Boolean(False)
    try:
        v15.value = t15
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal to None **error**
    v16 = MI_Real32()
    try:
        v16.value = 'sixteen'
    except:
        pass
    else:
        BookEndPrint('----- MI_Boolean assign invalid literal failed')
        rval = False

    # assign under-range value to None **error**
    v17 = MI_Real32()
    try:
        v17.value = -1e39
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value to None failed')
        rval = False

    # assign over-range value to None **error**
    v18 = MI_Real32()
    try:
        v18.value = 1e39
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value to None failed')
        rval = False

    # assign None
    r19 = ctypes.c_float(random.uniform(-1e37, 1e37))
    v19 = MI_Real32(r19.value)
    v19.value = None
    if v19.value is not None:
        BookEndPrint('----- None assignment failed')
        rval = False

    # assign a literal value
    r20a = ctypes.c_float(random.uniform(-1e37, 1e37))
    r20b = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(r20a.value, r20b.value):
        r20b = ctypes.c_float(random.uniform(-1e37, 1e37))
    v20 = MI_Real32(r20a.value)
    v20.value = r20b.value
    if not float_eq(v20.value, r20b.value):
        BookEndPrint('----- value assignment failed')
        rval = False

    # assign MI_Real32 (None)
    r21 = ctypes.c_float(random.uniform(-1e37, 1e37))
    v21 = MI_Real32(r21.value)
    t21 = MI_Real32()
    if ASSIGN_OP:
        v21.value = t21
        if v21.value != t21.value:
            BookEndPrint('----- MI_Real32 (None) assignment failed')
            rval = False
    else:
        try:
            v21.value = t21
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Real32
    r22a = ctypes.c_float(random.uniform(-1e37, 1e37))
    r22b = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(r22a.value, r22b.value):
        r22b = ctypes.c_float(random.uniform(-1e37, 1e37))
    v22 = MI_Real32(r22a.value)
    t22 = MI_Real32(r22b.value)
    if ASSIGN_OP:
        v22.value = t22
        if not float_eq(v22.value, t22.value):
            BookEndPrint('----- MI_Real32 assignment failed')
            rval = False
    else:
        try:
            v22.value = t22
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign a different MI type (None) **error**
    r23 = ctypes.c_float(random.uniform(-1e37, 1e37))
    v23 = MI_Real32(r23.value)
    t23 = MI_Boolean()
    try:
        v23.value = t23
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type **error**
    r24 = ctypes.c_float(random.uniform(-1e37, 1e37))
    v24 = MI_Real32(r24.value)
    t24 = MI_Boolean(False)
    try:
        v24.value = t24
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal **error**
    r25 = ctypes.c_float(random.uniform(-1e37, 1e37))
    v25 = MI_Real32(r25.value)
    try:
        v25.value = 'twenty-five'
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign invalid literal failed')
        rval = False

    # assign under-range value **error**
    r26 = ctypes.c_float(random.uniform(-1e37, 1e37))
    v26 = MI_Real32(r26.value)
    try:
        v26.value = -1e39
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value failed')
        rval = False

    # assign over-range value **error**
    r27 = ctypes.c_float(random.uniform(-1e37, 1e37))
    v27 = MI_Real32(r27.value)
    try:
        v27.value = 1e39
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value failed')
        rval = False

    # init to zero
    try:
        r28 = MI_Real32(0)
        if 0.0 != r28.value:
            BookEndPrint('----- init to zero value failed')
            rval = False
    except:
        BookEndPrint('----- init to zero failed - exception')
        rval = False

    try:
        r29 = MI_Real32(0.0)
        if 0.0 != r29.value:
            BookEndPrint('----- init to zero value failed')
            rval = False
    except:
        BookEndPrint('----- init to zero failed - exception')
        rval = False

    # set to zero
    r30 = MI_Real32()
    try:
        r30.value = 0
    except:
        BookEndPrint('----- set to zero failed - exception')
        rval = False
    else:
        if 0.0 != r30.value:
            BookEndPrint('----- set to zero value failed')
            rval = False

    # set to zero
    r31 = MI_Real32()
    try:
        r31.value = 0.0
    except:
        BookEndPrint('----- set to zero failed - exception')
        rval = False
    else:
        if 0.0 != r31.value:
            BookEndPrint('----- set to zero value failed')
            rval = False

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_Real32)')

    return rval
