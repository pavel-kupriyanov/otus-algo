def main(args: list[str]) -> str:
    return str(fibo(int(args[0])))


def fibo(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibo(n - 1) + fibo(n - 2)
