"""Cross-platform advisory file locking.

fcntl.flock is POSIX-only and silently does nothing on Windows in the
scripts this was lifted from (dataforseo_costs.py, moz_api.py both had a
bare `except ImportError: fcntl = None` fallback with no real lock),
which lets two concurrent runs race on the same ledger/cache file. This
gives both platforms a real lock via the same `with locked(f):` call.
"""

from __future__ import annotations

import sys
from contextlib import contextmanager

if sys.platform == "win32":
    import msvcrt

    @contextmanager
    def locked(file_obj, exclusive: bool = True):
        # msvcrt.locking locks a byte range starting at the file's current
        # position, and needs at least one byte to exist there to lock.
        file_obj.seek(0, 2)  # end of file
        if file_obj.tell() == 0:
            newline = b"\n" if "b" in getattr(file_obj, "mode", "") else "\n"
            file_obj.write(newline)
            file_obj.flush()
        file_obj.seek(0)
        msvcrt.locking(file_obj.fileno(), msvcrt.LK_LOCK, 1)
        try:
            yield
        finally:
            file_obj.seek(0)
            msvcrt.locking(file_obj.fileno(), msvcrt.LK_UNLCK, 1)

else:
    import fcntl

    @contextmanager
    def locked(file_obj, exclusive: bool = True):
        fcntl.flock(file_obj, fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH)
        try:
            yield
        finally:
            fcntl.flock(file_obj, fcntl.LOCK_UN)
