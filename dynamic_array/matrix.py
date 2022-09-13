from typing import Any

from .base import placeholder


class MatrixArray:

    def __init__(self, line_size: int = 100):
        self.matrix = [[placeholder] * line_size]
        self.line_size = line_size
        self.last_line_size = 0

    def __getitem__(self, index):
        row, col = self.map(index)
        result = self.matrix[row][col]
        if result is placeholder:
            raise IndexError('Такого индекса не существует')
        return result

    @property
    def size(self) -> int:
        return self.line_size * (len(self.matrix) - 1) + self.last_line_size

    def map(self, index: int) -> tuple[int, int]:
        return divmod(index, self.line_size)

    def expand(self):
        self.matrix.append([placeholder] * self.line_size)
        self.last_line_size = 0

    def insert(self, index: int, item: Any):
        row, col = self.map(index)
        start_line = self.matrix[row]
        item = insert_to_line_right(start_line, item, col)
        for line in self.matrix[row + 1:]:
            item = insert_to_line_right(line, item, 0)

        self.last_line_size += 1

    def pull(self, index: int):
        row, col = self.map(index)
        item = placeholder
        size = self.last_line_size
        for line in reversed(self.matrix[row + 1::]):
            item = insert_to_line_left(line, item, size - 1)
            size = self.line_size

        changed_line = self.matrix[row]
        removed = changed_line[col]
        changed_line[col:self.line_size - 1] = changed_line[col + 1: self.line_size]
        changed_line[-1] = item

        return removed

    def reduce(self):
        self.matrix.pop()
        self.last_line_size = self.line_size

    def append(self, item, index: int = -1):
        if self.matrix[-1][-1] != placeholder:
            self.expand()

        if index < 0:
            index = max(self.size + 1 + index, 0)

        self.insert(index, item)

    def remove(self, index: int):
        if index < 0:
            index = max(self.size + 1 + index, 0)

        item = self.pull(index)

        if self.last_line_size == 0:
            self.reduce()

        return item


def insert_to_line_right(line: list, item: Any, index: int = 0) -> Any:
    last = line[-1]
    line[index + 1:] = line[index:-1]
    line[index] = item
    return last


def insert_to_line_left(line: list, item: Any, index: int = 0) -> Any:
    first = line[0]
    line[0: index] = line[1: index + 1]
    line[index] = item
    return first
