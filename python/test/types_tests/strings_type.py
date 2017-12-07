from omi import *

try:
    from utils import *
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from utils import *


def string_test():
    be = BookEnd('string_test')
    vals = [
        'apple', 'banana', 'peach', 'pear', 'orange',
        'watermelon', 'lemon', 'grapefruit', 'kiwi', 'plum',
        'chicken', 'dog', 'cat', 'goat', 'sheep',
        'rabbit', 'cow', 'horse', 'llama', 'pig'
    ]

    rval = True

    # init (empty)
    v0 = MI_String()
    if v0.getType() != MI_STRING:
        BookEndPrint('----- getType failed')
        rval = False
    if v0.value is not None:
        BookEndPrint('----- empty init failed')
        rval = False

    # init to None
    v1 = MI_String(None)
    if v1.value is not None:
        BookEndPrint('----- NULL init failed')
        rval = False

    # init to value
    r2 = vals[random.randint(0, len(vals) - 1)]
    v2 = MI_String(r2)
    if v2.value != r2:
        BookEndPrint('----- value init failed')
        rval = False

    # init to MI_String (None)
    t3 = MI_String()
    if COPY_CTOR:
        v3 = MI_String(t3)
        if v3.value != t3.value:
            BookEndPrint('----- MI_String (None) init failed')
            rval = False
    else:
        try:
            v3 = MI_String(t3)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to MI_String
    t4 = MI_String(vals[random.randint(0, len(vals) - 1)])
    if COPY_CTOR:
        v4 = MI_String(t4)
        if v4.value != t4.value:
            BookEndPrint('----- MI_String init failed')
            rval = False
    else:
        try:
            v4 = MI_String(t4)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to a different MI type (None) **error**
    t5 = MI_Boolean()
    try:
        v5 = MI_String(t5)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type (None) failed')
        rval = False

    # init to a different MI type **error**
    t6 = MI_Boolean(True)
    try:
        v6 = MI_String(t6)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type failed')
        rval = False

    # init to invalid literal value **error**
    try:
        v7 = MI_String(True)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to invalid literal failed')
        rval = False

    # assign None to None
    v8 = MI_String()
    v8.value = None
    if v8.value is not None:
        BookEndPrint('----- None assignment to None failed')
        rval = False

    # assign a  value to None
    v9 = MI_String()
    r9 = vals[random.randint(0, len(vals) - 1)]
    v9.value = r9
    if v9.value != r9:
        BookEndPrint('----- literal value assignment to None failed')
        rval = False

    # assign MI_String (None) to None
    v10 = MI_String()
    t10 = MI_String()
    if ASSIGN_OP:
        v10.value = t10
        if v10.value != t10.value:
            BookEndPrint('----- MI_String (None) assignment to None failed')
            rval = False
    else:
        try:
            v10.value = t10
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_String to None
    v11 = MI_String()
    t11 = MI_String(vals[random.randint(0, len(vals) - 1)])
    if ASSIGN_OP:
        v11.value = t11
        if v11.value != t11.value:
            BookEndPrint('----- MI_String assignment to None failed')
            rval = False
    else:
        try:
            v11.value = t11
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign a different MI type (None) to None **error**
    v12 = MI_String()
    t12 = MI_Boolean()
    try:
        v12.value = t12
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type to None **error**
    v13 = MI_String()
    t13 = MI_Boolean(False)
    try:
        v13.value = t13
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal to None **error**
    v14 = MI_String()
    try:
        v14.value = False
    except:
        pass
    else:
        BookEndPrint('----- MI_Boolean assign invalid literal failed')
        rval = False

    # assign None
    v15 = MI_String(vals[random.randint(0, len(vals) - 1)])
    v15.value = None
    if v15.value is not None:
        BookEndPrint('----- None assignment failed')
        rval = False

    # assign a literal value
    i16 = random.randint(0, len(vals) - 2)
    r16a = vals[i16]
    r16b = vals[i16 + 1]
    v16 = MI_String(r16a)
    v16.value = r16b
    if v16.value != r16b:
        BookEndPrint('----- value assignment failed')
        rval = False

    # assign MI_String (None)
    v17 = MI_String(vals[random.randint(0, len(vals) - 1)])
    t17 = MI_String()
    if ASSIGN_OP:
        v17.value = t17
        if v17.value != t17.value:
            BookEndPrint('----- MI_String (None) assignment failed')
            rval = False
    else:
        try:
            v17.value = t17
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_String
    i18 = random.randint(0, len(vals) - 2)
    r18a = vals[i18]
    r18b = vals[i18 + 1]
    #r22a = random.randint (0, 0xFFFF)
    #r22b = random.randint (0, 0xFFFF)
    # while r22a == r22b:
    #    r22b = random.randint (0, 0xFFFF)
    v18 = MI_String(r18a)
    t18 = MI_String(r18b)
    if ASSIGN_OP:
        v18.value = t18
        if v18.value != t18.value:
            BookEndPrint('----- MI_String assignment failed')
            rval = False
    else:
        try:
            v18.value = t18
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign a different MI type (None) **error**
    v19 = MI_String(vals[random.randint(0, len(vals) - 1)])
    t19 = MI_Boolean()
    try:
        v19.value = t19
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type **error**
    v20 = MI_String(vals[random.randint(0, len(vals) - 1)])
    t20 = MI_Boolean(False)
    try:
        v20.value = t20
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal **error**
    v21 = MI_String(vals[random.randint(0, len(vals) - 1)])
    try:
        v21.value = False
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign invalid literal failed')
        rval = False

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_String)')

    return rval
