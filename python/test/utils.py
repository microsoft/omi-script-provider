import ctypes
import random
import sys


COPY_CTOR = False
ASSIGN_OP = False


def float_eq(left, right):
    if (left > 0 and right > 0):
        if left > right:
            return (left - right) < sys.float_info.epsilon
        else:
            return (right - left) < sys.float_info.epsilon
    elif (left < 0 and right < 0):
        if left < right:
            return (left - right) < sys.float_info.epsilon
        else:
            return (right - left) < sys.float_info.epsilon
    return False


def datetime_eq(left, right):
    if left.isTimestamp() and right.isTimestamp():
        if left.year == right.year and \
                left.month == right.month and \
                left.day == right.day and \
                left.hour == right.hour and \
                left.minute == right.minute and \
                left.second == right.second and \
                left.microseconds == right.microseconds and \
                left.utc == right.utc:
            return True
        else:
            return False
    elif not left.isTimestamp() and not right.isTimestamp():
        if left.days == right.days and \
                left.hours == right.hours and \
                left.minutes == right.minutes and \
                left.seconds == right.seconds and \
                left.microseconds == right.microseconds:
            return True
        return False
    else:
        return False


def array_eq(lhs, rhs):
    rval = True
    if lhs.count() == rhs.count():
        for i in range(lhs.count()):
            rval = rval and lhs.getValueAt(i) == rhs.getValueAt(i)
    else:
        rval = False
    return rval


def float_array_eq(lhs, rhs):
    rval = True
    if lhs.count() == rhs.count():
        for i in range(lhs.count()):
            rval = rval and float_eq(lhs.getValueAt(i), rhs.getValueAt(i))
    else:
        rval = False
    return rval


def datetime_array_eq(lhs, rhs):
    rval = True
    if lhs.count() == rhs.count():
        for i in range(lhs.count()):
            rval = rval and datetime_eq(lhs.getValueAt(i), rhs.getValueAt(i))
    else:
        rval = False
    return rval
