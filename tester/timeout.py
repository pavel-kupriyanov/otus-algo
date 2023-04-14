from functools import wraps
from contextlib import contextmanager
from time import monotonic

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


@contextmanager
def timeout(name):
    timeout_reached = False
    start = monotonic()
    try:
        yield
    except TimeoutError:
        timeout_reached = True

    time = monotonic() - start

    formatted_time = f'{(time * 1000):.0f} ms'
    print(f'{name}: {formatted_time if not timeout_reached else "timeout"}')
