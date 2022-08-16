def main(args: list[str]) -> str:
    result = lucky_tickets(int(args[0]))
    return str(result)


def line(size: int, filler: int = 0) -> list[int]:
    return [filler] * size


def matrix(x: int, y: int, filler: int = 0) -> list[list[int]]:
    return [line(x, filler) for _ in range(y)]


def get_sums(table: list[list[int]]) -> list[int]:
    size = len(table[0])
    sums = line(size)

    for i in range(size):
        for j in range(10):
            sums[i] += table[j][i]

    return sums


def magic_number(n: int) -> int:
    return 9 * n + 1


def lucky_tickets(n: int) -> int:
    table = matrix(magic_number(n), 10)
    sums = line(10, filler=1)

    for i in range(2, n + 1):
        for j in range(10):
            offset = magic_number(i - 1) + j
            table[j][j:offset] = sums

        sums = get_sums(table)

    return sum([s ** 2 for s in sums])
