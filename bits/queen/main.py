from ..popcnt import cached_popcnt
from ..utils import intersect, Vertical, Horizontal, UpwardRightDiagonal, DownRightDiagonal


def main(args: list[str]) -> list[str]:
    position = int(args[0])
    mask = get_queen_moves(position)
    count = cached_popcnt(mask)
    return [str(count), str(mask)]


def get_queen_moves(position: int) -> int:
    queen = 1 << position
    straights = intersect(Horizontal.items, queen) | intersect(Vertical.items, queen)
    diagonals = intersect(UpwardRightDiagonal.items, queen) | intersect(DownRightDiagonal.items, queen)
    return (straights | diagonals) ^ queen
