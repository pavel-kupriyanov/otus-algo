from ..popcnt import cached_popcnt
from ..utils import Vertical


def main(args: list[str]) -> list[str]:
    position = int(args[0])
    mask = get_knight_moves(position)
    count = cached_popcnt(mask)
    return [str(count), str(mask)]


def get_knight_moves(position: int) -> int:
    knight = 1 << position
    return (
            (Vertical.H & Vertical.G) & (knight << 6 | knight >> 10)
            | Vertical.H & (knight << 15 | knight >> 17)
            | Vertical.A & (knight << 17 | knight >> 15)
            | (Vertical.A & Vertical.B) & (knight << 10 | knight >> 6)
    )
