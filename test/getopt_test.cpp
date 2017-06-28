// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include "getopt_test.hpp"


#include <base/omigetopt.h>


using test::getopt_test;


namespace test
{


/*ctor*/
getopt_test::getopt_test ()
{
    add_test (MAKE_TEST (getopt_test::test01));
    add_test (MAKE_TEST (getopt_test::test02));
    add_test (MAKE_TEST (getopt_test::test03));
    add_test (MAKE_TEST (getopt_test::test04));
    add_test (MAKE_TEST (getopt_test::test05));
    add_test (MAKE_TEST (getopt_test::test06));
    add_test (MAKE_TEST (getopt_test::test07));
    add_test (MAKE_TEST (getopt_test::test08));
    add_test (MAKE_TEST (getopt_test::test09));
}


int
getopt_test::test01 ()
{
    // test with no args and no opts
    int argc = 1;
    char const* argv[] = {
        "Test", // exe name
    };
    char const* opts[] = {
        NULL,
    };
    int rval = EXIT_SUCCESS;
    GetOptState state = GETOPTSTATE_INITIALIZER;
    if (1 != GetOpt (&argc, argv, opts, &state))
    {
        rval = EXIT_FAILURE;
    }
    return rval;
}


int
getopt_test::test02 ()
{
    // test with opts not in args
    int argc = 1;
    char const* argv[] = {
        "Test", // exe name
    };
    char const* opts[] = {
        "-n", // not in args
        "-m", // not in args
        "-l", // not in args
        NULL,
    };
    int rval = EXIT_SUCCESS;
    GetOptState state = GETOPTSTATE_INITIALIZER;
    if (1 != GetOpt (&argc, argv, opts, &state))
    {
        rval = EXIT_FAILURE;
    }
    return rval;
}


int
getopt_test::test03 ()
{
    // test with opts in args
    int argc = 4;
    char const* argv[] = {
        "Test", // exe name
        "-n", // in opts
        "-m", // in opts
        "-l", // in opts
    };
    char const* opts[] = {
        "-n", // in args
        "-m", // in args
        "-l", // in args
        NULL,
    };
    int rval = EXIT_SUCCESS;
    GetOptState state = GETOPTSTATE_INITIALIZER;
    int result = 0;
    for (size_t i = 0; 0 == result && i < 3; ++i)
    {
        result = GetOpt (&argc, argv, opts, &state);
        if (0 == result &&
            (0 != strcmp (state.opt, opts[i]) ||
             NULL != state.arg))
        {
            rval = EXIT_FAILURE;
        }
    }
    if (1 != GetOpt (&argc, argv, opts, &state))
    {
        rval = EXIT_FAILURE;
    }
    return rval;
}


int
getopt_test::test04 ()
{
    // test with args not in opts
    int argc = 5;
    char const* argv[] = {
        "Test", // exe name
        "-n", // in opts
        "-XXX", // not in opts
        "-m", // in opts
        "-l", // in opts
    };
    char const* opts[] = {
        "-n", // in args
        "-m", // in args
        "-l", // in args
        NULL,
    };
    int rval = EXIT_SUCCESS;
    GetOptState state = GETOPTSTATE_INITIALIZER;
    int result = 0;
    for (size_t i = 0; 0 == result && i < 4; ++i)
    {
        result = GetOpt (&argc, argv, opts, &state);
    }
    if (-1 != result)
    {
        rval = EXIT_FAILURE;
    }
    return rval;
}


int
getopt_test::test05 ()
{
    // <arguments> test with opts not in args
    int argc = 1;
    char const* argv[] = {
        "Test", // exe name
    };
    char const* opts[] = {
        "-n:", // not in args
        "-m:", // not in args
        "-l:", // not in args
        NULL,
    };
    int rval = EXIT_SUCCESS;
    GetOptState state = GETOPTSTATE_INITIALIZER;
    if (1 != GetOpt (&argc, argv, opts, &state))
    {
        rval = EXIT_FAILURE;
    }
    return rval;
}


int
getopt_test::test06 ()
{
    // <arguments equal> test with opts in args with arguments
    int argc = 4;
    char const* argv[] = {
        "Test", // exe name
        "-n=n_value", // in opts
        "-m=m_value", // in opts
        "-l=l_value", // in opts
    };
    char const* opts[] = {
        "-n:", // in args
        "-m:", // in args
        "-l:", // in args
        NULL,
    };
    int rval = EXIT_SUCCESS;
    GetOptState state = GETOPTSTATE_INITIALIZER;
    int result = 0;
    for (size_t i = 0; 0 == result && i < 3; ++i)
    {
        result = GetOpt (&argc, argv, opts, &state);
        if (0 == result &&
            (0 != strncmp (state.opt, opts[i], 2) ||
             *(state.arg) != opts[i][1]))
        {
            rval = EXIT_FAILURE;
        }
    }
    if (1 != GetOpt (&argc, argv, opts, &state))
    {
        rval = EXIT_FAILURE;
    }
    return rval;
}


int
getopt_test::test07 ()
{
    // <optional arguments> test with opts in args without arguments
    int argc = 4;
    char const* argv[] = {
        "Test", // exe name
        "-n",// "n_value", // in opts
        "-m",// "m_value", // in opts
        "-l",// "l_value", // in opts
    };
    char const* opts[] = {
        "-n?", // in args
        "-m?", // in args
        "-l?", // in args
        NULL,
    };
    int rval = EXIT_SUCCESS;
    GetOptState state = GETOPTSTATE_INITIALIZER;
    int result = 0;
    for (size_t i = 0; 0 == result && i < 3; ++i)
    {
        result = GetOpt (&argc, argv, opts, &state);
        if (0 == result &&
            (0 != strncmp (state.opt, opts[i], 2) ||
             NULL != state.arg))//*(state.arg) != opts[i][1]))
        {
            rval = EXIT_FAILURE;
        }
    }
    if (1 != GetOpt (&argc, argv, opts, &state))
    {
        rval = EXIT_FAILURE;
    }
    return rval;
}


int
getopt_test::test08 ()
{
    // <optional arguments> test with opts in args with arguments
    int argc = 4;
    char const* argv[] = {
        "Test", // exe name
        "-n=n_value", // in opts
        "-m=m_value", // in opts
        "-l=l_value", // in opts
    };
    char const* opts[] = {
        "-n?", // in args
        "-m?", // in args
        "-l?", // in args
        NULL,
    };
    int rval = EXIT_SUCCESS;
    GetOptState state = GETOPTSTATE_INITIALIZER;
    int result = 0;
    for (size_t i = 0; 0 == result && i < 3; ++i)
    {
        result = GetOpt (&argc, argv, opts, &state);
        if (0 == result &&
            (0 != strncmp (state.opt, opts[i], 2) ||
             *(state.arg) != opts[i][1]))
        {
            rval = EXIT_FAILURE;
        }
    }
    if (1 != GetOpt (&argc, argv, opts, &state))
    {
        rval = EXIT_FAILURE;
    }
    return rval;
}


int
getopt_test::test09 ()
{
    // <arguments> test with opts w/o arguments with args with arguments
    int argc = 4;
    char const* argv[] = {
        "Test", // exe name
        "-n=n_value", // in opts
        "-m=m_value", // in opts
        "-l=l_value", // in opts
    };
    char const* opts[] = {
        "-n", // in args
        "-m", // in args
        "-l", // in args
        NULL,
    };
    int rval = EXIT_SUCCESS;
    GetOptState state = GETOPTSTATE_INITIALIZER;
    if (-1 != GetOpt (&argc, argv, opts, &state))
    {
        rval = EXIT_FAILURE;
    }
    return rval;
}


} // namespace test
