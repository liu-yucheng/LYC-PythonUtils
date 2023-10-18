"""Executable that tests the clamps utilities."""

# Copyright 2022-2023 Yucheng Liu. GNU LGPL3 license.
# GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
# GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng

import os
import pathlib
# import shutil
import typing
import unittest
from os import path as ospath

import lyc_pyutils

# _copytree = shutil.copytree
_IO = typing.IO
_join = ospath.join
_makedirs = os.makedirs
_Path = pathlib.Path
# _rmtree = shutil.rmtree
_TestCase = unittest.TestCase

_lyc_clamp_float = lyc_pyutils.clamp_float
_lyc_clamp_int = lyc_pyutils.clamp_int

_tests_path = _Path(__file__).parent
_repo_path = _Path(_tests_path).parent.parent

# _default_configs_path = _join(_repo_path, "lyc_pyutils_default_configs")
# _default_test_data_path = _join(_default_configs_path, "test_data")

_test_data_path = _join(_repo_path, ".lyc_pyutils_test_data")
_log_loc = _join(_test_data_path, "log.txt")


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


class TestClampFloat(_BaseCase):
    """Tests for the clamp_float function."""

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

        not_match_info = str(
            f"Clamp result does not match\n"
            f"Actual: {{}}\n"
            f"Expected: {{}}\n"
        )

        match_info = str(
            f"Clamp result matched\n"
            f"Actual and expected: {{}}\n"
        )

        bound1 = float(0)
        bound2 = float(1)

        inval = 0.5
        outval = _lyc_clamp_float(inval, bound1, bound2)
        self._match_values(outval, inval, not_match_info, match_info)

        inval = 1.5
        outval = _lyc_clamp_float(inval, bound1, bound2)
        self._match_values(outval, bound2, not_match_info, match_info)

        inval = -0.5
        outval = _lyc_clamp_float(inval, bound1, bound2)
        self._match_values(outval, bound1, not_match_info, match_info)

        inval = 0.5
        outval = _lyc_clamp_float(inval, bound2, bound1)
        self._match_values(outval, inval, not_match_info, match_info)

        inval = 1.5
        outval = _lyc_clamp_float(inval, bound2, bound1)
        self._match_values(outval, bound2, not_match_info, match_info)

        inval = -0.5
        outval = _lyc_clamp_float(inval, bound2, bound1)
        self._match_values(outval, bound1, not_match_info, match_info)

        self._log_method_end(method_name)


class TestClampInt(_BaseCase):
    """Tests for the clamp_int function."""

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

        not_match_info = str(
            f"Clamp result does not match\n"
            f"Actual: {{}}\n"
            f"Expected: {{}}\n"
        )

        match_info = str(
            f"Clamp result matched\n"
            f"Actual and expected: {{}}\n"
        )

        bound1 = 0
        bound2 = 2

        inval = 1
        outval = _lyc_clamp_int(inval, bound1, bound2)
        self._match_values(outval, inval, not_match_info, match_info)

        inval = 3
        outval = _lyc_clamp_int(inval, bound1, bound2)
        self._match_values(outval, bound2, not_match_info, match_info)

        inval = -1
        outval = _lyc_clamp_int(inval, bound1, bound2)
        self._match_values(outval, bound1, not_match_info, match_info)

        inval = 1
        outval = _lyc_clamp_int(inval, bound2, bound1)
        self._match_values(outval, inval, not_match_info, match_info)

        inval = 3
        outval = _lyc_clamp_int(inval, bound2, bound1)
        self._match_values(outval, bound2, not_match_info, match_info)

        inval = -1
        outval = _lyc_clamp_int(inval, bound2, bound1)
        self._match_values(outval, bound1, not_match_info, match_info)

        self._log_method_end(method_name)


def main():
    """Runs this module as an executable."""
    unittest.main(verbosity=1)


if __name__ == "__main__":
    main()
