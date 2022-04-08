"""Executable that tests the timed input utilities."""

# Copyright 2022 Yucheng Liu. GNU LGPL3 license.
# GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
# GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng

import asyncio
import os
import pathlib
# import shutil
import sys
import threading
import time
import typing
import unittest

from asyncio import subprocess
from os import path as ospath

# import lyc_pyutils

_async_run = asyncio.run
# _copytree = shutil.copytree
_create_subprocess_exec = asyncio.create_subprocess_exec
_IO = typing.IO
_join = ospath.join
_makedirs = os.makedirs
_Path = pathlib.Path
_PIPE = subprocess.PIPE
# _rmtree = shutil.rmtree
_sleep = time.sleep
_sysexe = sys.executable
_TestCase = unittest.TestCase
_Thread = threading.Thread

# _LYCTimedInput = lyc_pyutils.TimedInput

_tests_path = _Path(__file__).parent
_repo_path = _Path(_tests_path).parent.parent

# _default_configs_path = _join(_repo_path, "lyc_pyutils_default_configs")
# _default_test_data_path = _join(_default_configs_path, "test_data")

_test_data_path = _join(_repo_path, ".lyc_pyutils_test_data")
_log_loc = _join(_test_data_path, "log.txt")

_timeout = float(10)


def _utf8_enc(str_to_enc):
    str_to_enc = str(str_to_enc)

    result = str_to_enc.encode("utf-8", "replace")
    return result


def _utf8_dec(bytes_to_dec):
    bytes_to_dec = bytes(bytes_to_dec)

    result = bytes_to_dec.decode("utf-8", "replace")
    return result


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


async def _async_run_sysexe(pystr, instr="", in_delay=None):
    """Returns outstr, errstr, exitcode."""
    pystr = str(pystr)
    instr = str(instr)

    if in_delay is not None:
        in_delay = float(in_delay)

        if in_delay < 0:
            in_delay *= -1

    else:
        in_delay = None
    # end if

    subproc = await _create_subprocess_exec(_sysexe, "-c", pystr, stdin=_PIPE, stdout=_PIPE, stderr=_PIPE)

    if in_delay is not None:
        _sleep(in_delay)

    inbytes = _utf8_enc(instr)
    outbytes, errbytes = await subproc.communicate(inbytes)
    exitcode = await subproc.wait()

    outstr = _utf8_dec(outbytes)
    outstr = _fix_newline_format(outstr)
    errstr = _utf8_dec(errbytes)
    errstr = _fix_newline_format(errstr)

    result = outstr, errstr, exitcode
    return result


def _run_sysexe(pystr, instr="", in_delay=None):
    """Returns outstr, errstr, exitcode."""
    outstr, errstr, exitcode = _async_run(_async_run_sysexe(pystr, instr, in_delay))
    result = outstr, errstr, exitcode
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


class _FuncThread(_Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        """Inits self with the given args.

        Args:
            group: Group.
            target: Target.
            name: Name.
            args: Arguments
            kwargs: Keyword arguments.
            *: Positional-keyword and keyword-only arguments separator.
            daemon: Daemon thread switch.
        """
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._result = None

    def run(self):
        """Runs the thread."""
        # Adopted from CPython standard library threading source code
        # Ref: https://github.com/python/cpython/blob/main/Lib/threading.py
        try:
            if self._target is not None:
                self._result = self._target(*self._args, **self._kwargs)
        finally:
            # Avoid reference cycles
            del self._target
            del self._args
            del self._kwargs

    def join(self, timeout=None):
        """Joins the thread.

        Args:
            timeout: Timeout length in seconds.

        Returns:
            self._result: Result. Return value.
        """
        super().join(timeout=timeout)
        return self._result


class TestTimedInput(_BaseCase):
    """Tests for the TimedInput class."""

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

        pystr = fr"""

import lyc_pyutils

_TimedInput = lyc_pyutils.TimedInput

_timeout = float(5)

_tinput = _TimedInput()
_instr = _tinput.take(_timeout)

if _instr is not None:
    print(_instr)

        """

        pystr = pystr.strip()
        pystr = pystr + "\n"
        instr = "Hello world!\n"
        fthread = _FuncThread(target=_run_sysexe, args=[pystr, instr])
        fthread.start()
        outstr, _, exitcode = fthread.join(_timeout)

        fail_msg = f"TimedInput results in an unexpected exit code: {exitcode}"
        success_msg = f"TimedInput results in the expected exit code: {exitcode}"
        self.assertTrue(exitcode == 0, fail_msg)
        self._logln(success_msg)

        not_match_info = str(
            f"TimedInput result does not match\n"
            f"Actual: {{}}\n"
            f"Expected: {{}}"
        )

        match_info = str(
            f"TimedInput result matched\n"
            f"Actual and expected: {{}}"
        )

        actual = str(outstr)
        actual = actual.strip()
        expect = instr.strip()
        self._match_values(actual, expect, not_match_info, match_info)

        self._log_method_end(method_name)

    def test_timeout(self):
        """Tests the case in which the timed input is timed out."""
        method_name = self.test_norm.__name__
        self._log_method_start(method_name)

        pystr = fr"""

import lyc_pyutils

_TimedInput = lyc_pyutils.TimedInput

_timeout = 1e-6  # 1 micro-second

_tinput = _TimedInput()
_instr = _tinput.take(_timeout)

if _instr is not None:
    print(_instr)

        """

        pystr = pystr.strip()
        pystr = pystr + "\n"
        instr = ""
        in_delay = 0.1
        fthread = _FuncThread(target=_run_sysexe, args=[pystr, instr, in_delay])
        fthread.start()
        outstr, _, exitcode = fthread.join(_timeout)

        fail_msg = f"TimedInput results in an unexpected exit code: {exitcode}"
        success_msg = f"TimedInput results in the expected exit code: {exitcode}"
        self.assertTrue(exitcode == 0, fail_msg)
        self._logln(success_msg)

        not_match_info = str(
            f"TimedInput result does not match\n"
            f"Actual: {{}}\n"
            f"Expected: {{}}"
        )

        match_info = str(
            f"TimedInput result matched\n"
            f"Actual and expected: {{}}"
        )

        actual = str(outstr)
        actual = actual.strip()
        expect = ""
        self._match_values(_dquote_repr(actual), _dquote_repr(expect), not_match_info, match_info)

        self._log_method_end(method_name)


def main():
    """Runs this module as an executable."""
    unittest.main(verbosity=1)


if __name__ == "__main__":
    main()
