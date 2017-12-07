from omi import *

try:
    from utils import *
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from utils import *


def real32a_test():
    be = BookEnd('real32a_test')

    val0 = ctypes.c_float(random.uniform(-1e37, 1e37))
    val1 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(val0.value, val1.value):
        val1 = ctypes.c_float(random.uniform(-1e37, 1e37))
    val2 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(val0.value, val2.value) or \
            float_eq(val1.value, val2.value):
        val2 = ctypes.c_float(random.uniform(-1e37, 1e37))
    val3 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(val0.value, val3.value) or \
            float_eq(val1.value, val3.value) or \
            float_eq(val2.value, val3.value):
        val3 = ctypes.c_float(random.uniform(-1e37, 1e37))
    val4 = ctypes.c_float(random.uniform(-1e37, 1e37))
    while float_eq(val0.value, val4.value) or \
            float_eq(val1.value, val4.value) or \
            float_eq(val2.value, val4.value) or \
            float_eq(val3.value, val4.value):
        val4 = ctypes.c_float(random.uniform(-1e37, 1e37))

    #BookEndPrint ('val0: {0}'.format (val0.value))
    #BookEndPrint ('val1: {0}'.format (val1.value))
    #BookEndPrint ('val2: {0}'.format (val2.value))
    #BookEndPrint ('val3: {0}'.format (val3.value))
    #BookEndPrint ('val4: {0}'.format (val4.value))

    rval = True

    # init (empty)
    v0 = MI_Real32A()
    if MI_REAL32A != v0.getType():
        BookEndPrint('----- getType failed')
        rval = False
    if v0.count() != 0:
        BookEndPrint('----- empty init failed')
        rval = False

    # test getValueAt (out of range) **error**
    try:
        v0.getValueAt(0)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False
    try:
        v0.getValueAt(-1)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False
    try:
        v0.getValueAt(1)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False

    # test getValueAt (invalid type) **error**
    try:
        v0.getValueAt('zero')
    except ValueError:
        pass
    else:
        BookEndPrint('----- getValueAt (empty - invalid literal) failed')
        rval = False

    # PyList init
    v1 = MI_Real32A([val0.value, val1.value, val2.value])
    if v1.count() != 3:
        BookEndPrint('----- PyList init failed')
        rval = False
    if not float_eq(v1.getValueAt(0), val0.value) or \
            not float_eq(v1.getValueAt(1), val1.value) or \
            not float_eq(v1.getValueAt(2), val2.value) or \
            not float_eq(v1.getValueAt(-3), val0.value) or \
            not float_eq(v1.getValueAt(-2), val1.value) or \
            not float_eq(v1.getValueAt(-1), val2.value):
        BookEndPrint('----- PyList init or getValueAt failed')
        rval = False

    # test getValueAt (out of range) **error**
    try:
        v1.getValueAt(-4)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False
    try:
        v1.getValueAt(3)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False

    # test getValueAt (invalid type) **error**
    try:
        v1.getValueAt('one')
    except ValueError:
        pass
    else:
        BookEndPrint('----- getValueAt (invalid type) failed')
        rval = False

    # PyTuple init
    v2 = MI_Real32A((val0.value, val1.value, val2.value))
    if v2.count() != 3 or \
            not float_eq(v2.getValueAt(0), val0.value) or \
            not float_eq(v2.getValueAt(1), val1.value) or \
            not float_eq(v2.getValueAt(2), val2.value):
        BookEndPrint('----- PyTuple init failed')
        rval = False

    # init from None **error**
    # try:
    #    v3 = MI_Real32A (None)
    # except ValueError:
    #    pass
    # else:
    #    BookEndPrint ('----- None init failed')
    #    rval = False
    v3 = MI_Real32A(None)
    if v3.count() != 0:
        BookEndPrint('----- None init failed')
        rval = False

    # init from invalid literal value **error**
    try:
        v4 = MI_Real32A('four')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to invalid literal failed')
        rval = False

    # PyList init (None) **error**
    try:
        v5 = MI_Real32A([val0.value, None, val2.value])
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyList init (None value) failed')
        rval = False

    # PyList init (underflow value) **error**
    try:
        v6 = MI_Real32A([val0.value, -1e39, val2.value])
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyList init (underflow value) failed')
        rval = False

    # PyList init (overflow value) **error**
    try:
        v7 = MI_Real32A([val0.value, 1e39, val2.value])
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyList init (overflow value) failed')
        rval = False

    # PyList init (invalid type) **error**
    try:
        v8 = MI_Real32A([val0.value, 'eight', val2.value])
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyList init (invalid type) failed')
        rval = False

    # PyTuple init (None) **error**
    try:
        v9 = MI_Real32A((val0.value, None, val2.value))
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyTuple init (None value) failed')
        rval = False

    # PyTuple init (underflow value) **error**
    try:
        v10 = MI_Real32A((val0.value, -1e39, val2.value))
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyTuple init (underflow value) failed')
        rval = False

    # PyTuple init (overflow value) **error**
    try:
        v11 = MI_Real32A((val0.value, 1e39, val2.value))
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyTuple init (overflow value) failed')
        rval = False

    # PyTuple init (invalid type) **error**
    try:
        v12 = MI_Real32A((val0.value, 'twelve', val2.value))
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyTuple init (invalid type) failed')
        rval = False

    # setValueAt
    v13 = MI_Real32A((val0.value, val1.value, val2.value))
    v13.setValueAt(0, val4.value)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val4.value) or \
            not float_eq(v13.getValueAt(1), val1.value) or \
            not float_eq(v13.getValueAt(2), val2.value):
        BookEndPrint('----- setValueAt failed')
        rval = False
    v13.setValueAt(1, val0.value)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val4.value) or \
            not float_eq(v13.getValueAt(1), val0.value) or \
            not float_eq(v13.getValueAt(2), val2.value):
        BookEndPrint('----- setValueAt failed')
        rval = False
    v13.setValueAt(2, val1.value)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val4.value) or \
            not float_eq(v13.getValueAt(1), val0.value) or \
            not float_eq(v13.getValueAt(2), val1.value):
        BookEndPrint('----- setValueAt failed')
        rval = False
    v13.setValueAt(-1, val2.value)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val4.value) or \
            not float_eq(v13.getValueAt(1), val0.value) or \
            not float_eq(v13.getValueAt(2), val2.value):
        BookEndPrint('----- setValueAt failed')
        rval = False
    v13.setValueAt(-2, val1.value)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val4.value) or \
            not float_eq(v13.getValueAt(1), val1.value) or \
            not float_eq(v13.getValueAt(2), val2.value):
        BookEndPrint('----- setValueAt failed')
        rval = False
    v13.setValueAt(-3, val0.value)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val0.value) or \
            not float_eq(v13.getValueAt(1), val1.value) or \
            not float_eq(v13.getValueAt(2), val2.value):
        BookEndPrint('----- setValueAt failed')
        rval = False

    # setValueAt (index out of range) **error**
    try:
        v13.setValueAt(-4, val3.value)
    except IndexError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0.value) or \
                not float_eq(v13.getValueAt(1), val1.value) or \
                not float_eq(v13.getValueAt(2), val2.value):
            BookEndPrint('----- setValueAt (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (index out of range) failed')
        rval = False
    try:
        v13.setValueAt(3, val3.value)
    except IndexError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0.value) or \
                not float_eq(v13.getValueAt(1), val1.value) or \
                not float_eq(v13.getValueAt(2), val2.value):
            BookEndPrint('----- setValueAt (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (index out of range) failed')
        rval = False

    # setValueAt (index invalid type) **error**
    try:
        v13.setValueAt('one', val3.value)
    except ValueError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0.value) or \
                not float_eq(v13.getValueAt(1), val1.value) or \
                not float_eq(v13.getValueAt(2), val2.value):
            BookEndPrint('----- setValueAt (index invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (index invalid type) failed')
        rval = False

    # setValueAt (value underflow) **error**
    try:
        v13.setValueAt(1, -1e39)
    except ValueError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0.value) or \
                not float_eq(v13.getValueAt(1), val1.value) or \
                not float_eq(v13.getValueAt(2), val2.value):
            BookEndPrint('----- setValueAt (value underflow) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (value underflow) failed')
        rval = False

    # setValueAt (value overflow)
    try:
        v13.setValueAt(1, 1e39)
    except ValueError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0.value) or \
                not float_eq(v13.getValueAt(1), val1.value) or \
                not float_eq(v13.getValueAt(2), val2.value):
            BookEndPrint('----- setValueAt (value overflow) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (value overflow) failed')
        rval = False

    # setValueAt (value invalid type) **error**
    try:
        v13.setValueAt(1, 'thirteen')
    except ValueError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0.value) or \
                not float_eq(v13.getValueAt(1), val1.value) or \
                not float_eq(v13.getValueAt(2), val2.value):
            BookEndPrint('----- setValueAt (value invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (value invalid type) failed')
        rval = False

    # append
    v14 = MI_Real32A()
    v14.append(val0.value)
    if v14.count() != 1 or \
            not float_eq(v14.getValueAt(0), val0.value):
        BookEndPrint('----- append failed')
        rval = False
    v14.append(val1.value)
    if v14.count() != 2 or \
            not float_eq(v14.getValueAt(0), val0.value) or \
            not float_eq(v14.getValueAt(1), val1.value):
        BookEndPrint('----- append failed')
        rval = False
    v14.append(val2.value)
    if v14.count() != 3 or \
            not float_eq(v14.getValueAt(0), val0.value) or \
            not float_eq(v14.getValueAt(1), val1.value) or \
            not float_eq(v14.getValueAt(2), val2.value):
        BookEndPrint('----- append failed')
        rval = False

    # append (value underflow) **error**
    try:
        v14.append(-1e39)
    except ValueError:
        if v14.count() != 3 or \
                not float_eq(v14.getValueAt(0), val0.value) or \
                not float_eq(v14.getValueAt(1), val1.value) or \
                not float_eq(v14.getValueAt(2), val2.value):
            BookEndPrint('----- append (value underflow) failed')
            rval = False
    else:
        BookEndPrint('----- append (value underflow) failed')
        rval = False

    # append (value overflow)
    try:
        v14.append(1e39)
    except ValueError:
        if v14.count() != 3 or \
                not float_eq(v14.getValueAt(0), val0.value) or \
                not float_eq(v14.getValueAt(1), val1.value) or \
                not float_eq(v14.getValueAt(2), val2.value):
            BookEndPrint('----- append (value overflow) failed')
            rval = False
    else:
        BookEndPrint('----- append (value overflow) failed')
        rval = False

    # append (value invalid type) **error**
    try:
        v14.append('fourteen')
    except ValueError:
        if v14.count() != 3 or \
                not float_eq(v14.getValueAt(0), val0.value) or \
                not float_eq(v14.getValueAt(1), val1.value) or \
                not float_eq(v14.getValueAt(2), val2.value):
            BookEndPrint('----- append (value invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- append (value invalid type) failed')
        rval = False

    # insert
    v15 = MI_Real32A()
    v15.insert(0, val1.value)
    if v15.count() != 1 or \
            not float_eq(v15.getValueAt(0), val1.value):
        BookEndPrint('----- insert failed')
        rval = False
    v15.insert(0, val0.value)
    if v15.count() != 2 or \
            not float_eq(v15.getValueAt(0), val0.value) or \
            not float_eq(v15.getValueAt(1), val1.value):
        BookEndPrint('----- insert failed')
        rval = False
    v15.insert(2, val3.value)
    if v15.count() != 3 or \
            not float_eq(v15.getValueAt(0), val0.value) or \
            not float_eq(v15.getValueAt(1), val1.value) or \
            not float_eq(v15.getValueAt(2), val3.value):
        BookEndPrint('----- insert failed')
        rval = False
    v15.insert(2, val2.value)
    if v15.count() != 4 or \
            not float_eq(v15.getValueAt(0), val0.value) or \
            not float_eq(v15.getValueAt(1), val1.value) or \
            not float_eq(v15.getValueAt(2), val2.value) or \
            not float_eq(v15.getValueAt(3), val3.value):
        BookEndPrint('----- insert failed')
        rval = False

    # insert using negative indices
    v16 = MI_Real32A([val2.value])
    v16.insert(-1, val0.value)
    if v16.count() != 2 or \
            not float_eq(v16.getValueAt(0), val0.value) or \
            not float_eq(v16.getValueAt(1), val2.value):
        BookEndPrint('----- insert (negative index) failed')
        rval = False
    v16.insert(-1, val1.value)
    if v16.count() != 3 or \
            not float_eq(v16.getValueAt(0), val0.value) or \
            not float_eq(v16.getValueAt(1), val1.value) or \
            not float_eq(v16.getValueAt(2), val2.value):
        BookEndPrint('----- insert (negative index) failed')
        rval = False

    # insert (index out of bounds) **error**
    try:
        v16.insert(4, val3.value)
    except IndexError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0.value) or \
                not float_eq(v16.getValueAt(1), val1.value) or \
                not float_eq(v16.getValueAt(2), val2.value):
            BookEndPrint('----- insert (index out of bounds) failed')
            rval = False
    else:
        BookEndPrint('----- insert (index out of bounds) failed')
        rval = False
    try:
        v16.insert(-4, val3.value)
    except IndexError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0.value) or \
                not float_eq(v16.getValueAt(1), val1.value) or \
                not float_eq(v16.getValueAt(2), val2.value):
            BookEndPrint('----- insert (index out of bounds) failed')
            rval = False
    else:
        BookEndPrint('----- insert (index out of bounds) failed')
        rval = False

    # insert (index invalid type) **error**
    try:
        v16.insert('sixteen', val3.value)
    except ValueError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0.value) or \
                not float_eq(v16.getValueAt(1), val1.value) or \
                not float_eq(v16.getValueAt(2), val2.value):
            BookEndPrint('----- insert (index invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- insert (index invalid type) failed')
        rval = False

    # insert (value out of range) **error**
    try:
        v16.insert(1, -1e39)
    except ValueError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0.value) or \
                not float_eq(v16.getValueAt(1), val1.value) or \
                not float_eq(v16.getValueAt(2), val2.value):
            BookEndPrint('----- insert (value out of range) failed')
            rval = False
    else:
        BookEndPrint('----- insert (value out of range) failed')
        rval = False
    try:
        v16.insert(1, 1e39)
    except ValueError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0.value) or \
                not float_eq(v16.getValueAt(1), val1.value) or \
                not float_eq(v16.getValueAt(2), val2.value):
            BookEndPrint('----- insert (value out of range) failed')
            rval = False
    else:
        BookEndPrint('----- insert (value out of range) failed')
        rval = False

    # value type invalid
    try:
        v16.insert(1, 'sixteen')
    except ValueError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0.value) or \
                not float_eq(v16.getValueAt(1), val1.value) or \
                not float_eq(v16.getValueAt(2), val2.value):
            BookEndPrint('----- insert (value invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- insert (value invalid type) failed')
        rval = False

    # pop
    v17 = MI_Real32A((val0.value, val1.value, val2.value, val3.value))
    t17 = v17.pop()
    if not float_eq(t17, val3.value) or \
            v17.count() != 3 or \
            not float_eq(v17.getValueAt(0), val0.value) or \
            not float_eq(v17.getValueAt(1), val1.value) or \
            not float_eq(v17.getValueAt(2), val2.value):
        BookEndPrint('----- pop failed')
        rval = False
    t17 = v17.pop(1)
    if not float_eq(t17, val1.value) or \
            v17.count() != 2 or \
            not float_eq(v17.getValueAt(0), val0.value) or \
            not float_eq(v17.getValueAt(1), val2.value):
        BookEndPrint('----- pop failed')
        rval = False
    v17.insert(1, val1.value)
    t17 = v17.pop(0)
    if not float_eq(t17, val0.value) or \
            v17.count() != 2 or \
            not float_eq(v17.getValueAt(0), val1.value) or \
            not float_eq(v17.getValueAt(1), val2.value):
        BookEndPrint('----- pop failed')
        rval = False
    v17.insert(0, val0.value)
    t17 = v17.pop(2)
    if not float_eq(t17, val2.value) or \
            v17.count() != 2 or \
            not float_eq(v17.getValueAt(0), val0.value) or \
            not float_eq(v17.getValueAt(1), val1.value):
        BookEndPrint('----- pop failed')
        rval = False

    # pop (negative indices)
    v18 = MI_Real32A((val0.value, val1.value, val2.value))
    t18 = v18.pop(-2)
    if not float_eq(t18, val1.value) or \
            v18.count() != 2 or \
            not float_eq(v18.getValueAt(0), val0.value) or \
            not float_eq(v18.getValueAt(1), val2.value):
        BookEndPrint('----- pop failed')
        rval = False
    v18.insert(1, val1.value)
    t18 = v18.pop(-3)
    if not float_eq(t18, val0.value) or \
            v18.count() != 2 or \
            not float_eq(v18.getValueAt(0), val1.value) or \
            not float_eq(v18.getValueAt(1), val2.value):
        BookEndPrint('----- pop failed')
        rval = False
    v18.insert(0, val0.value)
    t18 = v18.pop(-1)
    if not float_eq(t18, val2.value) or \
            v18.count() != 2 or \
            not float_eq(v18.getValueAt(0), val0.value) or \
            not float_eq(v18.getValueAt(1), val1.value):
        BookEndPrint('----- pop failed')
        rval = False

    # pop (empty array) **error**
    v19 = MI_Real32A()
    try:
        v19.pop()
    except IndexError:
        pass
    else:
        BookEndPrint('----- pop (empty array) failed')
        rval = False

    v20 = MI_Real32A((val0.value, val1.value, val2.value))
    try:
        v20.pop(3)
    except IndexError:
        if v20.count() != 3 or \
                not float_eq(v20.getValueAt(0), val0.value) or \
                not float_eq(v20.getValueAt(1), val1.value) or \
                not float_eq(v20.getValueAt(2), val2.value):
            BookEndPrint('----- pop (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- pop (index out of range) failed')
        rval = False
    try:
        v20.pop(-4)
    except IndexError:
        if v20.count() != 3 or \
                not float_eq(v20.getValueAt(0), val0.value) or \
                not float_eq(v20.getValueAt(1), val1.value) or \
                not float_eq(v20.getValueAt(2), val2.value):
            BookEndPrint('----- pop (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- pop (index out of range) failed')
        rval = False

    # pop (index invalid type) **error**
    try:
        v20.pop('twenty')
    except ValueError:
        if v20.count() != 3 or \
                not float_eq(v20.getValueAt(0), val0.value) or \
                not float_eq(v20.getValueAt(1), val1.value) or \
                not float_eq(v20.getValueAt(2), val2.value):
            BookEndPrint('----- pop (index invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- pop (index invalid type) failed')
        rval = False

    # test get value
    vals21 = (val0.value, val1.value, val2.value, val3.value)
    v21 = MI_Real32A(vals21)
    i = 0
    for v in v21:
        if not float_eq(v.value, vals21[i]):
            BookEndPrint('----- iterator (get value) failed')
            rval = False
        i += 1

    # iterator set value
    v22 = MI_Real32A((val0.value, val1.value, val2.value))
    vals22 = (val1.value, val2.value, val3.value)
    i = 0
    for v in v22:
        v.value = vals22[i]
        i += 1
    if v22.count() != 3 or \
            not float_eq(v22.getValueAt(0), val1.value) or \
            not float_eq(v22.getValueAt(1), val2.value) or \
            not float_eq(v22.getValueAt(2), val3.value):
        BookEndPrint('----- iterator (set value) failed')
        rval = False

    # iterator set value (out of range) **error**
    for v in v22:
        try:
            v.value = -1e39
        except ValueError:
            if v22.count() != 3 or \
                    not float_eq(v22.getValueAt(0), val1.value) or \
                    not float_eq(v22.getValueAt(1), val2.value) or \
                    not float_eq(v22.getValueAt(2), val3.value):
                BookEndPrint('----- iterator (set value out of range) failed')
                rval = False
        else:
            BookEndPrint('----- iterator (set value out of range) failed')
            rval = False
    for v in v22:
        try:
            v.value = 1e39
        except ValueError:
            if v22.count() != 3 or \
                    not float_eq(v22.getValueAt(0), val1.value) or \
                    not float_eq(v22.getValueAt(1), val2.value) or \
                    not float_eq(v22.getValueAt(2), val3.value):
                BookEndPrint('----- iterator (set value out of range) failed')
                rval = False
        else:
            BookEndPrint('----- iterator (set value out of range) failed')
            rval = False

    # iterator set value (invalid type)
    for v in v22:
        try:
            v.value = 'twenty-two'
        except ValueError:
            if v22.count() != 3 or \
                    not float_eq(v22.getValueAt(0), val1.value) or \
                    not float_eq(v22.getValueAt(1), val2.value) or \
                    not float_eq(v22.getValueAt(2), val3.value):
                BookEndPrint('----- iterator (set value invalid type) failed')
                rval = False
        else:
            BookEndPrint('----- iterator (set value invalid type) failed')
            rval = False

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_Real32A)')

    return rval
