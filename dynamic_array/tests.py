from unittest import TestCase
from time import monotonic
from copy import copy

from tester.timeout import timeout_deco

from .base import WrapArray
from .single import SingleArray
from .vector import VectorArray
from .factor import FactorArray
from .matrix import insert_to_line_right, insert_to_line_left, MatrixArray


class ArrayTest(TestCase):

    def test_single_array(self):
        arr = SingleArray()

        arr.append(1)
        assert arr[0] == 1

        arr.append(2)
        assert arr[0] == 1
        assert arr[1] == 2

        arr.append(3, 1)
        assert arr[0] == 1
        assert arr[1] == 3
        assert arr[2] == 2

        arr.remove(1)
        assert arr[0] == 1
        assert arr[1] == 2

    def test_vector_array(self):
        arr = VectorArray()

        arr.append(1)
        assert arr[0] == 1

        arr.append(2)
        assert arr[0] == 1
        assert arr[1] == 2

        arr.append(3, 1)
        assert arr[0] == 1
        assert arr[1] == 3
        assert arr[2] == 2

        arr.remove(1)
        assert arr[0] == 1
        assert arr[1] == 2

        arr = VectorArray(2)

        arr.append(1)
        assert len(arr.array) == 2

        arr.append(2)
        assert len(arr.array) == 2

        arr.append(3)
        assert len(arr.array) == 4

    def test_factor_array(self):
        arr = FactorArray()

        arr.append(1)
        assert arr[0] == 1

        arr.append(2)
        assert arr[0] == 1
        assert arr[1] == 2

        arr.append(3, 1)
        assert arr[0] == 1
        assert arr[1] == 3
        assert arr[2] == 2

        arr.remove(1)
        assert arr[0] == 1
        assert arr[1] == 2

        arr = FactorArray()

        for i in range(5):
            arr.append(i)

        assert len(arr.array) == 8

    arr = FactorArray()

    for i in range(17):
        arr.append(i)

    assert len(arr.array) == 32

    def test_matrix_array(self):
        arr = MatrixArray(line_size=2)

        arr.append(1)
        assert arr[0] == 1

        arr.append(2)
        assert arr[0] == 1
        assert arr[1] == 2

        arr.append(3, 1)
        assert arr[0] == 1
        assert arr[1] == 3
        assert arr[2] == 2

        arr = MatrixArray(line_size=2)

        for i in range(6):
            arr.append(i)

        arr.remove(1)

        assert arr[0] == 0
        assert arr[1] == 2
        assert arr[2] == 3
        assert arr[3] == 4
        assert arr[4] == 5

        arr = MatrixArray(line_size=10)

        for i in range(100):
            arr.append(i)

        arr.remove(10)

        assert arr[0] == 0
        assert arr[10] == 11
        assert arr[90] == 91

        arr = MatrixArray(line_size=2)

        for i in range(10):
            arr.append(i)

        for i in range(10):
            arr.remove(0)

        assert arr.size == 0

    def test_insert_to_line(self):
        line = [0, 1, 2, 3, 4]
        excess = insert_to_line_right(line, 5, 2)

        assert excess == 4
        assert line == [0, 1, 5, 2, 3]

        line = [0, 1, 2, 3, 4]
        excess = insert_to_line_left(line, 5, 2)

        assert excess == 0
        assert line == [1, 2, 5, 3, 4]


class BenchmarkTest(TestCase):

    def arrays(self):
        return {
            'Стандартный массив': WrapArray,
            'Простой массив': SingleArray,
            'Векторный массив': VectorArray,
            'Факторный массив': FactorArray,
            'Матричный массив': MatrixArray
        }

    def run_test(self, case, cases, name, array_cls, init: callable = None):
        for elements in cases:
            array = array_cls()
            if init:
                init(array)

            timeout_reached = False
            start = monotonic()

            try:
                case(array, elements)
            except TimeoutError:
                timeout_reached = True

            time = monotonic() - start

            formatted_time = f'{(time * 1000):.0f} ms'
            print(f'{name} {elements}: {formatted_time if not timeout_reached else "timeout"}')

    def test_append_last(self):
        lists = self.arrays()
        cases = [
            500,
            1000,
            5_000,
            10_000
        ]

        @timeout_deco(3)
        def case(arr, size):
            for i in range(size):
                arr.append(i)

        print('Добавление в конец')
        for name, array in lists.items():
            self.run_test(case, cases, name, array)
            print('------------------')

    def test_append_first(self):
        lists = self.arrays()
        cases = [
            500,
            1000,
            5_000,
            10_000
        ]

        @timeout_deco(3)
        def case(arr, size):
            for i in range(size):
                arr.append(i, 0)

        print('Добавление в начало')
        for name, array in lists.items():
            self.run_test(case, cases, name, array)
            print('------------------')

    def test_remove_last(self):
        lists = self.arrays()
        cases = [
            500,
            1000,
            5_000,
            10_000
        ]

        @timeout_deco(3)
        def case(arr, size):
            for i in range(size):
                arr.remove(-1)

        print('Удаление с конца')
        for name, array in lists.items():

            def init(arr):
                for i in range(10_000):
                    arr.append(i)

            self.run_test(case, cases, name, array, init=init)
            print('------------------')

    def test_remove_first(self):
        lists = self.arrays()
        cases = [
            500,
            1000,
            5_000,
            10_000
        ]

        @timeout_deco(3)
        def case(arr, size):
            for i in range(size):
                arr.remove(0)

        print('Удаление с начала')
        for name, array in lists.items():

            def init(arr):
                for i in range(10_000):
                    arr.append(i)

            self.run_test(case, cases, name, array, init=init)
            print('------------------')
