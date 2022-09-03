def main(args: list[str]) -> str:
    n = int(args[0])
    result = count_primes(n)
    return str(result)


def count_primes(n: int) -> int:
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count


def is_prime(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False

    return True
