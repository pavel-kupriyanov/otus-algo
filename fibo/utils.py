from typing import Any


def is_pow2(n: int) -> bool:
    return bool(n and not (n & (n - 1)))


def pow2(matrix: Any, n: int) -> Any:
    assert is_pow2(n), 'n должно быть степенью 2'
    while n > 1:
        matrix *= matrix
        n /= 2

    return matrix


def get_powers2(n: int):
    if n % 2 == 1:
        yield 1
        n -= 1

    count = 0
    while n > 1:
        n //= 2
        count += 1

        if n % 2 == 1:
            yield 2 ** count
