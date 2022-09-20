MAX = 0xffffffffffffffff


def not_(num: int) -> int:
    """
    Без сторонних библиотек int в питоне со знаком и неограничен по длине, поэтому оператор ~ работает не так
    как нужно в рамках задачи
    """
    return (1 << 64) - 1 - num


def intersect(lines: list[int], point: int) -> int:
    """
    Выбирает линию, на которой находится точка из списка линий
    """
    for line in lines:
        if not line & point:
            return not_(line)
    return 0


class UpwardRightDiagonal:
    A1 = 0x7fbfdfeff7fbfdfe

    A2 = 0xbfdfeff7fbfdfeff
    A3 = 0xdfeff7fbfdfeffff
    A4 = 0xeff7fbfdfeffffff
    A5 = 0xf7fbfdfeffffffff
    A6 = 0xfbfdfeffffffffff
    A7 = 0xfdfeffffffffffff

    B1 = 0xff7fbfdfeff7fbfd
    C1 = 0xffff7fbfdfeff7fb
    D1 = 0xffffffff7fbfdfef
    E1 = 0xffffffff7fbfdfef
    F1 = 0xffffffffff7fbfdf
    G1 = 0xffffffffffff7fbf

    items = [A1, A2, A3, A4, A5, A6, A7, B1, C1, D1, E1, F1, G1]


class DownRightDiagonal:
    A8 = 0xfefdfbf7efdfbf7f

    A7 = 0xfffefdfbf7efdfbf
    A6 = 0xfffffefdfbf7efdf
    A5 = 0xfffffffefdfbf7ef
    A4 = 0xfffffffffefdfbf7
    A3 = 0xfffffffffffefdfb
    A2 = 0xfffffffffffffefd

    B8 = 0xfdfbf7efdfbf7fff
    C8 = 0xfbf7efdfbf7fffff
    D8 = 0Xf7efdfbf7fffffff
    E8 = 0xefdfbf7fffffffff
    F8 = 0xdfbf7fffffffffff
    G8 = 0xbf7fffffffffffff

    items = [A8, A7, A6, A5, A4, A3, A2, B8, C8, D8, E8, F8, G8]


class Horizontal:
    N1 = 0xffffffffffffff00
    N2 = 0xffffffffffff00ff
    N3 = 0xffffffffff00ffff
    N4 = 0xffffffff00ffffff
    N5 = 0xffffff00ffffffff
    N6 = 0xffff00ffffffffff
    N7 = 0xff00ffffffffffff
    N8 = 0xffffffffffffff

    items = [N1, N2, N3, N4, N5, N6, N7, N8]


class Vertical:
    A = 0xfefefefefefefefe
    B = 0xfdfdfdfdfdfdfdfd
    C = 0xfbfbfbfbfbfbfbfb
    D = 0xf7f7f7f7f7f7f7f7
    E = 0xefefefefefefefef
    F = 0xdfdfdfdfdfdfdfdf
    G = 0xbfbfbfbfbfbfbfbf
    H = 0x7f7f7f7f7f7f7f7f

    items = [A, B, C, D, E, F, G, H]


class Line:
    A = 0xfefefefefefefefe
    B = 0xfdfdfdfdfdfdfdfd
    C = 0xfbfbfbfbfbfbfbfb
    D = 0xf7f7f7f7f7f7f7f7
    E = 0xefefefefefefefef
    F = 0xdfdfdfdfdfdfdfdf
    G = 0xbfbfbfbfbfbfbfbf
    H = 0x7f7f7f7f7f7f7f7f

    N1 = 0xffffffffffffff00
    N2 = 0xffffffffffff00ff
    N3 = 0xffffffffff00ffff
    N4 = 0xffffffff00ffffff
    N5 = 0xffffff00ffffffff
    N6 = 0xffff00ffffffffff
    N7 = 0xff00ffffffffffff
    N8 = 0xffffffffffffff
