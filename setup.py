"""Package setup executable.

To be called by a package manager (pip or conda or others).
NOT supposed to be executed directly (via python or py).
Tells the package manager the way to install the source directory as a package.
The "entry_points" parameter of the setup function specifies the function to call when the user enters the
    corresponding command via the command line.
"""

# Copyright 2022 Yucheng Liu. GNU LGPL3 license.
# GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
# GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng

import setuptools

_find_packages = setuptools.find_packages
_setup = setuptools.setup


def main():
    _setup(
        name="lyc-pyutils",
        version="1.1.4",
        description="LYC's personal Python utilities.",
        author="Yucheng Liu",
        packages=_find_packages(),
        entry_points={
            "console_scripts": []
        }  # ,
        # test_suite="lyc_pyutils.tests"
    )


if __name__ == "__main__":
    main()
