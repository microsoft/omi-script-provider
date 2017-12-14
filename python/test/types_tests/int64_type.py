from omi import *

try:
    from utils import *
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from utils import *


def uint64_test():
    be = BookEnd('uint64_test')

    rval = True

    # init (empty)
    v0 = MI_Uint64()
    if v0.getType() != MI_UINT64:
        BookEndPrint('----- getType failed')
        rval = False
    if v0.value is not None:
        BookEndPrint('----- empty init failed')
        rval = False

    # init to None
    v1 = MI_Uint64(None)
    if v1.value is not None:
        BookEndPrint('----- NULL init failed')
        rval = False

    # init to value
    r2 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    v2 = MI_Uint64(r2)
    if v2.value != r2:
        BookEndPrint('----- value init failed')
        rval = False

    # init to MI_Uint64 (None)
    t3 = MI_Uint64()
    if COPY_CTOR:
        v3 = MI_Uint64(t3)
        if v3.value != t3.value:
            BookEndPrint('----- MI_Uint64 (None) init failed')
            rval = False
    else:
        try:
            v3 = MI_Uint64(t3)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to MI_Uint64
    t4 = MI_Uint64(random.randint(0, 0xFFFFFFFFFFFFFFFF))
    if COPY_CTOR:
        v4 = MI_Uint64(t4)
        if v4.value != t4.value:
            BookEndPrint('----- MI_Uint64 init failed')
            rval = False
    else:
        try:
            v4 = MI_Uint64(t4)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to a different MI type (None) **error**
    t5 = MI_Boolean()
    try:
        v5 = MI_Uint64(t5)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type (None) failed')
        rval = False

    # init to a different MI type **error**
    t6 = MI_Boolean(True)
    try:
        v6 = MI_Uint64(t6)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type failed')
        rval = False

    # init to invalid literal value **error**
    try:
        v7 = MI_Uint64('seven')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to invalid literal failed')
        rval = False

    # init to under-range value **error**
    try:
        v8 = MI_Uint64(-1)
    except:
        pass
    else:
        BookEndPrint('----- init to under-range value failed')
        rval = False

    # init to over-range value **error**
    try:
        v9 = MI_Uint64(0x10000000000000000)
    except:
        pass
    else:
        BookEndPrint('----- init to over-range value failed')
        rval = False

    # assign None to None
    v10 = MI_Uint64()
    v10.value = None
    if v10.value is not None:
        BookEndPrint('----- None assignment to None failed')
        rval = False

    # assign a  value to None
    v11 = MI_Uint64()
    r11 = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    v11.value = r11
    if v11.value != r11:
        BookEndPrint('----- literal value assignment to None failed')
        rval = False

    # assign MI_Uint64 (None) to None
    v12 = MI_Uint64()
    t12 = MI_Uint64()
    if ASSIGN_OP:
        v12.value = t12
        if v12.value != t12.value:
            BookEndPrint('----- MI_Uint64 (None) assignment to None failed')
            rval = False
    else:
        try:
            v12.value = t12
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Uint64 to None
    v13 = MI_Uint64()
    t13 = MI_Uint64(random.randint(0, 0xFFFFFFFFFFFFFFFF))
    if ASSIGN_OP:
        v13.value = t13
        if v13.value != t13.value:
            BookEndPrint('----- MI_Uint64 assignment to None failed')
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
    v14 = MI_Uint64()
    t14 = MI_Boolean()
    try:
        v14.value = t14
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type to None **error**
    v15 = MI_Uint64()
    t15 = MI_Boolean(False)
    try:
        v15.value = t15
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal to None **error**
    v16 = MI_Uint64()
    try:
        v16.value = 'sixteen'
    except:
        pass
    else:
        BookEndPrint('----- MI_Boolean assign invalid literal failed')
        rval = False

    # assign under-range value to None **error**
    v17 = MI_Uint64()
    try:
        v17.value = -1
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value to None failed')
        rval = False

    # assign over-range value to None **error**
    v18 = MI_Uint64()
    try:
        v18.value = 0x10000000000000000
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value to None failed')
        rval = False

    # assign None
    v19 = MI_Uint64(random.randint(0, 0xFFFFFFFFFFFFFFFF))
    v19.value = None
    if v19.value is not None:
        BookEndPrint('----- None assignment failed')
        rval = False

    # assign a literal value
    r20a = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    r20b = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    while r20a == r20b:
        r20b = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    v20 = MI_Uint64(r20a)
    v20.value = r20b
    if v20.value != r20b:
        BookEndPrint('----- value assignment failed')
        rval = False

    # assign MI_Uint64 (None)
    v21 = MI_Uint64(random.randint(0, 0xFFFFFFFFFFFFFFFF))
    t21 = MI_Uint64()
    if ASSIGN_OP:
        v21.value = t21
        if v21.value != t21.value:
            BookEndPrint('----- MI_Uint64 (None) assignment failed')
            rval = False
    else:
        try:
            v21.value = t21
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Uint64
    r22a = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    r22b = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    while r22a == r22b:
        r22b = random.randint(0, 0xFFFFFFFFFFFFFFFF)
    v22 = MI_Uint64(r22a)
    t22 = MI_Uint64(r22b)
    if ASSIGN_OP:
        v22.value = t22
        if v22.value != t22.value:
            BookEndPrint('----- MI_Uint64 assignment failed')
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
    v23 = MI_Uint64(random.randint(0, 0xFFFFFFFFFFFFFFFF))
    t23 = MI_Boolean()
    try:
        v23.value = t23
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type **error**
    v24 = MI_Uint64(random.randint(0, 0xFFFFFFFFFFFFFFFF))
    t24 = MI_Boolean(False)
    try:
        v24.value = t24
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal **error**
    v25 = MI_Uint64(random.randint(0, 0xFFFFFFFFFFFFFFFF))
    try:
        v25.value = 'twenty-five'
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign invalid literal failed')
        rval = False

    # assign under-range value **error**
    v26 = MI_Uint64(random.randint(0, 0xFFFFFFFFFFFFFFFF))
    try:
        v26.value = -1
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value failed')
        rval = False

    # assign over-range value **error**
    v27 = MI_Uint64(random.randint(0, 0xFFFFFFFFFFFFFFFF))
    try:
        v27.value = 0x10000000000000000
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value failed')
        rval = False

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_Uint64)')

    return rval


