// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#ifndef INCLUDED_OPTIONS_HPP
#define INCLUDED_OPTIONS_HPP


#include <string>
#include <vector>


class Options
{
public:
    /*ctor*/ Options ();

    int parseDestDir (int* argc, char const** argv);
    int getConfigOptions ();
    int parseArgs (int* argc, char const** argv);

    // List of directories to search for included MOF files.
    std::vector<std::string> paths;

    // qualifier flags
    bool ignoreAllQualifiers;
    bool standardQualifiers;
    bool booleanQualifiers;
    bool descriptions;
    bool values;
    bool mappingStrings;
    bool modelCorrespondence;

    // Operate quietly if true (do not print anything to standard output).
    bool quiet;

    // Include all classes encountered during parsing in generated output.
    bool all;

    // Place all output files in this directory. If empty, place output files
    // in the current directory.
    std::string dir;

    // Print no warnings if true (otherwise print them).
    bool no_warnings;

    std::string schemafile;
};


#endif // INLCUDED_OPTIONS_HPP
