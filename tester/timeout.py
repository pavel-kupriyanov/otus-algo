from functools import wraps

import signal


def timeout_deco(seconds=10):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError('Таймаут истек')

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator
