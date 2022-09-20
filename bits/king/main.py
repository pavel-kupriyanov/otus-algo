from ..popcnt import cached_popcnt
from ..utils import Horizontal, Vertical


def main(args: list[str]) -> list[str]:
    position = int(args[0])
    mask = get_king_moves(position)
    count = cached_popcnt(mask)
    return [str(count), str(mask)]


def get_king_moves(position: int) -> int:
    king = 1 << position

    return (
            (king & Vertical.A & Horizontal.N8) << 7 |
            (king & Horizontal.N8) << 8 |
            (king & Vertical.H & Horizontal.N8) << 9 |

            (king & Vertical.A) >> 1 |
            (king & Vertical.H) << 1 |

            (king & Vertical.A) >> 9 |
            king >> 8 |
            (king & Vertical.H) >> 7
    )
