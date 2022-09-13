from unittest import TestCase

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

    def test_insert_to_line(self):
        line = [0, 1, 2, 3, 4]
        excess = insert_to_line_right(line, 5, 2)

        assert excess == 4
        assert line == [0, 1, 5, 2, 3]

        line = [0, 1, 2, 3, 4]
        excess = insert_to_line_left(line, 5, 2)

        assert excess == 0
        assert line == [1, 2, 5, 3, 4]
