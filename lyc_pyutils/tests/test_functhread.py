"""Executable that tests the functional thread utilities."""

# Copyright 2022 Yucheng Liu. GNU GPL3 license.
# GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt
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

_LYCFuncThread = lyc_pyutils.FuncThread

_tests_path = _Path(__file__).parent
_repo_path = _Path(_tests_path).parent.parent

# _default_configs_path = _join(_repo_path, "lyc_pyutils_default_configs")
# _default_test_data_path = _join(_default_configs_path, "test_data")

_test_data_path = _join(_repo_path, ".lyc_pyutils_test_data")
_log_loc = _join(_test_data_path, "log.txt")


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


class TestFuncThread(_BaseCase):
    """Tests for the FuncThread class."""

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

        def say_hello(to_name):
            to_name = str(to_name)

            result = f"Hello {to_name}!"
            return result

        fthread = _LYCFuncThread(target=say_hello, args=["world"])
        fthread.start()
        fthread_result = fthread.join()

        not_match_info = str(
            f"FuncThread result does not match\n"
            f"Actual: {{}}\n"
            f"Expected: {{}}"
        )

        match_info = str(
            f"FuncThread result matched\n"
            f"Actual and expected: {{}}"
        )

        actual = fthread_result
        expect = "Hello world!"
        self._match_values(actual, expect, not_match_info, match_info)

        self._log_method_end(method_name)


def main():
    """Runs this module as an executable."""
    unittest.main(verbosity=1)


if __name__ == "__main__":
    main()
