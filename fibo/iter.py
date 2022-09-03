def main(args: list[str]) -> str:
    return str(fibo(int(args[0])))


def fibo(n: int) -> int:
    if n == 0:
        return 0

    f_last, f_next = 0, 1

    for i in range(2, n + 1):
        f_last, f_next = f_next, f_next + f_last

    return f_next
