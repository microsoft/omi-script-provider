from omi import *

try:
    from utils import *
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from utils import *


def timestamp_test():
    be = BookEnd('timestamp_test')

    rval = True

    # init (empty)
    v0 = MI_Timestamp()
    if v0.getType() != MI_DATETIME:
        BookEndPrint('----- getType failed')
        rval = False
    if not v0.isTimestamp():
        BookEndPrint('----- isTimestamp failed')
        rval = False
    if 0 != v0.year or \
            0 != v0.month or \
            0 != v0.day or \
            0 != v0.hour or \
            0 != v0.minute or \
            0 != v0.second or \
            0 != v0.microseconds or \
            0 != v0.utc:
        BookEndPrint('----- empty init failed')
        rval = False

    # init (year only)
    y1 = random.randint(0, 0xFFFF)
    v1 = MI_Timestamp(year=y1)
    if y1 != v1.year or \
            0 != v1.month or \
            0 != v1.day or \
            0 != v1.hour or \
            0 != v1.minute or \
            0 != v1.second or \
            0 != v1.microseconds or \
            0 != v1.utc:
        BookEndPrint('----- init (year only) failed')
        rval = False

    # init (month only)
    m2 = random.randint(1, 12)
    v2 = MI_Timestamp(month=m2)
    if 0 != v2.year or \
            m2 != v2.month or \
            0 != v2.day or \
            0 != v2.hour or \
            0 != v2.minute or \
            0 != v2.second or \
            0 != v2.microseconds or \
            0 != v2.utc:
        BookEndPrint('----- init (month only) failed')
        rval = False

    # init (day only)
    d3 = random.randint(1, 28)
    v3 = MI_Timestamp(day=d3)
    if 0 != v3.year or \
            0 != v3.month or \
            d3 != v3.day or \
            0 != v3.hour or \
            0 != v3.minute or \
            0 != v3.second or \
            0 != v3.microseconds or \
            0 != v3.utc:
        BookEndPrint('----- init (day only) failed')
        rval = False

    # init (hour only)
    h4 = random.randint(1, 23)
    v4 = MI_Timestamp(hour=h4)
    if 0 != v4.year or \
            0 != v4.month or \
            0 != v4.day or \
            h4 != v4.hour or \
            0 != v4.minute or \
            0 != v4.second or \
            0 != v4.microseconds or \
            0 != v4.utc:
        BookEndPrint('----- init (hour only) failed')
        rval = False

    # init (minute only)
    min5 = random.randint(1, 59)
    v5 = MI_Timestamp(minute=min5)
    if 0 != v5.year or \
            0 != v5.month or \
            0 != v5.day or \
            0 != v5.hour or \
            min5 != v5.minute or \
            0 != v5.second or \
            0 != v5.microseconds or \
            0 != v5.utc:
        BookEndPrint('----- init (minute only) failed')
        rval = False

    # init (second only)
    s6 = random.randint(1, 59)
    v6 = MI_Timestamp(second=s6)
    if 0 != v6.year or \
            0 != v6.month or \
            0 != v6.day or \
            0 != v6.hour or \
            0 != v6.minute or \
            s6 != v6.second or \
            0 != v6.microseconds or \
            0 != v6.utc:
        BookEndPrint('----- init (second only) failed')
        rval = False

    # init (microseconds only)
    ms7 = random.randint(1, 999)
    v7 = MI_Timestamp(microseconds=ms7)
    if 0 != v7.year or \
            0 != v7.month or \
            0 != v7.day or \
            0 != v7.hour or \
            0 != v7.minute or \
            0 != v7.second or \
            ms7 != v7.microseconds or \
            0 != v7.utc:
        BookEndPrint('----- init (microseconds only) failed')
        rval = False

    # init (utc only)
    u8 = random.randint(1, 11)
    v8 = MI_Timestamp(utc=u8)
    if 0 != v8.year or \
            0 != v8.month or \
            0 != v8.day or \
            0 != v8.hour or \
            0 != v8.minute or \
            0 != v8.second or \
            0 != v8.microseconds or \
            u8 != v8.utc:
        BookEndPrint('----- init (utc only) failed')
        rval = False

    # init (all)
    y9 = random.randint(0, 9)
    m9 = random.randint(10, 19)
    d9 = random.randint(20, 29)
    h9 = random.randint(30, 39)
    min9 = random.randint(40, 49)
    s9 = random.randint(50, 59)
    ms9 = random.randint(60, 61)
    u9 = random.randint(70, 79)
    v9 = MI_Timestamp(y9, m9, d9, h9, min9, s9, ms9, u9)
    if y9 != v9.year or \
            m9 != v9.month or \
            d9 != v9.day or \
            h9 != v9.hour or \
            min9 != v9.minute or \
            s9 != v9.second or \
            ms9 != v9.microseconds or \
            u9 != v9.utc:
        BookEndPrint('----- init (all) failed')
        rval = False
    #BookEndPrint (str (v9))

    # init underflow (year)
    try:
        v10 = MI_Timestamp(year=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (year) failed')
        rval = False

    # init overflow (year)
    try:
        v11 = MI_Timestamp(year=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (year) failed')
        rval = False

    # init invalid type (year)
    try:
        v12 = MI_Timestamp(year='twelve')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (year) failed')
        rval = False

    # init underflow (month)
    try:
        v13 = MI_Timestamp(month=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (month) failed')
        rval = False

    # init overflow (month)
    try:
        v14 = MI_Timestamp(month=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (month) failed')
        rval = False

    # init invalid type (month)
    try:
        v15 = MI_Timestamp(month='fifteen')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (month) failed')
        rval = False

    # init underflow (day)
    try:
        v16 = MI_Timestamp(day=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (day) failed')
        rval = False

    # init overflow (day)
    try:
        v17 = MI_Timestamp(day=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (day) failed')
        rval = False

    # init invalid type (day)
    try:
        v18 = MI_Timestamp(day='eighteen')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (day) failed')
        rval = False

    # init underflow (hour)
    try:
        v19 = MI_Timestamp(hour=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (hour) failed')
        rval = False

    # init overflow (hour)
    try:
        v20 = MI_Timestamp(hour=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (hour) failed')
        rval = False

    # init invalid type (hour)
    try:
        v21 = MI_Timestamp(hour='twenty-one')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (hour) failed')
        rval = False

    # init underflow (minute)
    try:
        v22 = MI_Timestamp(minute=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (minute) failed')
        rval = False

    # init overflow (minute)
    try:
        v23 = MI_Timestamp(minute=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (minute) failed')
        rval = False

    # init invalid type (minute)
    try:
        v24 = MI_Timestamp(minute='twenty-four')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (minute) failed')
        rval = False

    # init underflow (second)
    try:
        v25 = MI_Timestamp(second=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (second) failed')
        rval = False

    # init overflow (second)
    try:
        v26 = MI_Timestamp(second=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (second) failed')
        rval = False

    # init invalid type (second)
    try:
        v27 = MI_Timestamp(second='twenty-seven')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (second) failed')
        rval = False

    # init underflow (microseconds)
    try:
        v28 = MI_Timestamp(microseconds=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (microseconds) failed')
        rval = False

    # init overflow (microseconds)
    try:
        v29 = MI_Timestamp(microseconds=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (microseconds) failed')
        rval = False

    # init invalid type (microseconds)
    try:
        v30 = MI_Timestamp(microseconds='thirty')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (microseconds) failed')
        rval = False

    # init underflow (utc)
    try:
        v31 = MI_Timestamp(utc=-0x80000001)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (utc) failed')
        rval = False

    # init overflow (utc)
    try:
        v32 = MI_Timestamp(utc=0x80000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (utc) failed')
        rval = False

    # init invalid type (utc)
    try:
        v33 = MI_Timestamp(utc='thirty')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (utc) failed')
        rval = False

    # set underflow (year)
    v34 = MI_Timestamp()
    try:
        v34.year = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (year) failed')
        rval = False

    # set overflow (year)
    v35 = MI_Timestamp()
    try:
        v35.year = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (year) failed')
        rval = False

    # set invalid type (year)
    v36 = MI_Timestamp()
    try:
        v36.year = 'thirty-six'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (year) failed')
        rval = False

    # set underflow (month)
    v37 = MI_Timestamp()
    try:
        v37.month = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (month) failed')
        rval = False

    # set overflow (month)
    v38 = MI_Timestamp()
    try:
        v38.month = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (month) failed')
        rval = False

    # set invalid type (month)
    v39 = MI_Timestamp()
    try:
        v39.month = 'thirty-nine'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (month) failed')
        rval = False

    # set underflow (day)
    v40 = MI_Timestamp()
    try:
        v40.day = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (day) failed')
        rval = False

    # set overflow (day)
    v41 = MI_Timestamp()
    try:
        v41.day = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (day) failed')
        rval = False

    # set invalid type (day)
    v42 = MI_Timestamp()
    try:
        v42.day = 'forty-two'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (day) failed')
        rval = False

    # set underflow (hour)
    v43 = MI_Timestamp()
    try:
        v43.hour = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (hour) failed')
        rval = False

    # set overflow (hour)
    v44 = MI_Timestamp()
    try:
        v44.hour = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (hour) failed')
        rval = False

    # set invalid type (hour)
    v45 = MI_Timestamp()
    try:
        v45.hour = 'forty-five'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (hour) failed')
        rval = False

    # set underflow (minute)
    v46 = MI_Timestamp()
    try:
        v46.minute = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (minute) failed')
        rval = False

    # set overflow (minute)
    v47 = MI_Timestamp()
    try:
        v47.minute = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (minute) failed')
        rval = False

    # set invalid type (minute)
    v48 = MI_Timestamp()
    try:
        v48.minute = 'forty-eight'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (minute) failed')
        rval = False

    # set underflow (second)
    v49 = MI_Timestamp()
    try:
        v49.second = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (second) failed')
        rval = False

    # set overflow (second)
    v50 = MI_Timestamp()
    try:
        v50.second = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (second) failed')
        rval = False

    # set invalid type (second)
    v51 = MI_Timestamp()
    try:
        v51.second = 'fifty-one'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (second) failed')
        rval = False

    # set underflow (microseconds)
    v52 = MI_Timestamp()
    try:
        v52.microseconds = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (microseconds) failed')
        rval = False

    # set overflow (microseconds)
    v53 = MI_Timestamp()
    try:
        v53.microseconds = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (microseconds) failed')
        rval = False

    # set invalid type (microseconds)
    v54 = MI_Timestamp()
    try:
        v54.microseconds = 'fifty-four'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (microseconds) failed')
        rval = False

    # set underflow (utc)
    v55 = MI_Timestamp()
    try:
        v55.utc = -0x80000001
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (utc) failed')
        rval = False

    # set overflow (utc)
    v56 = MI_Timestamp()
    try:
        v56.utc = 0x80000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (utc) failed')
        rval = False

    # set invalid type (utc)
    v57 = MI_Timestamp()
    try:
        v57.utc = 'fifty-seven'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (utc) failed')
        rval = False

    # set (year)
    v58 = MI_Timestamp()
    y58 = random.randint(0, 2000)
    v58.year = y58
    if y58 != v58.year or \
            0 != v58.month or \
            0 != v58.day or \
            0 != v58.hour or \
            0 != v58.minute or \
            0 != v58.second or \
            0 != v58.microseconds or \
            0 != v58.utc:
        BookEndPrint('----- set (year) failed')
        rval = False

    # set (month)
    v59 = MI_Timestamp()
    m59 = random.randint(1, 12)
    v59.month = m59
    if 0 != v59.year or \
            m59 != v59.month or \
            0 != v59.day or \
            0 != v59.hour or \
            0 != v59.minute or \
            0 != v59.second or \
            0 != v59.microseconds or \
            0 != v59.utc:
        BookEndPrint('----- set (month) failed')
        rval = False

    # set (day)
    v60 = MI_Timestamp()
    d60 = random.randint(1, 28)
    v60.day = d60
    if 0 != v60.year or \
            0 != v60.month or \
            d60 != v60.day or \
            0 != v60.hour or \
            0 != v60.minute or \
            0 != v60.second or \
            0 != v60.microseconds or \
            0 != v60.utc:
        BookEndPrint('----- set (day) failed')
        rval = False

    # set (hour)
    v61 = MI_Timestamp()
    h61 = random.randint(0, 23)
    v61.hour = h61
    if 0 != v61.year or \
            0 != v61.month or \
            0 != v61.day or \
            h61 != v61.hour or \
            0 != v61.minute or \
            0 != v61.second or \
            0 != v61.microseconds or \
            0 != v61.utc:
        BookEndPrint('----- set (hour) failed')
        rval = False

    # set (minute)
    v62 = MI_Timestamp()
    min62 = random.randint(0, 59)
    v62.minute = min62
    if 0 != v62.year or \
            0 != v62.month or \
            0 != v62.day or \
            0 != v62.hour or \
            min62 != v62.minute or \
            0 != v62.second or \
            0 != v62.microseconds or \
            0 != v62.utc:
        BookEndPrint('----- set (minute) failed')
        rval = False

    # set (second)
    v63 = MI_Timestamp()
    s63 = random.randint(0, 59)
    v63.second = s63
    if 0 != v63.year or \
            0 != v63.month or \
            0 != v63.day or \
            0 != v63.hour or \
            0 != v63.minute or \
            s63 != v63.second or \
            0 != v63.microseconds or \
            0 != v63.utc:
        BookEndPrint('----- set (second) failed')
        rval = False

    # set (microseconds)
    v64 = MI_Timestamp()
    ms64 = random.randint(0, 999)
    v64.microseconds = ms64
    if 0 != v64.year or \
            0 != v64.month or \
            0 != v64.day or \
            0 != v64.hour or \
            0 != v64.minute or \
            0 != v64.second or \
            ms64 != v64.microseconds or \
            0 != v64.utc:
        BookEndPrint('----- set (microseconds) failed')
        rval = False

    # set (utc)
    v65 = MI_Timestamp()
    u65 = random.randint(0, 12)
    v65.utc = u65
    if 0 != v65.year or \
            0 != v65.month or \
            0 != v65.day or \
            0 != v65.hour or \
            0 != v65.minute or \
            0 != v65.second or \
            0 != v65.microseconds or \
            u65 != v65.utc:
        BookEndPrint('----- set (utc) failed')
        rval = False

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_Timestamp)')

    return rval


def interval_test():
    be = BookEnd('interval_test')

    rval = True

    # init (empty)
    v0 = MI_Interval()
    if v0.getType() != MI_DATETIME:
        BookEndPrint('----- getType failed')
        rval = False
    if v0.isTimestamp():
        BookEndPrint('----- isTimestamp failed')
        rval = False
    if 0 != v0.days or \
            0 != v0.hours or \
            0 != v0.minutes or \
            0 != v0.seconds or \
            0 != v0.microseconds:
        BookEndPrint('----- empty init failed')
        rval = False

    # init (days only)
    d1 = random.randint(1, 28)
    v1 = MI_Interval(days=d1)
    if d1 != v1.days or \
            0 != v1.hours or \
            0 != v1.minutes or \
            0 != v1.seconds or \
            0 != v1.microseconds:
        BookEndPrint('----- init (days only) failed')
        rval = False

    # init (hours only)
    h2 = random.randint(1, 23)
    v2 = MI_Interval(hours=h2)
    if 0 != v2.days or \
            h2 != v2.hours or \
            0 != v2.minutes or \
            0 != v2.seconds or \
            0 != v2.microseconds:
        BookEndPrint('----- init (hours only) failed')
        rval = False

    # init (minutes only)
    m3 = random.randint(1, 59)
    v3 = MI_Interval(minutes=m3)
    if 0 != v3.days or \
            0 != v3.hours or \
            m3 != v3.minutes or \
            0 != v3.seconds or \
            0 != v3.microseconds:
        BookEndPrint('----- init (minutes only) failed')
        rval = False

    # init (seconds only)
    s4 = random.randint(1, 59)
    v4 = MI_Interval(seconds=s4)
    if 0 != v4.days or \
            0 != v4.hours or \
            0 != v4.minutes or \
            s4 != v4.seconds or \
            0 != v4.microseconds:
        BookEndPrint('----- init (seconds only) failed')
        rval = False

    # init (microseconds only)
    ms5 = random.randint(1, 999)
    v5 = MI_Interval(microseconds=ms5)
    if 0 != v5.days or \
            0 != v5.hours or \
            0 != v5.minutes or \
            0 != v5.seconds or \
            ms5 != v5.microseconds:
        BookEndPrint('----- init (microseconds only) failed')
        rval = False

    # init (all)
    d6 = random.randint(21, 30)
    h6 = random.randint(31, 40)
    m6 = random.randint(41, 50)
    s6 = random.randint(51, 60)
    ms6 = random.randint(61, 70)
    v6 = MI_Interval(d6, h6, m6, s6, ms6)
    if d6 != v6.days or \
            h6 != v6.hours or \
            m6 != v6.minutes or \
            s6 != v6.seconds or \
            ms6 != v6.microseconds:
        BookEndPrint('----- init (all) failed')
        rval = False
    #BookEndPrint (str (v6))

    # init underflow (days)
    try:
        v7 = MI_Interval(days=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (days) failed')
        rval = False

    # init overflow (days)
    try:
        v8 = MI_Interval(days=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (days) failed')
        rval = False

    # init invalid type (days)
    try:
        v9 = MI_Interval(days='nine')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (days) failed')
        rval = False

    # init underflow (hours)
    try:
        v10 = MI_Interval(hours=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (hours) failed')
        rval = False

    # init overflow (hours)
    try:
        v11 = MI_Interval(hours=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (hours) failed')
        rval = False

    # init invalid type (hours)
    try:
        v12 = MI_Interval(hours='twelve')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (hours) failed')
        rval = False

    # init underflow (minutes)
    try:
        v13 = MI_Interval(minutes=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (minutes) failed')
        rval = False

    # init overflow (minutes)
    try:
        v14 = MI_Interval(minutes=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (minutes) failed')
        rval = False

    # init invalid type (minutes)
    try:
        v15 = MI_Interval(minutes='fifteen')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (minutes) failed')
        rval = False

    # init underflow (seconds)
    try:
        v16 = MI_Interval(seconds=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (seconds) failed')
        rval = False

    # init overflow (seconds)
    try:
        v17 = MI_Interval(seconds=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (seconds) failed')
        rval = False

    # init invalid type (seconds)
    try:
        v18 = MI_Interval(seconds='eighteen')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (second) failed')
        rval = False

    # init underflow (microseconds)
    try:
        v19 = MI_Interval(microseconds=-1)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init underflow (microseconds) failed')
        rval = False

    # init overflow (microseconds)
    try:
        v20 = MI_Interval(microseconds=0x100000000)
    except ValueError:
        pass
    else:
        BookEndPrint('----- init overflow (microseconds) failed')
        rval = False

    # init invalid type (microseconds)
    try:
        v21 = MI_Interval(microseconds='twenty-one')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init invalid type (microseconds) failed')
        rval = False

    # set underflow (days)
    v22 = MI_Interval()
    try:
        v22.days = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (days) failed')
        rval = False

    # set overflow (days)
    v23 = MI_Interval()
    try:
        v23.days = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (days) failed')
        rval = False

    # set invalid type (days)
    v24 = MI_Interval()
    try:
        v24.days = 'twenty-four'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (days) failed')
        rval = False

    # set underflow (hours)
    v25 = MI_Interval()
    try:
        v25.hours = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (hours) failed')
        rval = False

    # set overflow (hours)
    v26 = MI_Interval()
    try:
        v26.hours = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (hours) failed')
        rval = False

    # set invalid type (hours)
    v27 = MI_Interval()
    try:
        v27.hours = 'twenty-seven'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (hours) failed')
        rval = False

    # set underflow (minutes)
    v28 = MI_Interval()
    try:
        v28.minutes = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (minutes) failed')
        rval = False

    # set overflow (minutes)
    v29 = MI_Interval()
    try:
        v29.minutes = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (minutes) failed')
        rval = False

    # set invalid type (minutes)
    v30 = MI_Interval()
    try:
        v30.minutes = 'thirty'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (minutes) failed')
        rval = False

    # set underflow (seconds)
    v31 = MI_Interval()
    try:
        v31.seconds = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (seconds) failed')
        rval = False

    # set overflow (seconds)
    v32 = MI_Interval()
    try:
        v32.seconds = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (seconds) failed')
        rval = False

    # set invalid type (seconds)
    v33 = MI_Interval()
    try:
        v33.seconds = 'thirty-three'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (seconds) failed')
        rval = False

    # set underflow (microseconds)
    v34 = MI_Interval()
    try:
        v34.microseconds = -1
    except ValueError:
        pass
    else:
        BookEndPrint('----- set underflow (microseconds) failed')
        rval = False

    # set overflow (microseconds)
    v35 = MI_Interval()
    try:
        v35.microseconds = 0x100000000
    except ValueError:
        pass
    else:
        BookEndPrint('----- set overflow (microseconds) failed')
        rval = False

    # set invalid type (microseconds)
    v36 = MI_Interval()
    try:
        v36.microseconds = 'thirty-six'
    except ValueError:
        pass
    else:
        BookEndPrint('----- set invalid type (microseconds) failed')
        rval = False

    # set (days)
    v37 = MI_Interval()
    d37 = random.randint(0, 2000)
    v37.days = d37
    if d37 != v37.days or \
            0 != v37.hours or \
            0 != v37.minutes or \
            0 != v37.seconds or \
            0 != v37.microseconds:
        BookEndPrint('----- set (days) failed')
        rval = False

    # set (hours)
    v38 = MI_Interval()
    h38 = random.randint(0, 23)
    v38.hours = h38
    if 0 != v38.days or \
            h38 != v38.hours or \
            0 != v38.minutes or \
            0 != v38.seconds or \
            0 != v38.microseconds:
        BookEndPrint('----- set (hours) failed')
        rval = False

    # set (minutes)
    v39 = MI_Interval()
    m39 = random.randint(0, 59)
    v39.minutes = m39
    if 0 != v39.days or \
            0 != v39.hours or \
            m39 != v39.minutes or \
            0 != v39.seconds or \
            0 != v39.microseconds:
        BookEndPrint('----- set (minutes) failed')
        rval = False

    # set (seconds)
    v40 = MI_Interval()
    s40 = random.randint(0, 59)
    v40.seconds = s40
    if 0 != v40.days or \
            0 != v40.hours or \
            0 != v40.minutes or \
            s40 != v40.seconds or \
            0 != v40.microseconds:
        BookEndPrint('----- set (seconds) failed')
        rval = False

    # set (microseconds)
    v40 = MI_Interval()
    ms40 = random.randint(0, 999)
    v40.microseconds = ms40
    if 0 != v40.days or \
            0 != v40.hours or \
            0 != v40.minutes or \
            0 != v40.seconds or \
            ms40 != v40.microseconds:
        BookEndPrint('----- set (microseconds) failed')
        rval = False

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_Interval)')

    return rval
