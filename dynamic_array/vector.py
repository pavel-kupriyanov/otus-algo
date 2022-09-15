from .base import BaseArray, placeholder


class VectorArray(BaseArray):

    def __init__(self, vector_size: int = 10):
        super().__init__()
        self.vector_size = vector_size
        self.array = [placeholder] * self.vector_size
        self._size = 0

    def __repr__(self):
        return repr(self.array)

    @property
    def size(self):
        return self._size

    def expand(self):
        self.array = [*self.array, *([placeholder] * self.vector_size)]

    def reduce(self):
        self.array = self.array[0:self.size - 1]

    def append(self, item, index: int = -1):
        if self.size == len(self.array):
            self.expand()

        self._size += 1
        super().append(item, index)

    def remove(self, index: int):
        removed = super().remove(index)
        self.reduce()
        self._size -= 1
        return removed
