from omi import *

try:
    from utils import *
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from utils import *


def uint8_test():
    be = BookEnd('uint8_test')

    rval = True

    # init (empty)
    v0 = MI_Uint8()
    if v0.getType() != MI_UINT8:
        BookEndPrint('----- getType failed')
        rval = False
    if v0.value is not None:
        BookEndPrint('----- empty init failed')
        rval = False

    # init to None
    v1 = MI_Uint8(None)
    if v1.value is not None:
        BookEndPrint('----- NULL init failed')
        rval = False

    # init to value
    r2 = random.randint(0, 0xFF)
    v2 = MI_Uint8(r2)
    if v2.value != r2:
        BookEndPrint('----- value init failed')
        rval = False

    # init to MI_Uint8 (None)
    t3 = MI_Uint8()
    if COPY_CTOR:
        v3 = MI_Uint8(t3)
        if v3.value != t3.value:
            BookEndPrint('----- MI_Uint8 (None) init failed')
            rval = False
    else:
        try:
            v3 = MI_Uint8(t3)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to MI_Uint8
    t4 = MI_Uint8(random.randint(0, 0xFF))
    if COPY_CTOR:
        v4 = MI_Uint8(t4)
        if v4.value != t4.value:
            BookEndPrint('----- MI_Uint8 init failed')
            rval = False
    else:
        try:
            v4 = MI_Uint8(t4)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to a different MI type (None) **error**
    t5 = MI_Boolean()
    try:
        v5 = MI_Uint8(t5)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type (None) failed')
        rval = False

    # init to a different MI type **error**
    t6 = MI_Boolean(True)
    try:
        v6 = MI_Uint8(t6)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type failed')
        rval = False

    # init to invalid literal value **error**
    try:
        v7 = MI_Uint8('seven')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to invalid literal failed')
        rval = False

    # init to under-range value **error**
    try:
        v8 = MI_Uint8(-1)
    except:
        pass
    else:
        BookEndPrint('----- init to under-range value failed')
        rval = False

    # init to over-range value **error**
    try:
        v9 = MI_Uint8(0x100)
    except:
        pass
    else:
        BookEndPrint('----- init to over-range value failed')
        rval = False

    # assign None to None
    v10 = MI_Uint8()
    v10.value = None
    if v10.value is not None:
        BookEndPrint('----- None assignment to None failed')
        rval = False

    # assign a  value to None
    v11 = MI_Uint8()
    r11 = random.randint(0, 0xFF)
    v11.value = r11
    if v11.value != r11:
        BookEndPrint('----- literal value assignment to None failed')
        rval = False

    # assign MI_Uint8 (None) to None
    v12 = MI_Uint8()
    t12 = MI_Uint8()
    if ASSIGN_OP:
        v12.value = t12
        if v12.value != t12.value:
            BookEndPrint('----- MI_Uint8 (None) assignment to None failed')
            rval = False
    else:
        try:
            v12.value = t12
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Uint8 to None
    v13 = MI_Uint8()
    t13 = MI_Uint8(random.randint(0, 0xFF))
    if ASSIGN_OP:
        v13.value = t13
        if v13.value != t13.value:
            BookEndPrint('----- MI_Uint8 assignment to None failed')
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
    v14 = MI_Uint8()
    t14 = MI_Boolean()
    try:
        v14.value = t14
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type to None **error**
    v15 = MI_Uint8()
    t15 = MI_Boolean(False)
    try:
        v15.value = t15
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal to None **error**
    v16 = MI_Uint8()
    try:
        v16.value = 'sixteen'
    except:
        pass
    else:
        BookEndPrint('----- MI_Boolean assign invalid literal failed')
        rval = False

    # assign under-range value to None **error**
    v17 = MI_Uint8()
    try:
        v17.value = -1
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value to None failed')
        rval = False

    # assign over-range value to None **error**
    v18 = MI_Uint8()
    try:
        v18.value = 0x100
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value to None failed')
        rval = False

    # assign None
    v19 = MI_Uint8(random.randint(0, 0xFF))
    v19.value = None
    if v19.value is not None:
        BookEndPrint('----- None assignment failed')
        rval = False

    # assign a literal value
    r20a = random.randint(0, 0xFF)
    r20b = random.randint(0, 0xFF)
    while r20a == r20b:
        r20b = random.randint(0, 0xFF)
    v20 = MI_Uint8(r20a)
    v20.value = r20b
    if v20.value != r20b:
        BookEndPrint('----- value assignment failed')
        rval = False

    # assign MI_Uint8 (None)
    v21 = MI_Uint8(random.randint(0, 0xFF))
    t21 = MI_Uint8()
    if ASSIGN_OP:
        v21.value = t21
        if v21.value != t21.value:
            BookEndPrint('----- MI_Uint8 (None) assignment failed')
            rval = False
    else:
        try:
            v21.value = t21
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Uint8
    r22a = random.randint(0, 0xFF)
    r22b = random.randint(0, 0xFF)
    while r22a == r22b:
        r22b = random.randint(0, 0xFF)
    v22 = MI_Uint8(r22a)
    t22 = MI_Uint8(r22b)
    if ASSIGN_OP:
        v22.value = t22
        if v22.value != t22.value:
            BookEndPrint('----- MI_Uint8 assignment failed')
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
    v23 = MI_Uint8(random.randint(0, 0xFF))
    t23 = MI_Boolean()
    try:
        v23.value = t23
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type **error**
    v24 = MI_Uint8(random.randint(0, 0xFF))
    t24 = MI_Boolean(False)
    try:
        v24.value = t24
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal **error**
    v25 = MI_Uint8(random.randint(0, 0xFF))
    try:
        v25.value = 'twenty-five'
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign invalid literal failed')
        rval = False

    # assign under-range value **error**
    v26 = MI_Uint8(random.randint(0, 0xFF))
    try:
        v26.value = -1
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value failed')
        rval = False

    # assign over-range value **error**
    v27 = MI_Uint8(random.randint(0, 0xFF))
    try:
        v27.value = 0x100
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value failed')
        rval = False

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_Uint8)')

    return rval


