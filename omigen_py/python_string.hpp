// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#ifndef INCLUDED_PYTHON_STRING_HPP
#define INCLUDED_PYTHON_STRING_HPP

#include <ostream>
#include <string>


class PythonString
{
public:
    explicit PythonString (std::string const& value)
        : m_Value (value)
    {
    }

    template<typename CHAR_t, typename TRAITS>
    std::basic_ostream<CHAR_t, TRAITS>&
    to_stream (std::basic_ostream<CHAR_t, TRAITS>& strm) const
    {
        static char const hex[] = "0123456789abcdef";
        strm << '\'';
        for (std::string::const_iterator pos = m_Value.begin (),
                 endPos = m_Value.end ();
             pos != endPos;
             ++pos)
        {
            unsigned char const ch = static_cast<unsigned char>(*pos);
            if ('\'' == ch || '\\' == ch)
            {
                strm << '\\' << static_cast<char>(ch);
            }
            else if (ch < 0x20 || ch == 0x7f)
            {
                strm << "\\x" << hex[ch >> 4] << hex[ch & 0x0f];
            }
            else
            {
                // Preserve UTF-8 bytes in the UTF-8 encoded Python source.
                strm << static_cast<char>(ch);
            }
        }
        strm << '\'';
        return strm;
    }

private:
    std::string const m_Value;
};


template<typename CHAR_t, typename TRAITS>
std::basic_ostream<CHAR_t, TRAITS>&
operator << (
    std::basic_ostream<CHAR_t, TRAITS>& strm,
    PythonString const& value)
{
    return value.to_stream (strm);
}


#endif // INCLUDED_PYTHON_STRING_HPP
