from functools import wraps


def simple_popcnt(n: int) -> int:
    count = 0

    while n:
        count += n & 1
        n = n >> 1

    return count


def tricky_popcnt(n: int) -> int:
    count = 0

    while n:
        count += 1
        n &= n - 1

    return count


def cached(func):
    cache = [tricky_popcnt(n) for n in range(256)]

    @wraps(func)
    def wrapper(n: int):
        return func(n, cache)

    return wrapper


@cached
def cached_popcnt(n: int, cache: list[int]) -> int:
    count, mask = 0, 255

    while n:
        count += cache[n & mask]
        n = n >> 8

    return count
