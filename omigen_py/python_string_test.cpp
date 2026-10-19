// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include "python_string.hpp"

#include <iostream>
#include <sstream>
#ifdef _WIN32
#include <fcntl.h>
#include <io.h>
#endif


int main ()
{
#ifdef _WIN32
    _setmode (_fileno (stdin), _O_BINARY);
    _setmode (_fileno (stdout), _O_BINARY);
#endif
    std::ostringstream probe;
    probe.fill ('*');
    std::ios_base::fmtflags const flags = probe.flags ();
    probe << PythonString ("\001" "7");
    if (probe.str () != "'\\x017'" ||
        probe.fill () != '*' || probe.flags () != flags)
    {
        std::cerr << "PythonString changed stream state or escape width"
                  << std::endl;
        return 1;
    }

    std::cout << "# -*- coding: utf-8 -*-\nvalues = [\n";
    std::string value;
    while (std::getline (std::cin, value, '\0'))
    {
        std::cout << PythonString (value) << ",\n";
    }
    std::cout << "]\n";
    return std::cin.bad () || !std::cout ? 1 : 0;
}
