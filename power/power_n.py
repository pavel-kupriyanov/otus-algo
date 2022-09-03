from .utils import format_result


def main(args: list[str]) -> str:
    a, n = float(args[0]), int(args[1])
    result = simple_pow(a, n)
    return format_result(result)


def simple_pow(a: float, n: int) -> float:
    result = 1
    for i in range(n):
        result *= a

    return result
