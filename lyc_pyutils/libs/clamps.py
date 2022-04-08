"""Clamp functions."""

# Copyright 2022 Yucheng Liu. GNU LGPL3 license.
# GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
# GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng


def clamp_float(inval, bound1, bound2):
    """Clamps inval to the range bounded by bounds 1 and 2.

    Performs comparisons in floats.

    Args:
        inval: the input value
        bound1: bound 1
        bound2: bound 2

    Returns:
        result: the result
    """

    # Part of LYC-PythonUtils
    # Copyright 2022 Yucheng Liu. GNU LGPL3 license.
    # GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
    # GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt

    inval = float(inval)
    bound1 = float(bound1)
    bound2 = float(bound2)

    if bound1 < bound2:
        floor = bound1
        ceil = bound2
    else:  # elif bound1 >= bound2:
        floor = bound2
        ceil = bound1
    # end if

    result = inval

    if result < floor:
        result = floor

    if result > ceil:
        result = ceil

    return result


def clamp_int(inval, bound1, bound2):
    """Clamps inval to the range bounded by bounds 1 and 2.

    Performs comparisons in integers.

    Args:
        inval: the input value
        bound1: bound 1
        bound2: bound 2

    Returns:
        result: the result
    """

    # Part of LYC-PythonUtils
    # Copyright 2022 Yucheng Liu. GNU LGPL3 license.
    # GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
    # GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt

    inval = int(inval)
    bound1 = int(bound1)
    bound2 = int(bound2)

    if bound1 < bound2:
        floor = bound1
        ceil = bound2
    else:  # elif bound1 >= bound2:
        floor = bound2
        ceil = bound1
    # end if

    result = inval

    if result < floor:
        result = floor

    if result > ceil:
        result = ceil

    return result
