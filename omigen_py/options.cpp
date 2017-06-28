// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include "options.hpp"


#include <base/conf.h>
#include <base/env.h>
#include <base/omigetopt.h>
#include <base/paths.h>
#include <cstdlib>
#include <iostream>


namespace
{


char const* const HELP = "\
Usage: %s [OPTIONS] PATH CLASSNAME ...\n\
\n\
OVERVIEW:\n\
    This program generates provider source code from MOF class definitions.\n\
    PATH is a file that contains the MOF definitions (or includes them).\n\
    It must include any dependent MOF defintions as well (such as the CIM\n\
    schema). The PATH is followed by a list of CLASSNAME arguments, which are\n\
    the names of the MOF classes to be generated.\n\
\n\
OPTIONS:\n\
    -I PATH            Search this directory for included MOF files.\n\
    -D                 Generate 'Description' qualifiers.\n\
    -V                 Generate 'Values' and 'ValueMap' qualifiers.\n\
    -M                 Generate 'MappingStrings' qualifiers.\n\
    -O                 Generate 'ModelCorrespondence' qualifiers.\n\
    -S                 Generate standard CIM qualifier declarations.\n\
    -B                 Generate boolean qualifiers.\n\
    -Q                 Suppress qualifier declarations generation.\n\
    -q                 Quiet mode - do not print anything on stdout.\n\
    -h, --help         Print this help message.\n\
    -v, --version      Print the program version.\n\
    -d PATH            Place output files in this directory.\n\
    --no-warnings      Print no warnings.\n\
\n\
EXAMPLES:\n\
    The following example generates a 'MSFT_ComputerSystem' class, which is\n\
    defined in schema.mof.\n\
\n\
        $ omigen_py schema.mof MSFT_ComputerSystem\n\
        Created schema.py\n\
        Created mi_main.py\n\
\n\
";


} // namespace (unnamed)


/*ctor*/
Options::Options ()
    : paths ()
    , ignoreAllQualifiers (false)
    , standardQualifiers (false)
    , booleanQualifiers (false)
    , descriptions (false)
    , values (false)
    , mappingStrings (false)
    , modelCorrespondence (false)
    , quiet (false)
    , all (false)
    , dir ()
    , no_warnings (false)
    , schemafile ()
{
    // empty
}


int
Options::parseDestDir (
    int* argc,
    char const** argv)
{
    int rval = EXIT_SUCCESS;
    char const* destdir = NULL;
    int i = 1;
    while (EXIT_SUCCESS == rval &&
           i < *argc)
    {
        if (0 == strcmp (argv[i], "--destdir"))
        {
            if (i + 1 < *argc)
            {
                destdir = argv[i + 1];
                memmove (argv + i, argv + i + 2,
                         sizeof (char const*) * (*argc - i - 1));
                (*argc) -= 2;
            }
            else
            {
                std::cerr << "missing argument for --destdir option"
                          << std::endl;
                rval = EXIT_FAILURE;
            }
        }
        else if (0 == strncmp (argv[i], "--destdir=", 10))
        {
            destdir = argv[i] + 10;
            memmove (argv + i, argv + i + 1,
                     sizeof (char const*) * (*argc - i));
            --(*argc);
        }
        else
        {
            ++i;
        }
    }
    if (destdir)
    {
        if (0 != SetPath (ID_DESTDIR, destdir))
        {
            std::cerr << "failed to set destdir" << std::endl;
            rval = EXIT_FAILURE;
        }
    }
    schemafile = OMI_GetPath (ID_SCHEMAFILE);
    return rval;
}


