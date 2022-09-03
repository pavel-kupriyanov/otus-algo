from .utils import get_powers2, pow2


def main(args: list[str]) -> str:
    return str(fibo(int(args[0])))


class Matrix2D:

    def __init__(
            self,
            matrix: tuple[
                tuple[int, int],
                tuple[int, int]
            ]
    ):
        self.matrix = matrix

    def __repr__(self):
        return repr(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def __mul__(self, other: 'Matrix2D') -> 'Matrix2D':
        a00 = self[0][0] * other[0][0] + self[0][1] * other[1][0]
        a10 = self[0][0] * other[0][1] + self[0][1] * other[1][1]
        a01 = self[1][0] * other[0][0] + self[1][1] * other[1][0]
        a11 = self[1][0] * other[0][1] + self[1][1] * other[1][1]
        return Matrix2D((
            (a00, a01),
            (a10, a11)
        ))


def fibo(n: int) -> int:
    if n == 0:
        return 0

    base = Matrix2D((
        (1, 0),
        (0, 1)
    ))
    matrix = Matrix2D((
        (1, 1),
        (1, 0)
    ))
    for power in get_powers2(n - 1):
        base *= pow2(matrix, power)

    return base[0][0]
