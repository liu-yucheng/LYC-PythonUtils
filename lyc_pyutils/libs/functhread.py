"""Functional thread."""

# Copyright 2022 Yucheng Liu. GNU LGPL3 license.
# GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
# GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng

import threading

_Thread = threading.Thread


class FuncThread(_Thread):
    """Functional thread.

    A Python standard library thread with return values.
    """

    # Part of LYC-PythonUtils
    # Copyright 2022 Yucheng Liu. GNU LGPL3 license.
    # GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
    # GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        """Inits self with the given args.

        Args:
            group: Group.
            target: Target.
            name: Name.
            args: Arguments.
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

        # Based on CPython standard library threading source code.
        # Ref: https://github.com/python/cpython/blob/main/Lib/threading.py

        try:
            if self._target is not None:
                self._result = self._target(*self._args, **self._kwargs)
        finally:
            # Avoid reference cycles.
            del self._target
            del self._args
            del self._kwargs
        # end try

    def join(self, timeout=None):
        """Joins the thread.

        Returns:
            self._result: Result.
        """
        super().join(timeout=timeout)
        return self._result
