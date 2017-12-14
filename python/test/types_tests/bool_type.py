from omi import *

try:
    from utils import *
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from utils import *


def bool_test():
    be = BookEnd('bool_test')

    rval = True

    # init (empty)
    v0 = MI_Boolean()
    if v0.getType() != MI_BOOLEAN:
        BookEndPrint('----- getType failed')
        rval = False
    if v0.value is not None:
        BookEndPrint('----- empty init failed')
        rval = False

    # init to None
    v1 = MI_Boolean(None)
    if v1.value is not None:
        BookEndPrint('----- NULL init failed')
        rval = False

    # init to literal value
    v2 = MI_Boolean(True)
    if v2.value is not True:
        BookEndPrint('----- value init failed')
        rval = False

    # init to MI_Boolean (None)
    t3 = MI_Boolean()
    if COPY_CTOR:
        v3 = MI_Boolean(t3)
        if v3.value != t3.value:
            BookEndPrint('----- MI_Boolean (None) init failed')
            rval = False
    else:
        try:
            v3 = MI_Boolean(t3)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to MI_Boolean
    t4 = MI_Boolean(False)
    if COPY_CTOR:
        v4 = MI_Boolean(t4)
        if v4.value != t4.value:
            BookEndPrint('----- MI_Boolean init failed')
            rval = False
    else:
        try:
            v4 = MI_Boolean(t4)
        except ValueError:
            pass
        else:
            BookEndPrint('----- init using copy ctor failed')
            rval = False

    # init to a different MI type (None) **error**
    t5 = MI_Uint8()
    try:
        v5 = MI_Boolean(t5)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type (None) failed')
        rval = False

    # init to a different MI type **error**
    t6 = MI_Uint8(6)
    try:
        v6 = MI_Boolean(t6)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to a different MI type failed')
        rval = False

    # init to invalid literal value **error**
    try:
        v7 = MI_Boolean('seven')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to invalid literal failed')
        rval = False

    # assign None to None
    v8 = MI_Boolean()
    v8.value = None
    if v8.value is not None:
        BookEndPrint('----- None assignment to None failed')
        rval = False

    # assign a literal value to None
    v9 = MI_Boolean()
    v9.value = True
    if v9.value is not True:
        BookEndPrint('----- literal value assignment to None failed')
        rval = False

    # assign MI_Boolean (None) to None
    v10 = MI_Boolean()
    t10 = MI_Boolean()
    if ASSIGN_OP:
        v10.value = t10
        if v10.value != t10.value:
            BookEndPrint('----- MI_Boolean (None) assignment to None failed')
            rval = False
    else:
        try:
            v10.value = t10
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Boolean to None
    v11 = MI_Boolean()
    t11 = MI_Boolean(False)
    if ASSIGN_OP:
        v11.value = t11
        if v11.value != t11.value:
            BookEndPrint('----- MI_Boolean assignment to None failed')
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
    v12 = MI_Boolean()
    t12 = MI_Uint8()
    try:
        v12.value = t12
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type (None) failed')
        rval = False

    # assign a different MI type to None **error**
    v13 = MI_Boolean()
    t13 = MI_Uint8(13)
    try:
        v13.value = t13
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal to None **error**
    v14 = MI_Boolean()
    try:
        v14.value = 'fourteen'
    except:
        pass
    else:
        BookEndPrint('----- assign invalid literal failed')
        rval = False

    # assign None
    v15 = MI_Boolean(True)
    v15.value = None
    if v15.value is not None:
        BookEndPrint('----- None assignment failed')
        rval = False

    # assign a literal value
    v16 = MI_Boolean(False)
    v16.value = True
    if v16.value is not True:
        BookEndPrint('----- literal value assignment failed')
        rval = False

    # assign MI_Boolean (None)
    v17 = MI_Boolean(True)
    t17 = MI_Boolean()
    if ASSIGN_OP:
        v17.value = t17
        if v17.value != t17.value:
            BookEndPrint('----- MI_Boolean (None) assignment failed')
            rval = False
    else:
        try:
            v17.value = t17
        except ValueError:
            pass
        else:
            BookEndPrint('----- assignment operator failed')
            rval = False

    # assign MI_Boolean
    v18 = MI_Boolean(False)
    t18 = MI_Boolean(True)
    if ASSIGN_OP:
        v18.value = t18
        if v18.value != t18.value:
            BookEndPrint('----- MI_Boolean assignment failed')
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
    v19 = MI_Boolean(False)
    t19 = MI_Uint8()
    try:
        v19.value = t19
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign a different MI type **error**
    v20 = MI_Boolean(True)
    t20 = MI_Uint8(20)
    try:
        v20.value = t20
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign a different MI type failed')
        rval = False

    # assign invalid literal **error**
    v21 = MI_Boolean(False)
    try:
        v21.value = 'twenty-one'
    except ValueError:
        pass
    else:
        BookEndPrint('----- assign invalid literal failed')
        rval = False

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_Boolean)')

    return rval
