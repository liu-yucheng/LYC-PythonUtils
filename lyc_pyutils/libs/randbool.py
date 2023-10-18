"""Random boolean."""

# Copyright 2022-2023 Yucheng Liu. GNU LGPL3 license.
# GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
# GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng

import random

_randint = random.randint


def rand_bool():
    """Produce a random boolean value.

    This is like flipping a fair coin.

    Returns:
        result: the random boolean
    """

    # Part of LYC-PythonUtils
    # Copyright 2022-2023 Yucheng Liu. GNU LGPL3 license.
    # GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
    # GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt

    result = bool(_randint(0, 1))
    return result
