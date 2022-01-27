"""Executable that tests the batch log utilities."""

# Copyright 2022 Yucheng Liu. GNU GPL3 license.
# GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt
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

_lyc_logstr = lyc_pyutils.logstr
_lyc_logln = lyc_pyutils.logln
_lyc_flushlogs = lyc_pyutils.flushlogs

_tests_path = _Path(__file__).parent
_repo_path = _Path(_tests_path).parent.parent

_default_configs_path = _join(_repo_path, "lyc_pyutils_default_configs")
_default_test_data_path = _join(_default_configs_path, "test_data")
_default_test_batchlog_path = _join(_default_test_data_path, "test_batchlog")

_test_data_path = _join(_repo_path, ".lyc_pyutils_test_data")
_log_loc = _join(_test_data_path, "log.txt")
_test_batchlog_path = _join(_test_data_path, "test_batchlog")


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


class TestLogstr(_BaseCase):
    """Tests for the logstr function."""

    def __init__(self, methodName):
        """Initializes self with the given args."""
        super().__init__(methodName)

        self._test_log_locs = [
            _join(_test_batchlog_path, "log1.txt"),
            _join(_test_batchlog_path, "log2.txt"),
            _join(_test_batchlog_path, "log3.txt"),
            _join(_test_batchlog_path, "log4.txt")
        ]

        self._test_logs: list[_IO] = []

    def setUp(self):
        """Sets up before the tests."""
        super().setUp()

        _rmtree(_test_batchlog_path, ignore_errors=True)
        _copytree(_default_test_batchlog_path, _test_batchlog_path)

        for loc in self._test_log_locs:
            file = open(loc, "a+")
            self._test_logs.append(file)

    def tearDown(self):
        """Tears down after the tests."""
        super().tearDown()

        for file in self._test_logs:
            file.close()

        _rmtree(_test_batchlog_path, ignore_errors=True)

    def test_norm(self):
        """Tests the normal use case."""
        method_name = self.test_norm.__name__
        self._log_method_start(method_name)

        lines_to_log = str(
            f"[ logstr test ]\n"
            f"[ test logstr ]\n"
        )

        _lyc_logstr(self._test_logs, lines_to_log)

        for log in self._test_logs:
            log.flush()

        log_lines = [
            str(
                f"log1\n"
                f"{lines_to_log}"
            ),
            str(
                f"log2\n"
                f"{lines_to_log}"
            ),
            lines_to_log,
            lines_to_log
        ]

        match_info = str(
            f"Log contents matches\n"
            f"Log file location: {{}}\n"
            f"Log and supposed contents:\n"
            f"{{}}"
        )

        not_match_info = str(
            f"Log contents do not match\n"
            f"Log file location: {{}}\n"
            f"Log contents:\n"
            f"{{}}\n"
            f"Supposed contents:\n"
            f"{{}}"
        )

        for idx in range(len(self._test_log_locs)):
            loc = self._test_log_locs[idx]

            file = open(loc, "r")
            contents = file.read()
            file.close()

            contents = _fix_newline_format(contents)
            lines = log_lines[idx]
            fail_msg = not_match_info.format(loc, _dquote_repr(contents), _dquote_repr(lines))
            self.assertTrue(contents == lines, fail_msg)

            success_msg = match_info.format(loc, _dquote_repr(contents))
            self._logln(success_msg)
        # end for

        self._log_method_end(method_name)


