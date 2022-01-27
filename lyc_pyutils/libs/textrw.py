"""Text reading and writing."""

# Copyright 2022 Yucheng Liu. GNU GPL3 license.
# GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng

import typing

_IO = typing.IO


def load_text(from_file):
    """Loads the data from a file to a string and returns the string.

    Args:
        from_file: the file location

    Returns:
        result: the text
    """

    # Part of LYC-PythonUtils
    # Copyright 2022 Yucheng Liu. GNU GPL3 license.
    # GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt

    from_file = str(from_file)

    file: _IO = open(from_file, "r")
    text = file.read()
    file.close()

    result = text
    result = str(result)
    return result


def save_text(from_str, to_file):
    """Saves a string to a file.

    Args:
        from_str: the string
        to_file: the file location
    """

    # Part of LYC-PythonUtils
    # Copyright 2022 Yucheng Liu. GNU GPL3 license.
    # GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt

    from_str = str(from_str)
    to_file = str(to_file)

    file: _IO = open(to_file, "w+")
    file.write(from_str)
    file.close()
