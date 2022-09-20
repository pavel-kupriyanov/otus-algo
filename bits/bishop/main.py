from ..popcnt import cached_popcnt
from ..utils import intersect, UpwardRightDiagonal, DownRightDiagonal


def main(args: list[str]) -> list[str]:
    position = int(args[0])
    mask = get_bishop_moves(position)
    count = cached_popcnt(mask)
    return [str(count), str(mask)]


def get_bishop_moves(position: int) -> int:
    bishop = 1 << position
    return (intersect(UpwardRightDiagonal.items, bishop) | intersect(DownRightDiagonal.items, bishop)) ^ bishop
