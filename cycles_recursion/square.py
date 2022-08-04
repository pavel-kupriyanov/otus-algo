WIDTH = 25
HEIGHT = 25

symbols = {True: '#', False: '.'}


def draw_square(square: list[list[bool]]):
    for line in square:
        print(" ".join([symbols[value] for value in line]))


def main(height=HEIGHT, width=WIDTH):
    print('Введи выражение (например - "x > y")')
    expression = input('Выражение: ')

    square = [[False] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            square[y][x] = bool(eval(expression))

    draw_square(square)


if __name__ == '__main__':
    main()
