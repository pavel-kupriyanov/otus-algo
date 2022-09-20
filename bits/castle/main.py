from ..popcnt import cached_popcnt
from ..utils import intersect, Vertical, Horizontal


def main(args: list[str]) -> list[str]:
    position = int(args[0])
    mask = get_castle_moves(position)
    count = cached_popcnt(mask)
    return [str(count), str(mask)]


def get_castle_moves(position: int) -> int:
    castle = 1 << position
    return (intersect(Horizontal.items, castle) | intersect(Vertical.items, castle)) ^ castle
