# Copyright (c) Microsoft Corporation.  All rights reserved.
# Licensed under the MIT license.
from __future__ import print_function

import ast
import io
import optparse
import os
import shutil
import subprocess
import sys
import tempfile
import types
import unittest


EMITTER = None
GENERATOR = None
PAYLOAD = "' + str(marker.append('executed')) + '"


class PythonStringTests(unittest.TestCase):
    def check_values(self, values):
        data = b"".join(value.encode("utf-8") + b"\0" for value in values)
        process = subprocess.Popen(
            [EMITTER], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        source, errors = process.communicate(data)
        self.assertEqual(0, process.returncode, errors)
        tree = ast.parse(source)
        string_node = ast.Constant if sys.version_info >= (3, 8) else ast.Str
        self.assertTrue(all(isinstance(node, string_node)
                            for node in tree.body[0].value.elts))
        scope = {"marker": []}
        eval(compile(source, "<generated literals>", "exec"), scope)
        actual = [value.decode("utf-8") if isinstance(value, bytes)
                  else value for value in scope["values"]]
        self.assertEqual(values, actual)
        self.assertEqual([], scope["marker"])

    def test_quotes_and_backslashes(self):
        self.check_values(["", "ordinary", "'", '"', "\\", "trailing\\",
                           "\\'", "\\\\'", "'\\", "\\n", "\\x27"])

    def test_control_characters(self):
        self.check_values([chr(value) + "7f" for value in range(1, 32)] +
                          ["\x7f", "\r\n\t\b\f"])

    def test_utf8(self):
        self.check_values([u"\u4e2d\u6587", u"\u00e9", u"\U0001f600",
                           u"\u2028\u2029", u"\u4e2d'\\\n\u6587"])

    def test_injection_remains_data(self):
        self.check_values([PAYLOAD, "\\' + str(marker.append('executed')) + '",
                           "'\nmarker.append('executed')\n#"])


class GeneratorTests(unittest.TestCase):
    def test_generator(self):
        directory = tempfile.mkdtemp(prefix="omigen-string-test-")
        old_omi = sys.modules.get("omi")
        try:
            mof = os.path.join(directory, "strings.mof")
            with io.open(mof, "w", encoding="utf-8") as output:
                output.write(
                    u'Qualifier Probe : string = "{0}", Scope(any);\n'
                    u'class OMI_StringProbe {{\n'
                    u' [Probe("{0}")] string Text = "{0}";\n'
                    u' string Items[] = {{"{0}", "trailing\\\\",'
                    u' "quote\'", "line\\nnext", "\u4e2d\u6587"}};\n'
                    u'}};\n'.format(PAYLOAD))
            subprocess.check_call(
                [GENERATOR, "-d", directory, mof, "OMI_StringProbe"])
            with open(os.path.join(directory, "schema.py"), "rb") as source:
                schema = source.read()
            self.assertTrue(b"coding: utf-8" in schema.splitlines()[1])
            tree = ast.parse(schema)
            omi = types.ModuleType("omi")
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and node.id.startswith("MI_"):
                    setattr(omi, node.id, 0 if node.id.isupper()
                            else lambda *args: args)
            omi.MI_String = lambda value: value
            omi.MI_StringA = lambda value: value
            sys.modules["omi"] = omi
            scope = {"marker": []}
            eval(compile(schema, "<generated schema>", "exec"), scope)
            self.assertEqual(PAYLOAD, scope["Probe_qual_decl_value"])
            self.assertEqual(PAYLOAD, scope["OMI_StringProbe_Text_value"])
            self.assertEqual(
                PAYLOAD, scope["OMI_StringProbe_Text_Probe_qual_value"])
            # OMI's MOF parser preserves backslash sequences in string values.
            self.assertEqual(
                [PAYLOAD, "trailing\\\\", "quote'", "line\\nnext",
                 u"\u4e2d\u6587"],
                [value.decode("utf-8") if isinstance(value, bytes) else value
                 for value in scope["OMI_StringProbe_Items_value"]])
            self.assertEqual([], scope["marker"])
            with open(os.path.join(directory, "mi_main.py"), "rb") as source:
                compile(source.read(), "<generated main>", "exec")
        finally:
            if old_omi is None:
                sys.modules.pop("omi", None)
            else:
                sys.modules["omi"] = old_omi
            shutil.rmtree(directory)


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("--emitter")
    parser.add_option("--generator")
    parser.add_option("-v", "--verbose", action="store_true", default=False)
    options, remaining = parser.parse_args()
    if not options.emitter:
        parser.error("--emitter is required")
    if remaining:
        parser.error("unexpected arguments: " + " ".join(remaining))
    EMITTER = os.path.abspath(options.emitter)
    GENERATOR = (os.path.abspath(options.generator)
                 if options.generator else None)
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(PythonStringTests)
    if GENERATOR:
        suite.addTests(loader.loadTestsFromTestCase(GeneratorTests))
    else:
        print("Generator tests omitted: requires --generator and an OMI build",
              file=sys.stderr)
    result = unittest.TextTestRunner(
        verbosity=2 if options.verbose else 1).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
