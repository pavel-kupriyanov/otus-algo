from ..popcnt import cached_popcnt
from ..utils import Line


def main(args: list[str]) -> list[str]:
    position = int(args[0])
    mask = get_knight_moves(position)
    count = cached_popcnt(mask)
    return [str(count), str(mask)]


def get_knight_moves(position: int) -> int:
    knight = 1 << position
    return (
            (Line.H & Line.G) & (knight << 6 | knight >> 10)
            | Line.H & (knight << 15 | knight >> 17)
            | Line.A & (knight << 17 | knight >> 15)
            | (Line.A & Line.B) & (knight << 10 | knight >> 6)
    )
