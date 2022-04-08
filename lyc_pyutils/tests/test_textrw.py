"""Executable that tests the text reading and writing utilities."""

# Copyright 2022 Yucheng Liu. GNU LGPL3 license.
# GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
# GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng

import os
import pathlib
import shutil
import typing
import unittest

from os import path as ospath

import lyc_pyutils

_copytree = shutil.copytree
_IO = typing.IO
_join = ospath.join
_makedirs = os.makedirs
_Path = pathlib.Path
_rmtree = shutil.rmtree
_TestCase = unittest.TestCase

_lyc_load_text = lyc_pyutils.load_text
_lyc_save_text = lyc_pyutils.save_text

_tests_path = _Path(__file__).parent
_repo_path = _Path(_tests_path).parent.parent

_default_configs_path = _join(_repo_path, "lyc_pyutils_default_configs")
_default_test_data_path = _join(_default_configs_path, "test_data")
_default_test_textrw_path = _join(_default_test_data_path, "test_textrw")

_test_data_path = _join(_repo_path, ".lyc_pyutils_test_data")
_log_loc = _join(_test_data_path, "log.txt")
_test_textrw_path = _join(_test_data_path, "test_textrw")


def _fix_newline_format(instr):
    instr = str(instr)

    result = instr
    result = result.replace("\r\n", "\n")
    result = result.replace("\r", "\n")
    return result


def _dquote_repr(instr):
    instr = str(instr)

    result = repr(instr)[1: -1]
    result = f"\"{result}\""
    return result


class _BaseCase(_TestCase):

    def __init__(self, methodName):
        """Initializes self with the given args."""
        super().__init__(methodName)

        self._log: _IO = None

    def setUp(self):
        """Sets up before the tests."""
        super().setUp()

        _makedirs(_test_data_path, exist_ok=True)
        self._log = open(_log_loc, "a+")

        case_name = type(self).__name__
        info = f"- Test-case {case_name}"
        self._logln(info)

    def tearDown(self):
        """Tears down after the tests."""
        super().tearDown()

        case_name = type(self).__name__
        info = f"- End of test-case {case_name}"
        self._logln(info)

        self._log.flush()
        self._log.close()

    def _logstr(self, str_to_log):
        str_to_log = str(str_to_log)

        if self._log is not None:
            self._log.write(str_to_log)

    def _logln(self, line):
        line = str(line)

        line = line + "\n"
        self._logstr(line)

    def _log_method_start(self, method_name):
        method_name = str(method_name)

        info = f"-- Test-method {method_name}"
        self._logln(info)

    def _log_method_end(self, method_name):
        method_name = str(method_name)

        info = f"-- End of test-method {method_name}"
        self._logln(info)


class TestLoadText(_BaseCase):
    """Tests for the load_text function."""

    def __init__(self, methodName):
        """Initializes self with the given args."""
        super().__init__(methodName)

        self._text1_loc = None

    def setUp(self):
        """Sets up before the tests."""
        super().setUp()

        _rmtree(_test_textrw_path, ignore_errors=True)
        _copytree(_default_test_textrw_path, _test_textrw_path)

        self._text1_loc = _join(_test_textrw_path, "text1.txt")

    def tearDown(self):
        """Tears down after the tests."""
        super().tearDown()

        _rmtree(_test_textrw_path, ignore_errors=True)

    def _match_values(self, actual, expect, not_match_info, match_info):
        not_match_info = str(not_match_info)
        match_info = str(match_info)

        fail_msg = not_match_info.format(actual, expect)
        success_msg = match_info.format(actual)
        self.assertTrue(actual == expect, fail_msg)
        self._logln(success_msg)

    def test_norm(self):
        """Tests the normal use case."""
        method_name = self.test_norm.__name__
        self._log_method_start(method_name)

        text1 = _lyc_load_text(self._text1_loc)

        not_match_info = str(
            f"load_text result does not match\n"
            f"Actual: {{}}\n"
            f"Expected: {{}}"
        )

        match_info = str(
            f"load_text result matched\n"
            f"Actual and expected {{}}"
        )

        actual = text1
        actual = _fix_newline_format(actual)

        expect = fr"""

text1
[ test textrw ]
[ textrw test ]

        """

        expect = expect.strip()
        expect = expect + "\n"
        expect = _fix_newline_format(expect)
        self._match_values(_dquote_repr(actual), _dquote_repr(expect), not_match_info, match_info)

        self._log_method_end(method_name)


class TestSaveText(_BaseCase):
    """Tests for the save_text function."""

    def __init__(self, methodName):
        """Initializes self with the given args."""
        super().__init__(methodName)

        self._text2_loc = None

    def setUp(self):
        """Sets up before the tests."""
        super().setUp()

        _rmtree(_test_textrw_path, ignore_errors=True)
        _copytree(_default_test_textrw_path, _test_textrw_path)

        self._text2_loc = _join(_test_textrw_path, "text2.txt")

    def tearDown(self):
        """Tears down after the tests."""
        super().tearDown()

        _rmtree(_test_textrw_path, ignore_errors=True)

    def _match_values(self, actual, expect, not_match_info, match_info):
        not_match_info = str(not_match_info)
        match_info = str(match_info)

        fail_msg = not_match_info.format(actual, expect)
        success_msg = match_info.format(actual)
        self.assertTrue(actual == expect, fail_msg)
        self._logln(success_msg)

    def test_norm(self):
        """Tests the normal use case."""
        method_name = self.test_norm.__name__
        self._log_method_start(method_name)

        text2 = fr"""

text2
[ test textrw ]
[ textrw test ]

        """

        text2 = text2.strip()
        text2 = text2 + "\n"
        _lyc_save_text(text2, self._text2_loc)

        file: _IO = open(self._text2_loc, "r")
        saved_text2 = file.read()
        file.close()

        not_match_info = str(
            f"save_text result does not match\n"
            f"Actual: {{}}\n"
            f"Expected: {{}}"
        )

        match_info = str(
            f"save_text result matched\n"
            f"Actual and expected {{}}"
        )

        actual = saved_text2
        actual = _fix_newline_format(actual)
        expect = text2
        expect = _fix_newline_format(expect)
        self._match_values(_dquote_repr(actual), _dquote_repr(expect), not_match_info, match_info)

        self._log_method_end(method_name)


def main():
    """Runs this module as an executable."""
    unittest.main(verbosity=1)


if __name__ == "__main__":
    main()
