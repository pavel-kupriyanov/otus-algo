from typing import Optional
from .vector import VectorArray


class SpaceArray:

    def __init__(self, max_size: int = 100, space: int = 50):
        self.matrix = [
            VectorArray(max_size)
        ]
        self.actual_sizes = [0]
        self.max_size = max_size
        self.space = space

    def __getitem__(self, index: int):
        row, col = self.map(index)
        return self.matrix[row][col]

    def map(self, index: int) -> tuple[int, int]:
        if index < 0:
            index = max(self.size + index, 0)

        if index > self.size:
            raise IndexError('Такого индекса не существует')

        if index == self.size:
            return len(self.matrix) - 1, self.actual_sizes[-1]

        counter = 0
        for i, size in enumerate(self.actual_sizes):
            if index < size + counter:
                return i, index - counter
            counter += size

        raise IndexError('Такого индекса не существует')

    def rebalance(self, row: int):
        if self.actual_sizes[row] == 0:
            self.matrix.pop(row)
            self.actual_sizes.pop(row)
            return

        line = self.matrix[row]
        if line.size < self.max_size:
            return

        if row == len(self.matrix) -1:
            self.matrix.append(VectorArray(self.max_size))
            self.actual_sizes.append(0)

        while self.actual_sizes[row] > self.space:
            item = line.remove(-1)
            self.actual_sizes[row] -= 1
            self.add_to_row(item, row + 1, 0)

    def add_to_row(self, item, row: int, col: int):
        if self.actual_sizes[row] >= self.max_size:
            self.rebalance(row)

        self.matrix[row].append(item, col)
        self.actual_sizes[row] += 1

    @property
    def size(self):
        return sum(self.actual_sizes)

    def append(self, item, index: Optional[int] = None):
        if index is None:
            row, col = len(self.matrix) - 1, self.actual_sizes[-1]
        else:
            row, col = self.map(index)

        if row == len(self.matrix) - 1 and col >= self.space:
            self.matrix.append(VectorArray(self.max_size))
            self.actual_sizes.append(0)
            col = 0
            row += 1

        self.add_to_row(item, row, col)

    def remove(self, index: int = -1):
        row, col = self.map(index)
        item = self.matrix[row].remove(col)
        self.actual_sizes[row] -= 1
        if self.actual_sizes[row] == 0:
            self.rebalance(row)

        return item