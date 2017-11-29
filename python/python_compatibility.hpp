#ifndef INCLUDED_PYTHON_COMPATIBILITY_HPP
#define INCLUDED_PYTHON_COMPATIBILITY_HPP


#if PY_MAJOR_VERSION >= 3
    // All the functions that returned Python int objects are now gone
    // and wee need to replace them with the functions that returns
    // Python long objects.
    #define PyInt_FromLong PyLong_FromLong
    #define PyInt_FromSize_t PyLong_FromSize_t
    #define PyInt_FromSsize_t PyLong_FromSsize_t
    #define PyInt_Check PyLong_Check
    #define PyInt_AsLong PyLong_AsLong
    #define PyInt_FromLong PyLong_FromLong

    // Python 3 has now separate types for String, which doesn't exist anymore.
    // The new types are PyBytes and PyUnicode.
    // Using the following line will cause a memory leak on Python 3.
    // PyUnicode_AsEncodedString returns a new reference which needs to be
    // freed after the conversion
    // #define PyString_AsString(x) PyBytes_AsString(PyUnicode_AsEncodedString(x, "utf-8", "strict"))
    // Correct version to be used in the code:
    // PyObject* tmp = PyUnicode_AsEncodedString(x, "utf-8", "strict");
    // result = PyBytes_AsString(tmp);
    // Py_DECREF(tmp);
    #define PyString_Check PyUnicode_Check
    #define PyString_FromString PyUnicode_FromString
#endif

#endif // INCLUDED_PYTHON_COMPATIBILITY_HPP
