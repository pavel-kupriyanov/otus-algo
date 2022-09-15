from .base import BaseArray, placeholder


class SingleArray(BaseArray):

    def expand(self):
        self.array = [*self.array, placeholder]

    def reduce(self):
        self.array = self.array[0:self.size - 1]

    def append(self, item, index: int = -1):
        self.expand()
        super().append(item, index)

    def remove(self, index: int):
        removed = super().remove(index)
        self.reduce()
        return removed
