from decimal import Decimal
from .utils import format_result


def main(args: list[str]) -> str:
    a, n = float(args[0]), int(args[1])
    result = factorization_pow(a, n)
    return format_result(result)


def factorization_pow(a: float, n: int) -> float:
    result = 1
    for power in get_powers2(n):
        result *= pow2(a, power)

    return result


def is_pow2(n: int) -> bool:
    return bool(n and not (n & (n - 1)))


def pow2(a: float, n: int):
    assert is_pow2(n), 'n должно быть степенью 2'
    a_dec = Decimal(a)
    while n > 1:
        a_dec *= a_dec
        n /= 2

    return float(a_dec)


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