int
Options::getConfigOptions ()
{
    int rval = EXIT_SUCCESS;
    char path[PAL_MAX_PATH_SIZE];
    Strlcpy (path, "./.omigenrc", PAL_MAX_PATH_SIZE);
    if (0 != access (path, R_OK))
    {
        char* home = Dupenv ("HOME");
        if (home)
        {
            Strlcpy (path, home, PAL_MAX_PATH_SIZE);
            PAL_Free (home);
            Strlcat (path, "/.omigenrc", PAL_MAX_PATH_SIZE);
            if (0 != access (path, R_OK))
            {
                Strlcpy (path, OMI_GetPath (ID_DESTDIR), PAL_MAX_PATH_SIZE);
                Strlcat (path, "/", PAL_MAX_PATH_SIZE);
                Strlcat (path, OMI_GetPath (ID_SYSCONFDIR), PAL_MAX_PATH_SIZE);
                Strlcat (path, "/omigen.conf", PAL_MAX_PATH_SIZE);
                if (0 != access (path, R_OK))
                {
                    std::cerr << "failed to find configuration file"
                              << std::endl;
                    rval = EXIT_FAILURE;
                }
            }
        }
    }
    if (EXIT_SUCCESS == rval)
    {
        Conf* conf = NULL;
        conf = Conf_Open (path);
        if (conf)
        {
            char const* key = NULL;
            char const* value = NULL;
            int result = Conf_Read (conf, &key, &value);
            while (EXIT_SUCCESS == rval &&
                   0 == result)
            {
                if (0 == strcmp (key, "schemafile"))
                {
                    if (NULL != value &&
                        0 < strlen (value) &&
                        0 == access (value, R_OK))
                    {
                        schemafile = value;
                    }
                    else
                    {
                        std::cerr << path << ": file given by '" << key
                                  << "' key does not exits: " << value
                                  << std::endl;
                        rval = EXIT_FAILURE;
                    }
                }
                else
                {
                    std::cerr << path << ": unknown key: " << key << std::endl;
                    rval = EXIT_FAILURE;
                }
                if (EXIT_SUCCESS == rval)
                {
                    result = Conf_Read (conf, &key, &value);
                }
            }
            Conf_Close (conf);
        }
        else
        {
            std::cerr << "failed to open configuration file: " << path
                      << std::endl;
            rval = EXIT_FAILURE;
        }
    }


    return rval;
}


int
Options::parseArgs (
    int* argc,
    char const** argv)
{
    char const* opts[] = {
        "-I:",
        "-h",
        "--help",
        "-v",
        "--version",
        "-D",
        "-V",
        "-M",
        "-O",
        "-S",
        "-B",
        "-Q",
        "-f", // nix
        "-q",
        "--no-warnings",
        "-a",
        "-n", // nix
        "--cpp", // nix
        "-s:", // nix
        "-d:",
        "-e:", // nix
        "-y:", // nix
        "-l", // nix
        "-reg:", // nix
        "-A", // nix
        "-C:", // nix
        "--schemafile:", // nix
        "-m:", // nix
        "--nogi:", // nix
        NULL,
    };
    int rval = EXIT_SUCCESS;
    GetOptState state = GETOPTSTATE_INITIALIZER;
    int result = 0;
    while (EXIT_SUCCESS == rval &&
           0 == result)
    {
        result = GetOpt (argc, argv, opts, &state);
        if (0 == result)
        {
            if (0 == strcmp (state.opt, "-I"))
            {
                paths.push_back (state.arg);
            }
            else if (0 == strcmp (state.opt, "-h") ||
                     0 == strcmp (state.opt, "--help"))
            {
                std::cout << HELP;
                rval = EXIT_FAILURE;
            }
            else if (0 == strcmp (state.opt, "-v") ||
                     0 == strcmp (state.opt, "--version"))
            {
                std::cout << argv[0] << ": " CONFIG_PRODUCT "-" CONFIG_VERSION
                          << " - " CONFIG_DATE << std::endl;
                rval = EXIT_FAILURE;
            }
            else if (0 == strcmp (state.opt, "-D"))
            {
                descriptions = true;
            }
            else if (0 == strcmp (state.opt, "-V"))
            {
                values = true;
            }
            else if (0 == strcmp (state.opt, "-M"))
            {
                mappingStrings = true;
            }
            else if (0 == strcmp (state.opt, "-O"))
            {
                modelCorrespondence = true;
            }
            else if (0 == strcmp (state.opt, "-S"))
            {
                standardQualifiers = true;
            }
            else if (0 == strcmp (state.opt, "-B"))
            {
                booleanQualifiers = true;
            }
            else if (0 == strcmp (state.opt, "-Q"))
            {
                ignoreAllQualifiers = true;
            }
            else if (0 == strcmp (state.opt, "-q"))
            {
                quiet = true;
            }
            else if (0 == strcmp (state.opt, "--no-warnings"))
            {
                no_warnings = true;
            }
            else if (0 == strcmp (state.opt, "-a"))
            {
                all = true;
            }
            else if (0 == strcmp (state.opt, "-d"))
            {
                dir = state.arg;
            }
        }
        else if (-1 == result)
        {
            std::cerr << state.err << std::endl;
            rval = EXIT_FAILURE;
        }
    }
    return rval;
}
