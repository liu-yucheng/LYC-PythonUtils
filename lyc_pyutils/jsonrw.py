"""JSON reading and writing."""

# Copyright 2022 Yucheng Liu. GNU GPL3 license.
# GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng

import json

_jsonload = json.load
_jsondump = json.dump


def load_json(from_file):
    """Loads the data from a JSON file to a dict and returns the dict.

    Args:
        from_file: the JSON file location

    Returns:
        result: the dict
    """

    # Part of LYC-PythonUtils
    # Copyright 2022 Yucheng Liu. GNU GPL3 license.
    # GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt

    from_file = str(from_file)

    file = open(from_file, "r")
    to_dict = _jsonload(file)
    file.close()

    result = to_dict
    result = dict(result)
    return result


def save_json(from_dict, to_file):
    """Saves the data from a dict to a JSON file.

    Args:
        from_dict: the dict object
        to_file: the JSON file location
    """

    # Part of LYC-PythonUtils
    # Copyright 2022 Yucheng Liu. GNU GPL3 license.
    # GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt

    from_dict = dict(from_dict)
    to_file = str(to_file)

    file = open(to_file, "w+")
    _jsondump(from_dict, file, indent=4)
    file.close()
