"""Timed input."""

# Initially added by: liu-yucheng
# Last updated by: liu-yucheng

import asyncio
import sys
import threading


class TimedInput:
    """Timed input.

    Python "native" and platform independent timed input command prompt.
    """

    def __init__(self):
        """Inits self with the given args."""
        self._input_str = None
        self._subproc_code = r"""input_str = input()
print(input_str)
"""
        self._subproc = None

    async def _run_subproc(self):
        self._subproc = await asyncio.create_subprocess_exec(
            sys.executable, "-c", self._subproc_code, stdin=sys.stdin, stdout=asyncio.subprocess.PIPE
        )
        data = await self._subproc.stdout.readline()
        self._input_str = data.decode("utf-8", "replace").rstrip()
        await self._subproc.wait()

    def _take(self):
        self._subproc = None
        asyncio.run(self._run_subproc())

    def take(self, timeout=5.0):
        """Takes and returns a string from user input with a given timeout.

        Args:
            timeout: the timeout period length in seconds

        Returns:
            self._input_str: the taken input string, or None if there is a timeout
        """
        timeout = float(timeout)
        self._input_str = None
        thread = threading.Thread(target=self._take)
        thread.start()
        thread.join(timeout)
        if self._input_str is None and self._subproc is not None:
            self._subproc.terminate()
        return self._input_str
