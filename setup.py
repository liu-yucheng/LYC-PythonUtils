"""Package setup executable module.

When called by a package manager (pip/conda/python), this executable informs the package manager about how to install
the source directory as a package. The "entry_points" parameter of the setup function specifies the function to call
when the user enters the corresponding command on the command line. The "entry_points" elements takes the form of
"command = package.module.submodule. ... .submodule:function"
"""

# Initially added by: liu-yucheng
# Last updated by: liu-yucheng

import setuptools


def main():
    setuptools.setup(
        name="lyc-pyutils",
        version="0.2.0",
        description="LYC Python Utilities",
        author="Yucheng Liu",
        packages=setuptools.find_packages(),
        entry_points={
            "console_scripts": []
        }
        # test_suite="tests"
    )


if __name__ == "__main__":
    main()
