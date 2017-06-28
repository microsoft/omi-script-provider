// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include <cstdlib>
#include <iostream>
#include "py_gen.hpp"
#include "options.hpp"


int
main (
    int argc,
    char const** argv)
{
    int rval = EXIT_SUCCESS;
    Options options;
    rval = options.parseDestDir (&argc, argv);
    if (EXIT_SUCCESS == rval)
    {
        rval = options.getConfigOptions ();
    }
    if (EXIT_SUCCESS == rval)
    {
        rval = options.parseArgs (&argc, argv);
    }
    if (EXIT_SUCCESS == rval)
    {
        if (argc > 2 ||
            (options.all && argc > 1))
        {
            std::vector<std::string> mofFiles;
            if (!options.schemafile.empty ())
            {
                mofFiles.push_back (options.schemafile);
            }
            mofFiles.push_back (argv[1]);
            std::vector<std::string> classNames;
            for (int i = 2; i < argc; ++i)
            {
                classNames.push_back (argv[i]);
            }
            rval = Generate_Py (options, mofFiles, classNames);
        }
        else
        {
            std::cerr << "Usage: omigen_py PATH CLASSNAME ..." << std::endl;
            std::cerr << "Try 'omigen_py -h' for help"  << std::endl
                      << std::endl;
            rval = EXIT_FAILURE;
        }
    }
    return rval;
}