def sint8_test():
    be = BookEnd('sint8_test')

    rval = True

    # init (empty)
    v0 = MI_Sint8()
    if v0.getType() != MI_SINT8:
        BookEndPrint('----- getType failed')
        rval = False
    if v0.value is not None:
        BookEndPrint('----- empty init failed')
        rval = False

    # init to None
    v1 = MI_Sint8(None)
    if v1.value is not None:
        BookEndPrint('----- NULL init failed')
        rval = False

    # init to value
    r2 = random.randint(-0x80, 0x7F)
    v2 = MI_Sint8(r2)
    if v2.value != r2:
        BookEndPrint('----- value init failed')
        rval = False

    # init to MI_Sint8 (None)
    t3 = MI_Sint8()
    if COPY_CTOR:
        v3 = MI_Sint8(t3)
        if v3.value != t3.value:
            BookEndPrint('----- MI_Sint8 (None) init failed')
            rval = False
    else:
        try:
            v3 = MI_Sint8(t3)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to MI_Sint8
    t4 = MI_Sint8(random.randint(-0x80, 0x7F))
    if COPY_CTOR:
        v4 = MI_Sint8(t4)
        if v4.value != t4.value:
            BookEndPrint('----- MI_Sint8 init failed')
            rval = False
    else:
        try:
            v4 = MI_Sint8(t4)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to a different MI type (None) **error**
    t5 = MI_Boolean()
    try:
        v5 = MI_Sint8(t5)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type (None) failed')
        rval = False

    # init to a different MI type **error**
    t6 = MI_Boolean(True)
    try:
        v6 = MI_Sint8(t6)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type failed')
        rval = False

    # init to invalid literal value **error**
    try:
        v7 = MI_Sint8('seven')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to invalid literal failed')
        rval = False

    # init to under-range value **error**
    try:
        v8 = MI_Sint8(-0x81)
    except:
        pass
    else:
        BookEndPrint('----- init to under-range value failed')
        rval = False

    # init to over-range value **error**
    try:
        v9 = MI_Sint8(0x80)
    except:
        pass
    else:
        BookEndPrint('----- init to over-range value failed')
        rval = False

    # assign None to None
    v10 = MI_Sint8()
    v10.value = None
    if v10.value is not None:
        BookEndPrint('----- None assignment to None failed')
        rval = False

    # assign a  value to None
    v11 = MI_Sint8()
    r11 = random.randint(-0x80, 0x7F)
    v11.value = r11
    if v11.value != r11:
        BookEndPrint('----- literal value assignment to None failed')
        rval = False

    # assign MI_Sint8 (None) to None
    v12 = MI_Sint8()
    t12 = MI_Sint8()
    if ASSIGN_OP:
        v12.value = t12
        if v12.value != t12.value:
            BookEndPrint('----- MI_Sint8 (None) assignment to None failed')
            rval = False
    else:
        try:
            v12.value = t12
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Sint8 to None
    v13 = MI_Sint8()
    t13 = MI_Sint8(random.randint(-0x80, 0x7F))
    if ASSIGN_OP:
        v13.value = t13
        if v13.value != t13.value:
            BookEndPrint('----- MI_Sint8 assignment to None failed')
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
    v14 = MI_Sint8()
    t14 = MI_Boolean()
    try:
        v14.value = t14
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type to None **error**
    v15 = MI_Sint8()
    t15 = MI_Boolean(False)
    try:
        v15.value = t15
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal to None **error**
    v16 = MI_Sint8()
    try:
        v16.value = 'sixteen'
    except:
        pass
    else:
        BookEndPrint('----- MI_Boolean assign invalid literal failed')
        rval = False

    # assign under-range value to None **error**
    v17 = MI_Sint8()
    try:
        v17.value = -0x81
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value to None failed')
        rval = False

    # assign over-range value to None **error**
    v18 = MI_Sint8()
    try:
        v18.value = 0x80
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value to None failed')
        rval = False

    # assign None
    v19 = MI_Sint8(random.randint(-0x80, 0x7F))
    v19.value = None
    if v19.value is not None:
        BookEndPrint('----- None assignment failed')
        rval = False

    # assign a literal value
    r20a = random.randint(-0x80, 0x7F)
    r20b = random.randint(-0x80, 0x7F)
    while r20a == r20b:
        r20b = random.randint(-0x80, 0x7F)
    v20 = MI_Sint8(r20a)
    v20.value = r20b
    if v20.value != r20b:
        BookEndPrint('----- value assignment failed')
        rval = False

    # assign MI_Sint8 (None)
    v21 = MI_Sint8(random.randint(-0x80, 0x7F))
    t21 = MI_Sint8()
    if ASSIGN_OP:
        v21.value = t21
        if v21.value != t21.value:
            BookEndPrint('----- MI_Sint8 (None) assignment failed')
            rval = False
    else:
        try:
            v21.value = t21
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Sint8
    r22a = random.randint(-0x80, 0x7F)
    r22b = random.randint(-0x80, 0x7F)
    while r22a == r22b:
        r22b = random.randint(-0x80, 0x7F)
    v22 = MI_Sint8(r22a)
    t22 = MI_Sint8(r22b)
    if ASSIGN_OP:
        v22.value = t22
        if v22.value != t22.value:
            BookEndPrint('----- MI_Sint8 assignment failed')
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
    v23 = MI_Sint8(random.randint(-0x80, 0x7F))
    t23 = MI_Boolean()
    try:
        v23.value = t23
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type **error**
    v24 = MI_Sint8(random.randint(-0x80, 0x7F))
    t24 = MI_Boolean(False)
    try:
        v24.value = t24
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal **error**
    v25 = MI_Sint8(random.randint(-0x80, 0x7F))
    try:
        v25.value = 'twenty-five'
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign invalid literal failed')
        rval = False

    # assign under-range value **error**
    v26 = MI_Sint8(random.randint(-0x80, 0x7F))
    try:
        v26.value = -0x81
    except:
        pass
    else:
        BookEndPrint('----- assign under-range value failed')
        rval = False

    # assign over-range value **error**
    v27 = MI_Sint8(random.randint(-0x80, 0x7F))
    try:
        v27.value = 0x80
    except:
        pass
    else:
        BookEndPrint('----- assign over-range value failed')
        rval = False

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_Sint8)')

    return rval
