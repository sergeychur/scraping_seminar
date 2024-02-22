import time
import threading

class SimpleRateLimiter:
    def __init__(self, rate):
        self._lock = threading.Lock()
        self._delta = 1. / rate
        self._last_called_ts = 0

    def get_delay(self, now=None):
        with self._lock:
            expected_next_call_ts = self._last_called_ts + self._delta
            if now is None:
                now = time.time()
            self._last_called_ts = now
            return max(expected_next_call_ts - now, 0)
