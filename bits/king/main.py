from ..popcnt import cached_popcnt
from ..utils import Line


def main(args: list[str]) -> list[str]:
    position = int(args[0])
    mask = get_king_moves(position)
    count = cached_popcnt(mask)
    return [str(count), str(mask)]


def get_king_moves(position: int) -> int:
    king = 1 << position

    return (
            (king & Line.A & Line.N8) << 7 | (king & Line.N8) << 8 | (king & Line.H & Line.N8) << 9 |
            (king & Line.A) >> 1 | (king & Line.H) << 1 |
            (king & Line.A) >> 9 | king >> 8 | (king & Line.H) >> 7
    )
