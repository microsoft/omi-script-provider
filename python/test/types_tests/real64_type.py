from omi import *

try:
    from utils import *
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from utils import *


def real64_test():
    be = BookEnd('real64_test')

    rval = True

    # init (empty)
    v0 = MI_Real64()
    if v0.getType() != MI_REAL64:
        BookEndPrint('----- getType failed')
        rval = False
    if v0.value is not None:
        BookEndPrint('----- empty init failed')
        rval = False

    # init to None
    v1 = MI_Real64(None)
    if v1.value is not None:
        BookEndPrint('----- NULL init failed')
        rval = False

    # init to value
    r2 = random.uniform(-1e307, 1e307)
    v2 = MI_Real64(r2)
    if not float_eq(v2.value, r2):
        BookEndPrint('----- value init failed')
        rval = False

    # init to MI_Real64 (None)
    t3 = MI_Real64()
    if COPY_CTOR:
        v3 = MI_Real64(t3)
        if v3.value != t3.value:
            BookEndPrint('----- MI_Real64 (None) init failed')
            rval = False
    else:
        try:
            v3 = MI_Real64(t3)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to MI_Real64
    r4 = random.uniform(-1e307, 1e307)
    t4 = MI_Real64(r4)
    if COPY_CTOR:
        v4 = MI_Real64(t4)
        if not float_eq(t4.value, v4.value):
            BookEndPrint('----- MI_Real64 init failed')
            rval = False
    else:
        try:
            v4 = MI_Real64(t4)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to a different MI type (None) **error**
    t5 = MI_Boolean()
    try:
        v5 = MI_Real64(t5)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type (None) failed')
        rval = False

    # init to a different MI type **error**
    t6 = MI_Boolean(True)
    try:
        v6 = MI_Real64(t6)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type failed')
        rval = False

    # init to invalid literal value **error**
    try:
        v7 = MI_Real64('seven')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to invalid literal failed')
        rval = False

    # init to under-range value **error**
    try:
        v8 = MI_Real64(-1e309)
    except:
        pass
    else:
        BookEndPrint('----- init to under-range value failed')
        rval = False

    # init to over-range value **error**
    try:
        v9 = MI_Real64(1e309)
    except:
        pass
    else:
        BookEndPrint('----- init to over-range value failed')
        rval = False

    # assign None to None
    v10 = MI_Real64()
    v10.value = None
    if v10.value is not None:
        BookEndPrint('----- None assignment to None failed')
        rval = False

    # assign a value to None
    r11 = random.uniform(-1e307, 1e307)
    v11 = MI_Real64()
    v11.value = r11
    if not float_eq(v11.value, r11):
        BookEndPrint('----- literal value assignment to None failed')
        rval = False

    # assign MI_Real64 (None) to None
    v12 = MI_Real64()
    t12 = MI_Real64()
    if ASSIGN_OP:
        v12.value = t12
        if v12.value != t12.value:
            BookEndPrint('----- MI_Real64 (None) assignment to None failed')
            rval = False
    else:
        try:
            v12.value = t12
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Real64 to None
    r13 = random.uniform(-1e307, 1e307)
    v13 = MI_Real64()
    t13 = MI_Real64(r13)
    if ASSIGN_OP:
        v13.value = t13
        if not float_eq(v13.value, t13.value):
            BookEndPrint('----- MI_Real64 assignment to None failed')
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
    v14 = MI_Real64()
    t14 = MI_Boolean()
    try:
        v14.value = t14
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type to None **error**
    v15 = MI_Real64()
    t15 = MI_Boolean(False)
    try:
        v15.value = t15
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal to None **error**
    v16 = MI_Real64()
    try:
        v16.value = 'sixteen'
    except:
        pass
    else:
        BookEndPrint('----- MI_Boolean assign invalid literal failed')
        rval = False

    # assign under-range value to None **error**
    v17 = MI_Real64()
    try:
        v17.value = -1e309
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value to None failed')
        rval = False

    # assign over-range value to None **error**
    v18 = MI_Real64()
    try:
        v18.value = 1e309
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value to None failed')
        rval = False

    # assign None
    r19 = random.uniform(-1e307, 1e307)
    v19 = MI_Real64(r19)
    v19.value = None
    if v19.value is not None:
        BookEndPrint('----- None assignment failed')
        rval = False

    # assign a literal value
    r20a = random.uniform(-1e307, 1e307)
    r20b = random.uniform(-1e307, 1e307)
    while float_eq(r20a, r20b):
        r20b = random.uniform(-1e307, 1e307)
    v20 = MI_Real64(r20a)
    v20.value = r20b
    if not float_eq(v20.value, r20b):
        BookEndPrint('----- value assignment failed')
        rval = False

    # assign MI_Real64 (None)
    r21 = random.uniform(-1e307, 1e307)
    v21 = MI_Real64(r21)
    t21 = MI_Real64()
    if ASSIGN_OP:
        v21.value = t21
        if v21.value != t21.value:
            BookEndPrint('----- MI_Real64 (None) assignment failed')
            rval = False
    else:
        try:
            v21.value = t21
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Real64
    r22a = random.uniform(-1e307, 1e307)
    r22b = random.uniform(-1e307, 1e307)
    while float_eq(r22a, r22b):
        r22b = random.uniform(-1e307, 1e307)
    v22 = MI_Real64(r22a)
    t22 = MI_Real64(r22b)
    if ASSIGN_OP:
        v22.value = t22
        if not float_eq(v22.value, t22.value):
            BookEndPrint('----- MI_Real64 assignment failed')
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
    r23 = random.uniform(-1e307, 1e307)
    v23 = MI_Real64(r23)
    t23 = MI_Boolean()
    try:
        v23.value = t23
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type **error**
    r24 = random.uniform(-1e307, 1e307)
    v24 = MI_Real64(r24)
    t24 = MI_Boolean(False)
    try:
        v24.value = t24
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal **error**
    r25 = random.uniform(-1e307, 1e307)
    v25 = MI_Real64(r25)
    try:
        v25.value = 'twenty-five'
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign invalid literal failed')
        rval = False

    # assign under-range value **error**
    r26 = random.uniform(-1e307, 1e307)
    v26 = MI_Real64(r26)
    try:
        v26.value = -1e309
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value failed')
        rval = False

    # assign over-range value **error**
    r27 = random.uniform(-1e307, 1e307)
    v27 = MI_Real64(r27)
    try:
        v27.value = 1e309
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value failed')
        rval = False

    # init to zero
    try:
        r28 = MI_Real64(0)
        if 0.0 != r28.value:
            BookEndPrint('----- init to zero value failed')
            rval = False
    except:
        BookEndPrint('----- init to zero failed - exception')
        rval = False

    # init to zero
    try:
        r29 = MI_Real64(0.0)
        if 0.0 != r29.value:
            BookEndPrint('----- init to zero value failed')
            rval = False
    except:
        BookEndPrint('----- init to zero failed - exception')
        rval = False

    # set to zero
    r30 = MI_Real64()
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
    r31 = MI_Real64()
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
        BookEndPrint('!!!!!  Tests have failed! (MI_Real64)')

    return rval
