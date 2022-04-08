"""Batch logging."""

# Copyright 2022 Yucheng Liu. GNU LGPL3 license.
# GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
# GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng

import typing

_IO = typing.IO


def logstr(logs, string=""):
    """Logs a string on the log file objects.

    Args:
        logs: the log file objects
        string: the string to log
    """

    # Part of LYC-PythonUtils
    # Copyright 2022 Yucheng Liu. GNU LGPL3 license.
    # GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
    # GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt

    logs = list(logs)
    string = str(string)

    for log in logs:
        log: _IO
        log.write(string)


def logln(logs, line=""):
    """Logs a line on the log file objects.

    Args:
        logs: the log file objects
        line: the line to log
    """

    # Part of LYC-PythonUtils
    # Copyright 2022 Yucheng Liu. GNU LGPL3 license.
    # GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
    # GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt

    logs = list(logs)
    line = str(line)

    line = line + "\n"

    for log in logs:
        log: _IO
        log.write(line)


def flushlogs(logs):
    """Flushes the logs.

    Args:
        logs: the log file objects
    """

    # Part of LYC-PythonUtils
    # Copyright 2022 Yucheng Liu. GNU LGPL3 license.
    # GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
    # GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt

    logs = list(logs)

    for log in logs:
        log: _IO
        log.flush()
