// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#ifndef INCLUDED_PY_GEN_HPP
#define INCLUDED_PY_GEN_HPP


#include "options.hpp"
#include <gen/Parser.h>


#include <set>
#include <string>
#include <vector>


int
Generate_Py (
    Options const& options,
    std::vector<std::string> const& mofFiles,
    std::vector<std::string> const& sourceClassNames);


int
GenSchemaSourceFile_Py (
    Options const& options,
    Parser& parser,
    std::vector<std::string> const& classNames);


int
GenMI_Main_Py (
    Options const& options,
    Parser& parser,
    std::vector<std::string> const& classNames);


#endif // INCLUDED_PY_GEN_HPP
