import threading
from collections import defaultdict
from contextlib import contextmanager

class PerKeyLock:
    def __init__(self):
        self._locks = defaultdict(threading.Lock)
        self._registry_lock = threading.Lock()

    def get_lock(self, key):
        with self._registry_lock:
            return self._locks[key]

    @contextmanager
    def acquire(self, key):
        lock = self.get_lock(key)
        lock.acquire()
        try:
            yield
        finally:
            lock.release()

# Global instance
per_key_lock = PerKeyLock()