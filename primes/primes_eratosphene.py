from math import sqrt


def main(args: list[str]) -> str:
    n = int(args[0])
    result = count_primes(n)
    return str(result)


def count_primes(n: int) -> int:
    all_numbers = list(range(2, n + 1))
    max_number = sqrt(n)
    excludes = set()
    for number in all_numbers:
        if number in excludes:
            continue

        if number <= max_number:
            for i in range(number ** 2, n + 1, number):
                excludes.add(i)

    return len(all_numbers) - len(excludes)
