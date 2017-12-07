from omi import *

try:
    from utils import *
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from utils import *


def datetimea_test():
    be = BookEnd('datetimea_test')

    ts0 = MI_Timestamp(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49),
        random.randint(50, 59),
        random.randint(60, 69),
        random.randint(70, 79))
    ts1 = MI_Timestamp(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49),
        random.randint(50, 59),
        random.randint(60, 69),
        random.randint(70, 79))
    ts2 = MI_Timestamp(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49),
        random.randint(50, 59),
        random.randint(60, 69),
        random.randint(70, 79))

    i0 = MI_Interval(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49))

    i1 = MI_Interval(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49))

    i2 = MI_Interval(
        random.randint(0, 9),
        random.randint(10, 19),
        random.randint(20, 29),
        random.randint(30, 39),
        random.randint(40, 49))

    rval = True

    # init (empty)
    v0 = MI_DatetimeA()
    if MI_DATETIMEA != v0.getType():
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

    # PyList init (all MI_Timestamp)
    v1 = MI_DatetimeA([ts0, ts1, ts2])
    if v1.count() != 3:
        BookEndPrint('----- PyList init failed')
        rval = False
    if not datetime_eq(v1.getValueAt(0), ts0) or \
            not datetime_eq(v1.getValueAt(1), ts1) or \
            not datetime_eq(v1.getValueAt(2), ts2) or \
            not datetime_eq(v1.getValueAt(-3), ts0) or \
            not datetime_eq(v1.getValueAt(-2), ts1) or \
            not datetime_eq(v1.getValueAt(-1), ts2):
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

    # test that getValueAt returns a clone and not a reference
    val1 = v1.getValueAt(1)
    val1.year = val1.year + 1
    if datetime_eq(v1.getValueAt(1), val1):
        BookEndPrint('----- getValueAt returned a reference')
        rval = False

    # test that the initializer stores a clone and not a reference
    y4 = random.randint(0, 9)
    while y4 == ts0.year:
        y4 = random.randint(0, 9)
    ts0.year = y4
    if datetime_eq(v1.getValueAt(0), ts0):
        BookEndPrint('----- initializer stored a reference')
        rval = False

    # PyList init (all MI_Interval)
    v2 = MI_DatetimeA([i0, i1, i2])
    if v2.count() != 3:
        BookEndPrint('----- PyList init failed')
        rval = False
    if not datetime_eq(v2.getValueAt(0), i0) or \
       not datetime_eq(v2.getValueAt(1), i1) or \
       not datetime_eq(v2.getValueAt(2), i2) or \
       not datetime_eq(v2.getValueAt(-3), i0) or \
       not datetime_eq(v2.getValueAt(-2), i1) or \
       not datetime_eq(v2.getValueAt(-1), i2):
        BookEndPrint('----- PyList init or getValueAt failed')
        rval = False

    # test getValueAt (out of range) **error**
    try:
        v2.getValueAt(-4)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False
    try:
        v2.getValueAt(3)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False

    # test getValueAt (invalid type) **error**
    try:
        v2.getValueAt('two')
    except ValueError:
        pass
    else:
        BookEndPrint('----- getValueAt (invalid type) failed')
        rval = False

    # test that getValueAt returns a clone and not a reference
    val1 = v2.getValueAt(1)
    val1.days = val1.days + 1
    if datetime_eq(v2.getValueAt(1), val1):
        BookEndPrint('----- getValueAt returned a reference')
        rval = False

    # test that the initializer stores a clone and not a reference
    d4 = random.randint(0, 9)
    while d4 == i0.days:
        d4 = random.randint(0, 9)
    i0.days = d4
    if datetime_eq(v2.getValueAt(0), i0):
        BookEndPrint('----- initializer stored a reference')
        rval = False

    # PyList init (mixed MI_Timestamp and MI_Interval)
    v3 = MI_DatetimeA([ts0, i0, ts1, i1])
    if v3.count() != 4:
        BookEndPrint('----- PyList init failed')
        rval = False
    if not datetime_eq(v3.getValueAt(0), ts0) or \
       not datetime_eq(v3.getValueAt(1), i0) or \
       not datetime_eq(v3.getValueAt(2), ts1) or \
       not datetime_eq(v3.getValueAt(3), i1) or \
       not datetime_eq(v3.getValueAt(-4), ts0) or \
       not datetime_eq(v3.getValueAt(-3), i0) or \
       not datetime_eq(v3.getValueAt(-2), ts1) or \
       not datetime_eq(v3.getValueAt(-1), i1):
        BookEndPrint('----- PyList init or getValueAt failed')
        rval = False

    #BookEndPrint (str (v3))

    # test getValueAt (out of range) **error**
    try:
        v3.getValueAt(-5)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False
    try:
        v3.getValueAt(4)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False

    # test getValueAt (invalid type) **error**
    try:
        v3.getValueAt('three')
    except ValueError:
        pass
    else:
        BookEndPrint('----- getValueAt (invalid type) failed')
        rval = False

    # test that getValueAt returns a clone and not a reference
    val1 = v3.getValueAt(1)
    val1.days = val1.days + 1
    if datetime_eq(v3.getValueAt(1), val1):
        BookEndPrint('----- getValueAt returned a reference')
        rval = False

    # test that the initializer stores a clone and not a reference
    y4 = random.randint(0, 9)
    while y4 == ts0.year:
        y4 = random.randint(0, 9)
    ts0.year = y4
    if datetime_eq(v3.getValueAt(0), ts0):
        BookEndPrint('----- initializer stored a reference')
        rval = False

    # PyTuple init (all MI_Timestamp)
    v4 = MI_DatetimeA((ts0, ts1, ts2))
    if v4.count() != 3:
        BookEndPrint('----- PyTuple init failed')
        rval = False
    if not datetime_eq(v4.getValueAt(0), ts0) or \
       not datetime_eq(v4.getValueAt(1), ts1) or \
       not datetime_eq(v4.getValueAt(2), ts2) or \
       not datetime_eq(v4.getValueAt(-3), ts0) or \
       not datetime_eq(v4.getValueAt(-2), ts1) or \
       not datetime_eq(v4.getValueAt(-1), ts2):
        BookEndPrint('----- PyTuple init or getValueAt failed')
        rval = False

    # test getValueAt (out of range) **error**
    try:
        v4.getValueAt(-4)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False
    try:
        v4.getValueAt(3)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False

    # test getValueAt (invalid type) **error**
    try:
        v4.getValueAt('four')
    except ValueError:
        pass
    else:
        BookEndPrint('----- getValueAt (invalid type) failed')
        rval = False

    # test that getValueAt returns a clone and not a reference
    val1 = v4.getValueAt(1)
    val1.year = val1.year + 1
    if datetime_eq(v4.getValueAt(1), val1):
        BookEndPrint('----- getValueAt returned a reference')
        rval = False

    # test that the initializer stores a clone and not a reference
    y4 = random.randint(0, 9)
    while y4 == ts0.year:
        y4 = random.randint(0, 9)
    ts0.year = y4
    if datetime_eq(v4.getValueAt(0), ts0):
        BookEndPrint('----- initializer stored a reference')
        rval = False

    # PyTuple init (all MI_Interval)
    v5 = MI_DatetimeA((i0, i1, i2))
    if v5.count() != 3:
        BookEndPrint('----- PyTuple init failed')
        rval = False
    if not datetime_eq(v5.getValueAt(0), i0) or \
       not datetime_eq(v5.getValueAt(1), i1) or \
       not datetime_eq(v5.getValueAt(2), i2) or \
       not datetime_eq(v5.getValueAt(-3), i0) or \
       not datetime_eq(v5.getValueAt(-2), i1) or \
       not datetime_eq(v5.getValueAt(-1), i2):
        BookEndPrint('----- PyTuple init or getValueAt failed')
        rval = False

    # test getValueAt (out of range) **error**
    try:
        v5.getValueAt(-4)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False
    try:
        v5.getValueAt(3)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False

    # test getValueAt (invalid type) **error**
    try:
        v5.getValueAt('five')
    except ValueError:
        pass
    else:
        BookEndPrint('----- getValueAt (invalid type) failed')
        rval = False

    # test that getValueAt returns a clone and not a reference
    val1 = v5.getValueAt(1)
    val1.days = val1.days + 1
    if datetime_eq(v5.getValueAt(1), val1):
        BookEndPrint('----- getValueAt returned a reference')
        rval = False

    # test that the initializer stores a clone and not a reference
    d4 = random.randint(0, 9)
    while d4 == i0.days:
        d4 = random.randint(0, 9)
    i0.days = d4
    if datetime_eq(v5.getValueAt(0), i0):
        BookEndPrint('----- initializer stored a reference')
        rval = False

    # PyTuple init (mixed MI_Timestamp and MI_Interval)
    v6 = MI_DatetimeA([ts0, i0, ts1, i1])
    if v6.count() != 4:
        BookEndPrint('----- PyTuple init failed')
        rval = False
    if not datetime_eq(v6.getValueAt(0), ts0) or \
       not datetime_eq(v6.getValueAt(1), i0) or \
       not datetime_eq(v6.getValueAt(2), ts1) or \
       not datetime_eq(v6.getValueAt(3), i1) or \
       not datetime_eq(v6.getValueAt(-4), ts0) or \
       not datetime_eq(v6.getValueAt(-3), i0) or \
       not datetime_eq(v6.getValueAt(-2), ts1) or \
       not datetime_eq(v6.getValueAt(-1), i1):
        BookEndPrint('----- PyTuple init or getValueAt failed')
        rval = False

    # test getValueAt (out of range) **error**
    try:
        v6.getValueAt(-5)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False
    try:
        v6.getValueAt(4)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False

    # test getValueAt (invalid type) **error**
    try:
        v6.getValueAt('six')
    except ValueError:
        pass
    else:
        BookEndPrint('----- getValueAt (invalid type) failed')
        rval = False

    # test that getValueAt returns a clone and not a reference
    val1 = v6.getValueAt(1)
    val1.days = val1.days + 1
    if datetime_eq(v6.getValueAt(1), val1):
        BookEndPrint('----- getValueAt returned a reference')
        rval = False

    # test that the initializer stores a clone and not a reference
    y4 = random.randint(0, 9)
    while y4 == ts0.year:
        y4 = random.randint(0, 9)
    ts0.year = y4
    if datetime_eq(v6.getValueAt(0), ts0):
        BookEndPrint('----- initializer stored a reference')
        rval = False

    # init from None
    v7 = MI_DatetimeA(None)
    if v7.count() != 0:
        BookEndPrint('----- None init failed')
        rval = False

    # init from invalid literal value **error**
    try:
        v8 = MI_DatetimeA('eight')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to invalid literal failed')
        rval = False

    # PyList init (None) **error**
    try:
        v9 = MI_DatetimeA([ts0, None, i0])
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyList init (None value) failed')
        rval = False

    # PyList init (invalid type) **error**
    try:
        v10 = MI_DatetimeA([ts0, 'ten', i0])
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyList init (invalid type) failed')
        rval = False

    # PyTuple init (None)
    try:
        v11 = MI_DatetimeA((ts0, None, i0))
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyTuple init (None value) failed')
        rval = False

    # PyTuple init (invalid type) **error**
    try:
        v12 = MI_DatetimeA((ts0, 'twelve', i0))
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyTuple init (invalid type) failed')
        rval = False

    # setValueAt
    v13 = MI_DatetimeA((ts0, i0, ts1, i1))
    v13.setValueAt(0, ts2)
    if v13.count() != 4 or \
            not datetime_eq(v13.getValueAt(0), ts2) or \
            not datetime_eq(v13.getValueAt(1), i0) or \
            not datetime_eq(v13.getValueAt(2), ts1) or \
            not datetime_eq(v13.getValueAt(3), i1):
        BookEndPrint('----- setValueAt failed')
        rval = False

    v13.setValueAt(1, i2)
    if v13.count() != 4 or \
            not datetime_eq(v13.getValueAt(0), ts2) or \
            not datetime_eq(v13.getValueAt(1), i2) or \
            not datetime_eq(v13.getValueAt(2), ts1) or \
            not datetime_eq(v13.getValueAt(3), i1):
        BookEndPrint('----- setValueAt failed')
        rval = False

    v13.setValueAt(2, i0)
    if v13.count() != 4 or \
            not datetime_eq(v13.getValueAt(0), ts2) or \
            not datetime_eq(v13.getValueAt(1), i2) or \
            not datetime_eq(v13.getValueAt(2), i0) or \
            not datetime_eq(v13.getValueAt(3), i1):
        BookEndPrint('----- setValueAt failed')
        rval = False

    v13.setValueAt(3, ts0)
    if v13.count() != 4 or \
            not datetime_eq(v13.getValueAt(0), ts2) or \
            not datetime_eq(v13.getValueAt(1), i2) or \
            not datetime_eq(v13.getValueAt(2), i0) or \
            not datetime_eq(v13.getValueAt(3), ts0):
        BookEndPrint('----- setValueAt failed')
        rval = False

    v13.setValueAt(-1, i1)
    if v13.count() != 4 or \
            not datetime_eq(v13.getValueAt(0), ts2) or \
            not datetime_eq(v13.getValueAt(1), i2) or \
            not datetime_eq(v13.getValueAt(2), i0) or \
            not datetime_eq(v13.getValueAt(3), i1):
        BookEndPrint('----- setValueAt failed')
        rval = False

    v13.setValueAt(-2, ts1)
    if v13.count() != 4 or \
            not datetime_eq(v13.getValueAt(0), ts2) or \
            not datetime_eq(v13.getValueAt(1), i2) or \
            not datetime_eq(v13.getValueAt(2), ts1) or \
            not datetime_eq(v13.getValueAt(3), i1):
        BookEndPrint('----- setValueAt failed')
        rval = False

    v13.setValueAt(-3, i0)
    if v13.count() != 4 or \
            not datetime_eq(v13.getValueAt(0), ts2) or \
            not datetime_eq(v13.getValueAt(1), i0) or \
            not datetime_eq(v13.getValueAt(2), ts1) or \
            not datetime_eq(v13.getValueAt(3), i1):
        BookEndPrint('----- setValueAt failed')
        rval = False

    v13.setValueAt(-4, ts0)
    if v13.count() != 4 or \
            not datetime_eq(v13.getValueAt(0), ts0) or \
            not datetime_eq(v13.getValueAt(1), i0) or \
            not datetime_eq(v13.getValueAt(2), ts1) or \
            not datetime_eq(v13.getValueAt(3), i1):
        BookEndPrint('----- setValueAt failed')
        rval = False

    # setValueAt (index out of range) **error**
    try:
        v13.setValueAt(-5, ts2)
    except IndexError:
        if v13.count() != 4 or \
                not datetime_eq(v13.getValueAt(0), ts0) or \
                not datetime_eq(v13.getValueAt(1), i0) or \
                not datetime_eq(v13.getValueAt(2), ts1) or \
                not datetime_eq(v13.getValueAt(3), i1):
            BookEndPrint('----- setValueAt (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (index out of range) failed')
        rval = False

    try:
        v13.setValueAt(4, i2)
    except IndexError:
        if v13.count() != 4 or \
                not datetime_eq(v13.getValueAt(0), ts0) or \
                not datetime_eq(v13.getValueAt(1), i0) or \
                not datetime_eq(v13.getValueAt(2), ts1) or \
                not datetime_eq(v13.getValueAt(3), i1):
            BookEndPrint('----- setValueAt (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (index out of range) failed')
        rval = False

    # setValueAt (index invalid type) **error**
    try:
        v13.setValueAt('one', ts2)
    except ValueError:
        if v13.count() != 4 or \
                not datetime_eq(v13.getValueAt(0), ts0) or \
                not datetime_eq(v13.getValueAt(1), i0) or \
                not datetime_eq(v13.getValueAt(2), ts1) or \
                not datetime_eq(v13.getValueAt(3), i1):
            BookEndPrint('----- setValueAt (index invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (index invalid type) failed')
        rval = False

    # setValueAt (value invalid type) **error**
    try:
        v13.setValueAt(1, 'thirteen')
    except ValueError:
        if v13.count() != 4 or \
                not datetime_eq(v13.getValueAt(0), ts0) or \
                not datetime_eq(v13.getValueAt(1), i0) or \
                not datetime_eq(v13.getValueAt(2), ts1) or \
                not datetime_eq(v13.getValueAt(3), i1):
            BookEndPrint('----- setValueAt (value invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (value invalid type) failed')
        rval = False

    # test that setValueAt stores a clone and not a reference
    y4 = random.randint(0, 9)
    while y4 == ts0.year:
        y4 = random.randint(0, 9)
    ts0.year = y4
    if datetime_eq(v13.getValueAt(0), ts0):
        BookEndPrint('----- setValueAt stored a reference')
        rval = False

    # insert
    v14 = MI_DatetimeA()
    v14.insert(0, ts0)
    if v14.count() != 1 or \
            not datetime_eq(v14.getValueAt(0), ts0):
        BookEndPrint('----- insert failed')
        rval = False
    v14.insert(0, i0)
    if v14.count() != 2 or \
            not datetime_eq(v14.getValueAt(0), i0) or \
            not datetime_eq(v14.getValueAt(1), ts0):
        BookEndPrint('----- insert failed')
        rval = False
    v14.insert(2, ts1)
    if v14.count() != 3 or \
            not datetime_eq(v14.getValueAt(0), i0) or \
            not datetime_eq(v14.getValueAt(1), ts0) or \
            not datetime_eq(v14.getValueAt(2), ts1):
        BookEndPrint('----- insert failed')
        rval = False
    v14.insert(2, i1)
    if v14.count() != 4 or \
            not datetime_eq(v14.getValueAt(0), i0) or \
            not datetime_eq(v14.getValueAt(1), ts0) or \
            not datetime_eq(v14.getValueAt(2), i1) or \
            not datetime_eq(v14.getValueAt(3), ts1):
        BookEndPrint('----- insert failed')
        rval = False

    # insert using negative indices
    v15 = MI_DatetimeA([ts2])
    v15.insert(-1, i2)
    if v15.count() != 2 or \
            not datetime_eq(v15.getValueAt(0), i2) or \
            not datetime_eq(v15.getValueAt(1), ts2):
        BookEndPrint('----- insert (negative index) failed')
        rval = False
    v15.insert(-1, ts1)
    if v15.count() != 3 or \
            not datetime_eq(v15.getValueAt(0), i2) or \
            not datetime_eq(v15.getValueAt(1), ts1) or \
            not datetime_eq(v15.getValueAt(2), ts2):
        BookEndPrint('----- insert (negative index) failed')
        rval = False

    # insert (index out of bounds) **error**
    try:
        v15.insert(4, i2)
    except IndexError:
        if v15.count() != 3 or \
                not datetime_eq(v15.getValueAt(0), i2) or \
                not datetime_eq(v15.getValueAt(1), ts1) or \
                not datetime_eq(v15.getValueAt(2), ts2):
            BookEndPrint('----- insert (index out of bounds) failed')
            rval = False
    else:
        BookEndPrint('----- insert (index out of bounds) failed')
        rval = False
    try:
        v15.insert(-4, i2)
    except IndexError:
        if v15.count() != 3 or \
                not datetime_eq(v15.getValueAt(0), i2) or \
                not datetime_eq(v15.getValueAt(1), ts1) or \
                not datetime_eq(v15.getValueAt(2), ts2):
            BookEndPrint('----- insert (index out of bounds) failed')
            rval = False
    else:
        BookEndPrint('----- insert (index out of bounds) failed')
        rval = False

    # insert (index invalid type) **error**
    try:
        v15.insert('fifteen', i2)
    except ValueError:
        if v15.count() != 3 or \
                not datetime_eq(v15.getValueAt(0), i2) or \
                not datetime_eq(v15.getValueAt(1), ts1) or \
                not datetime_eq(v15.getValueAt(2), ts2):
            BookEndPrint('----- insert (index invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- insert (index invalid type) failed')
        rval = False

    # value type invalid
    try:
        v15.insert(1, 'fifteen')
    except ValueError:
        if v15.count() != 3 or \
                not datetime_eq(v15.getValueAt(0), i2) or \
                not datetime_eq(v15.getValueAt(1), ts1) or \
                not datetime_eq(v15.getValueAt(2), ts2):
            BookEndPrint('----- insert (value invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- insert (value invalid type) failed')
        rval = False

    # pop
    v16 = MI_DatetimeA((ts0, i0, ts1, i1))
    t16 = v16.pop()
    if not datetime_eq(t16, i1) or \
            v16.count() != 3 or \
            not datetime_eq(v16.getValueAt(0), ts0) or \
            not datetime_eq(v16.getValueAt(1), i0) or \
            not datetime_eq(v16.getValueAt(2), ts1):
        BookEndPrint('----- pop failed')
        rval = False
    t16 = v16.pop(1)
    if not datetime_eq(t16, i0) or \
            v16.count() != 2 or \
            not datetime_eq(v16.getValueAt(0), ts0) or \
            not datetime_eq(v16.getValueAt(1), ts1):
        BookEndPrint('----- pop failed')
        rval = False
    v16.insert(1, i0)
    t16 = v16.pop(0)
    if not datetime_eq(t16, ts0) or \
            v16.count() != 2 or \
            not datetime_eq(v16.getValueAt(0), i0) or \
            not datetime_eq(v16.getValueAt(1), ts1):
        BookEndPrint('----- pop failed')
        rval = False
    v16.insert(0, ts0)
    t16 = v16.pop(2)
    if not datetime_eq(t16, ts1) or \
            v16.count() != 2 or \
            not datetime_eq(v16.getValueAt(0), ts0) or \
            not datetime_eq(v16.getValueAt(1), i0):
        BookEndPrint('----- pop failed')
        rval = False

    # pop (negative indices)
    v17 = MI_DatetimeA((ts0, i0, ts1))
    t17 = v17.pop(-2)
    if not datetime_eq(t17, i0) or \
            v17.count() != 2 or \
            not datetime_eq(v17.getValueAt(0), ts0) or \
            not datetime_eq(v17.getValueAt(1), ts1):
        BookEndPrint('----- pop failed')
        rval = False
    v17.insert(1, i0)
    t17 = v17.pop(-3)
    if not datetime_eq(t17, ts0) or \
            v17.count() != 2 or \
            not datetime_eq(v17.getValueAt(0), i0) or \
            not datetime_eq(v17.getValueAt(1), ts1):
        BookEndPrint('----- pop failed')
        rval = False
    v17.insert(0, ts0)
    t17 = v17.pop(-1)
    if not datetime_eq(t17, ts1) or \
            v17.count() != 2 or \
            not datetime_eq(v17.getValueAt(0), ts0) or \
            not datetime_eq(v17.getValueAt(1), i0):
        BookEndPrint('----- pop failed')
        rval = False

    # pop (empty array) **error**
    v18 = MI_DatetimeA()
    try:
        v18.pop()
    except IndexError:
        pass
    else:
        BookEndPrint('----- pop (empty array) failed')
        rval = False

    v19 = MI_DatetimeA((ts0, i0, ts1))
    try:
        v19.pop(3)
    except IndexError:
        if v19.count() != 3 or \
                not datetime_eq(v19.getValueAt(0), ts0) or \
                not datetime_eq(v19.getValueAt(1), i0) or \
                not datetime_eq(v19.getValueAt(2), ts1):
            BookEndPrint('----- pop (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- pop (index out of range) failed')
        rval = False
    try:
        v19.pop(-4)
    except IndexError:
        if v19.count() != 3 or \
                not datetime_eq(v19.getValueAt(0), ts0) or \
                not datetime_eq(v19.getValueAt(1), i0) or \
                not datetime_eq(v19.getValueAt(2), ts1):
            BookEndPrint('----- pop (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- pop (index out of range) failed')
        rval = False

    # pop (index invalid type) **error**
    try:
        v19.pop('nineteen')
    except ValueError:
        if v19.count() != 3 or \
                not datetime_eq(v19.getValueAt(0), ts0) or \
                not datetime_eq(v19.getValueAt(1), i0) or \
                not datetime_eq(v19.getValueAt(2), ts1):
            BookEndPrint('----- pop (index invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- pop (index invalid type) failed')
        rval = False

    # iterator
    # test get value
    vals20 = (ts0, i0, ts1, i1)
    v20 = MI_DatetimeA(vals20)
    i = 0
    for v in v20:
        if not datetime_eq(v.value, vals20[i]):
            BookEndPrint('----- iterator (get value) failed')
            rval = False
        i += 1

    # iterator set value
    v21 = MI_DatetimeA((ts0, i0, ts1))
    vals21 = (i1, ts2, i2)
    i = 0
    for v in v21:
        v.value = vals21[i]
        i += 1
    if v21.count() != 3 or \
            not datetime_eq(v21.getValueAt(0), i1) or \
            not datetime_eq(v21.getValueAt(1), ts2) or \
            not datetime_eq(v21.getValueAt(2), i2):
        BookEndPrint('----- iterator (set value) failed')
        rval = False

    # iterator set value (invalid type)
    for v in v21:
        try:
            v.value = 'twenty-one'
        except ValueError:
            if v21.count() != 3 or \
                    not datetime_eq(v21.getValueAt(0), i1) or \
                    not datetime_eq(v21.getValueAt(1), ts2) or \
                    not datetime_eq(v21.getValueAt(2), i2):
                BookEndPrint('----- iterator (set value invalid type) failed')
                rval = False
        else:
            BookEndPrint('----- iterator (set value invalid type) failed')
            rval = False

    # test that setValue stores a clone and not a reference
    y4 = random.randint(0, 9)
    while y4 == ts2.year:
        y4 = random.randint(0, 9)
    ts2.year = y4
    if datetime_eq(v21.getValueAt(1), ts2):
        BookEndPrint('----- setValue stored a reference')
        rval = False

    # to_str
    # for v in v21:
    #    BookEndPrint (str (v))

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_DatetimeA)')

    return rval