def sint64_test():
    be = BookEnd('sint64_test')

    rval = True

    # init (empty)
    v0 = MI_Sint64()
    if v0.getType() != MI_SINT64:
        BookEndPrint('----- getType failed')
        rval = False
    if v0.value is not None:
        BookEndPrint('----- empty init failed')
        rval = False

    # init to None
    v1 = MI_Sint64(None)
    if v1.value is not None:
        BookEndPrint('----- NULL init failed')
        rval = False

    # init to value
    r2 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    v2 = MI_Sint64(r2)
    if v2.value != r2:
        BookEndPrint('----- value init failed')
        rval = False

    # init to MI_Sint64 (None)
    t3 = MI_Sint64()
    if COPY_CTOR:
        v3 = MI_Sint64(t3)
        if v3.value != t3.value:
            BookEndPrint('----- MI_Sint64 (None) init failed')
            rval = False
    else:
        try:
            v3 = MI_Sint64(t3)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to MI_Sint64
    t4 = MI_Sint64(random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF))
    if COPY_CTOR:
        v4 = MI_Sint64(t4)
        if v4.value != t4.value:
            BookEndPrint('----- MI_Sint64 init failed')
            rval = False
    else:
        try:
            v4 = MI_Sint64(t4)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to a different MI type (None) **error**
    t5 = MI_Boolean()
    try:
        v5 = MI_Sint64(t5)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type (None) failed')
        rval = False

    # init to a different MI type **error**
    t6 = MI_Boolean(True)
    try:
        v6 = MI_Sint64(t6)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type failed')
        rval = False

    # init to invalid literal value **error**
    try:
        v7 = MI_Sint64('seven')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to invalid literal failed')
        rval = False

    # init to under-range value **error**
    try:
        v8 = MI_Sint64(-0x8000000000000001)
    except:
        pass
    else:
        BookEndPrint('----- init to under-range value failed')
        rval = False

    # init to over-range value **error**
    try:
        v9 = MI_Sint64(0x8000000000000000)
    except:
        pass
    else:
        BookEndPrint('----- init to over-range value failed')
        rval = False

    # assign None to None
    v10 = MI_Sint64()
    v10.value = None
    if v10.value is not None:
        BookEndPrint('----- None assignment to None failed')
        rval = False

    # assign a  value to None
    v11 = MI_Sint64()
    r11 = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    v11.value = r11
    if v11.value != r11:
        BookEndPrint('----- literal value assignment to None failed')
        rval = False

    # assign MI_Sint64 (None) to None
    v12 = MI_Sint64()
    t12 = MI_Sint64()
    if ASSIGN_OP:
        v12.value = t12
        if v12.value != t12.value:
            BookEndPrint('----- MI_Sint64 (None) assignment to None failed')
            rval = False
    else:
        try:
            v12.value = t12
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Sint64 to None
    v13 = MI_Sint64()
    t13 = MI_Sint64(random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF))
    if ASSIGN_OP:
        v13.value = t13
        if v13.value != t13.value:
            BookEndPrint('----- MI_Sint64 assignment to None failed')
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
    v14 = MI_Sint64()
    t14 = MI_Boolean()
    try:
        v14.value = t14
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type to None **error**
    v15 = MI_Sint64()
    t15 = MI_Boolean(False)
    try:
        v15.value = t15
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal to None **error**
    v16 = MI_Sint64()
    try:
        v16.value = 'sixteen'
    except:
        pass
    else:
        BookEndPrint('----- MI_Boolean assign invalid literal failed')
        rval = False

    # assign under-range value to None **error**
    v17 = MI_Sint64()
    try:
        v17.value = -0x8000000000000001
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value to None failed')
        rval = False

    # assign over-range value to None **error**
    v18 = MI_Sint64()
    try:
        v18.value = 0x8000000000000000
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value to None failed')
        rval = False

    # assign None
    v19 = MI_Sint64(random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF))
    v19.value = None
    if v19.value is not None:
        BookEndPrint('----- None assignment failed')
        rval = False

    # assign a literal value
    r20a = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    r20b = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    while r20a == r20b:
        r20b = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    v20 = MI_Sint64(r20a)
    v20.value = r20b
    if v20.value != r20b:
        BookEndPrint('----- value assignment failed')
        rval = False

    # assign MI_Sint64 (None)
    v21 = MI_Sint64(random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF))
    t21 = MI_Sint64()
    if ASSIGN_OP:
        v21.value = t21
        if v21.value != t21.value:
            BookEndPrint('----- MI_Sint64 (None) assignment failed')
            rval = False
    else:
        try:
            v21.value = t21
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Sint64
    r22a = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    r22b = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    while r22a == r22b:
        r22b = random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF)
    v22 = MI_Sint64(r22a)
    t22 = MI_Sint64(r22b)
    if ASSIGN_OP:
        v22.value = t22
        if v22.value != t22.value:
            BookEndPrint('----- MI_Sint64 assignment failed')
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
    v23 = MI_Sint64(random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF))
    t23 = MI_Boolean()
    try:
        v23.value = t23
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type **error**
    v24 = MI_Sint64(random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF))
    t24 = MI_Boolean(False)
    try:
        v24.value = t24
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal **error**
    v25 = MI_Sint64(random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF))
    try:
        v25.value = 'twenty-five'
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign invalid literal failed')
        rval = False

    # assign under-range value **error**
    v26 = MI_Sint64(random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF))
    try:
        v26.value = -0x8000000000000001
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value failed')
        rval = False

    # assign over-range value **error**
    v27 = MI_Sint64(random.randint(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF))
    try:
        v27.value = 0x8000000000000000
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value failed')
        rval = False

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_Sint64)')

    return rval
