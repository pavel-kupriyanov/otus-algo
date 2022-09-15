placeholder = object()


class BaseArray:

    def __init__(self):
        self.array = []

    def __getitem__(self, item: int):
        result = self.array[item]
        if result is placeholder:
            raise IndexError('Такого индекса не существует')
        return result

    @property
    def size(self):
        return len(self.array)

    def append(self, item, index: int = -1):
        if index > self.size:
            raise IndexError('Такого индекса не существует')

        if index < 0:
            index = self.size + index

        if index < self.size:
            self.array[index + 1:self.size] = self.array[index:self.size - 1]

        self.array[index] = item

    def remove(self, index: int):
        if index > self.size:
            raise IndexError('Такого индекса не существует')

        if index < 0:
            index = self.size + index

        removed = self.array[index]
        self.array[index:self.size - 1] = self.array[index + 1: self.size]
        self.array[-1] = placeholder
        return removed


class WrapArray:

    def __init__(self):
        self.array = []

    def append(self, item, index: int = -1):
        return self.array.insert(index, item)

    def remove(self, index):
        return self.array.pop(index)
