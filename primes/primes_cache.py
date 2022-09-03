from math import sqrt


def main(args: list[str]) -> str:
    n = int(args[0])
    result = count_primes(n)
    return str(result)


def count_primes(n: int) -> int:
    cache = []
    for i in range(2, n + 1):
        if is_prime(i, cache):
            cache.append(i)

    return len(cache)


def is_prime(number: int, cache: list[int]) -> bool:
    if number == 2:
        return True

    max_number = sqrt(number)

    for i in cache:
        if i > max_number:
            break

        if number % i == 0:
            return False

    return True
