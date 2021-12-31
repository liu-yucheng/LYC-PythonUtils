"""Functional thread."""

# Initially added by: liu-yucheng
# Last updated by: liu-yucheng

import threading

_Thread = threading.Thread


class FuncThread(_Thread):
    """Functional thread.

    A Python standard library thread with return values.
    """

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        """Inits self with the given args.

        Args:
            group: Group.
            target: Target.
            name: Name.
            args: Arguments.
            kwargs: Keyword arguments.
            *: Variable arguments.
            daemon: Daemon thread switch.
        """
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._result = None

    def run(self):
        """Runs the thread."""
        # Adopted from CPython standard library threading source code.
        # Ref: https://github.com/python/cpython/blob/main/Lib/threading.py
        try:
            if self._target is not None:
                self._result = self._target(*self._args, **self._kwargs)
        finally:
            # Avoid reference cycles.
            del self._target
            del self._args
            del self._kwargs

    def join(self, timeout=None):
        """Joins the thread.

        Returns:
            self._result: Result.
        """
        super().join(timeout=timeout)
        return self._result