class TestLogln(_BaseCase):
    """Tests for the logln function."""

    def __init__(self, methodName):
        """Initializes self with the given args."""
        super().__init__(methodName)

        self._test_log_locs = [
            _join(_test_batchlog_path, "log1.txt"),
            _join(_test_batchlog_path, "log2.txt"),
            _join(_test_batchlog_path, "log3.txt"),
            _join(_test_batchlog_path, "log4.txt")
        ]

        self._test_logs: list[_IO] = []

    def setUp(self):
        """Sets up before the tests."""
        super().setUp()

        _rmtree(_test_batchlog_path, ignore_errors=True)
        _copytree(_default_test_batchlog_path, _test_batchlog_path)

        for loc in self._test_log_locs:
            file = open(loc, "a+")
            self._test_logs.append(file)

    def tearDown(self):
        """Tears down after the tests."""
        super().tearDown()

        for file in self._test_logs:
            file.close()

        _rmtree(_test_batchlog_path, ignore_errors=True)

    def test_norm(self):
        """Tests the normal use case."""
        method_name = self.test_norm.__name__
        self._log_method_start(method_name)

        contents_to_log = str(
            f"[ logln test ]\n"
            f"[ test logln ]"
        )

        _lyc_logln(self._test_logs, contents_to_log)

        for log in self._test_logs:
            log.flush()

        log_lines = [
            str(
                f"log1\n"
                f"{contents_to_log}\n"
            ),
            str(
                f"log2\n"
                f"{contents_to_log}\n"
            ),
            f"{contents_to_log}\n",
            f"{contents_to_log}\n"
        ]

        match_info = str(
            f"Log contents matches\n"
            f"Log file location: {{}}\n"
            f"Log and supposed contents:\n"
            f"{{}}"
        )

        not_match_info = str(
            f"Log contents do not match\n"
            f"Log file location: {{}}\n"
            f"Log contents:\n"
            f"{{}}\n"
            f"Supposed contents:\n"
            f"{{}}"
        )

        for idx in range(len(self._test_log_locs)):
            loc = self._test_log_locs[idx]

            file = open(loc, "r")
            contents = file.read()
            file.close()

            contents = _fix_newline_format(contents)
            lines = log_lines[idx]
            fail_msg = not_match_info.format(loc, _dquote_repr(contents), _dquote_repr(lines))
            self.assertTrue(contents == lines, fail_msg)

            success_msg = match_info.format(loc, _dquote_repr(contents))
            self._logln(success_msg)
        # end for

        self._log_method_end(method_name)


class TestFlushlogs(_BaseCase):
    """Tests for the flushlogs function."""

    def __init__(self, methodName):
        """Initializes self with the given args."""
        super().__init__(methodName)

        self._test_log_locs = [
            _join(_test_batchlog_path, "log1.txt"),
            _join(_test_batchlog_path, "log2.txt"),
            _join(_test_batchlog_path, "log3.txt"),
            _join(_test_batchlog_path, "log4.txt")
        ]

        self._test_logs: list[_IO] = []

    def setUp(self):
        """Sets up before the tests."""
        super().setUp()

        _rmtree(_test_batchlog_path, ignore_errors=True)
        _copytree(_default_test_batchlog_path, _test_batchlog_path)

        for loc in self._test_log_locs:
            file = open(loc, "a+")
            self._test_logs.append(file)

    def tearDown(self):
        """Tears down after the tests."""
        super().tearDown()

        for file in self._test_logs:
            file.close()

        _rmtree(_test_batchlog_path, ignore_errors=True)

    def test_norm(self):
        """Tests the normal use case."""
        method_name = self.test_norm.__name__
        self._log_method_start(method_name)

        lines_to_log = str(
            f"[ flushlogs test ]\n"
            f"[ test flushlogs ]\n"
        )

        for log in self._test_logs:
            log.write(lines_to_log)

        _lyc_flushlogs(self._test_logs)

        log_lines = [
            str(
                f"log1\n"
                f"{lines_to_log}"
            ),
            str(
                f"log2\n"
                f"{lines_to_log}"
            ),
            lines_to_log,
            lines_to_log
        ]

        match_info = str(
            f"Log contents matches\n"
            f"Log file location: {{}}\n"
            f"Log and supposed contents:\n"
            f"{{}}"
        )

        not_match_info = str(
            f"Log contents do not match\n"
            f"Log file location: {{}}\n"
            f"Log contents:\n"
            f"{{}}\n"
            f"Supposed contents:\n"
            f"{{}}"
        )

        for idx in range(len(self._test_log_locs)):
            loc = self._test_log_locs[idx]

            file = open(loc, "r")
            contents = file.read()
            file.close()

            contents = _fix_newline_format(contents)
            lines = log_lines[idx]
            fail_msg = not_match_info.format(loc, _dquote_repr(contents), _dquote_repr(lines))
            self.assertTrue(contents == lines, fail_msg)

            success_msg = match_info.format(loc, _dquote_repr(contents))
            self._logln(success_msg)
        # end for

        self._log_method_end(method_name)


def main():
    """Runs this module as an executable."""
    unittest.main(verbosity=1)


if __name__ == "__main__":
    main()
