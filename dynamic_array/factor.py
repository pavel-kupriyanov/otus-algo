from .base import BaseArray, placeholder


class FactorArray(BaseArray):

    def __init__(self):
        super().__init__()
        self.array = [placeholder]
        self._size = 0

    @property
    def size(self):
        return self._size

    def expand(self):
        factor = [placeholder] * max(self.size, 1)
        self.array = [*self.array, *factor]

    def reduce(self):
        self.array = self.array[0:self.size - 1]

    def append(self, item, index: int = -1):
        if self.array[-1] != placeholder:
            self.expand()

        self._size += 1
        super().append(item, index)

    def remove(self, index: int):
        super().remove(index)
        self.reduce()
        self._size -= 1
