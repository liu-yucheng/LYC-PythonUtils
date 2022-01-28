"""Executable that tests the batch log utilities."""

# Copyright 2022 Yucheng Liu. GNU GPL3 license.
# GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng

import json
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
_jsonload = json.load
_jsonloads = json.loads
_makedirs = os.makedirs
_Path = pathlib.Path
_rmtree = shutil.rmtree
_TestCase = unittest.TestCase

_lyc_load_json = lyc_pyutils.load_json
_lyc_save_json = lyc_pyutils.save_json
_lyc_load_json_str = lyc_pyutils.load_json_str
_lyc_save_json_str = lyc_pyutils.save_json_str

_tests_path = _Path(__file__).parent
_repo_path = _Path(_tests_path).parent.parent

_default_configs_path = _join(_repo_path, "lyc_pyutils_default_configs")
_default_test_data_path = _join(_default_configs_path, "test_data")
_default_test_jsonrw_path = _join(_default_test_data_path, "test_jsonrw")

_test_data_path = _join(_repo_path, ".lyc_pyutils_test_data")
_log_loc = _join(_test_data_path, "log.txt")
_test_jsonrw_path = _join(_test_data_path, "test_jsonrw")


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


class TestLoadJSON(_BaseCase):
    """Tests for the load_json function."""

    def __init__(self, methodName):
        """Initializes self with the given args."""
        super().__init__(methodName)

        self._cfg1_loc = None

    def setUp(self):
        """Sets up before the tests."""
        super().setUp()

        _rmtree(_test_jsonrw_path, ignore_errors=True)
        _copytree(_default_test_jsonrw_path, _test_jsonrw_path)

        self._cfg1_loc = _join(_test_jsonrw_path, "config1.json")

    def tearDown(self):
        """Tears down after the tests."""
        super().tearDown()

        _rmtree(_test_jsonrw_path, ignore_errors=True)

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

        cfg1 = _lyc_load_json(self._cfg1_loc)

        not_match_info = str(
            f"load_json result does not match\n"
            f"Actual: {{}}\n"
            f"Expected: {{}}"
        )

        match_info = str(
            f"load_json result matched\n"
            f"Actual and expected: {{}}"
        )

        actual = cfg1["config"]
        expect = "config1"
        self._match_values(actual, expect, not_match_info, match_info)

        actual = cfg1["test"]
        expect = "jsonrw"
        self._match_values(actual, expect, not_match_info, match_info)

        actual = cfg1["jsonrw"]
        expect = "test"
        self._match_values(actual, expect, not_match_info, match_info)

        self._log_method_end(method_name)


class TestSaveJSON(_BaseCase):
    """Tests for the save_json function."""

    def __init__(self, methodName):
        """Initializes self with the given args."""
        super().__init__(methodName)

        self._cfg2_loc = None

    def setUp(self):
        """Sets up before the tests."""
        super().setUp()

        _rmtree(_test_jsonrw_path, ignore_errors=True)
        _copytree(_default_test_jsonrw_path, _test_jsonrw_path)

        self._cfg2_loc = _join(_test_jsonrw_path, "config2.json")

    def tearDown(self):
        """Tears down after the tests."""
        super().tearDown()

        _rmtree(_test_jsonrw_path, ignore_errors=True)

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

        cfg2 = {
            "config": "config2",
            "test": "jsonrw",
            "jsonrw": "test"
        }

        _lyc_save_json(cfg2, self._cfg2_loc)

        file: _IO = open(self._cfg2_loc, "r")
        saved_cfg2 = _jsonload(file)
        file.close()

        saved_cfg2 = dict(saved_cfg2)

        not_match_info = str(
            f"save_json result does not match\n"
            f"Actual: {{}}\n"
            f"Expected: {{}}"
        )

        match_info = str(
            f"save_json result matched\n"
            f"Actual and expected: {{}}"
        )

        actual = saved_cfg2["config"]
        expect = cfg2["config"]
        self._match_values(actual, expect, not_match_info, match_info)

        actual = saved_cfg2["test"]
        expect = cfg2["test"]
        self._match_values(actual, expect, not_match_info, match_info)

        actual = saved_cfg2["jsonrw"]
        expect = cfg2["jsonrw"]
        self._match_values(actual, expect, not_match_info, match_info)

        self._log_method_end(method_name)


class TestLoadJSONStr(_BaseCase):
    """Tests for the load_json_str function."""

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

        cfg3_str = fr"""

{{
    "config": "config3",
    "test": "jsonrw",
    "jsonrw": "test"
}}

        """
        cfg3_str = cfg3_str.strip()

        cfg3 = _lyc_load_json_str(cfg3_str)

        not_match_info = str(
            f"load_json_str result does not match\n"
            f"Actual: {{}}\n"
            f"Expected: {{}}"
        )

        match_info = str(
            f"load_json_str result matched\n"
            f"Actual and expected: {{}}"
        )

        actual = cfg3["config"]
        expect = "config3"
        self._match_values(actual, expect, not_match_info, match_info)

        actual = cfg3["test"]
        expect = "jsonrw"
        self._match_values(actual, expect, not_match_info, match_info)

        actual = cfg3["jsonrw"]
        expect = "test"
        self._match_values(actual, expect, not_match_info, match_info)

        self._log_method_end(method_name)


class TestSaveJSONStr(_BaseCase):
    """Tests for the save_json_str function."""

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

        cfg3 = {
            "config": "config3",
            "test": "jsonrw",
            "jsonrw": "test"
        }

        cfg3_str = _lyc_save_json_str(cfg3)

        not_match_info = str(
            f"save_json_str result does not match\n"
            f"Actual: {{}}\n"
            f"Expected: {{}}"
        )

        match_info = str(
            f"save_json_str result matched\n"
            f"Actual and expected: {{}}"
        )

        actual = cfg3_str

        expect = fr"""

{{
    "config": "config3",
    "test": "jsonrw",
    "jsonrw": "test"
}}

        """
        expect = expect.strip()

        self._match_values(actual, expect, not_match_info, match_info)

        self._log_method_end(method_name)


def main():
    """Runs this module as an executable."""
    unittest.main(verbosity=1)


if __name__ == "__main__":
    main()
