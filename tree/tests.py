from unittest import TestCase
from random import randint

from tester.timeout import timeout_deco, timeout

from .tree import BinaryTree

#           4
#     2           6
#  1           5      8
ITEMS = [4, 2, 6, 5, 1, 8]


class TreeTest(TestCase):

    def test_insert(self):
        tree = BinaryTree()
        for item in ITEMS:
            tree.insert(item)

        assert tree.root.left.left.value == 1
        assert tree.root.right.right.value == 8
        assert tree.root.right.left.value == 5

    def test_search(self):
        tree = BinaryTree()
        for item in ITEMS:
            tree.insert(item)

        node = tree.search(999)
        assert node is None

        node = tree.search(1)
        assert node.value == 1

    def test_delete(self):
        tree = BinaryTree()
        for item in ITEMS:
            tree.insert(item)

        tree.remove(4)
        assert tree.root.left.left is None
        assert tree.root.right.right.value == 8

        tree.remove(8)
        assert tree.root.right.right is None


class BenchmarkTest(TestCase):

    @timeout_deco(60)
    def case(self, tree, items, operation):
        operation = getattr(tree, operation)
        for item in items:
            operation(item)

    def test_inserts(self):
        cases = [
            100,
            1000,
            10_000,
            100_000,
        ]

        print('Время вставки')
        for case in cases:
            print('------------------')
            print(f'{case} элементов:')
            print('------------------')
            arr = [randint(0, 999) for _ in range(case)]
            tree = BinaryTree()
            with timeout('Случайные элементы'):
                self.case(tree, arr, 'insert')

            arr = sorted([randint(0, 999) for _ in range(case)])
            tree = BinaryTree()
            with timeout('Упорядоченные элементы'):
                self.case(tree, arr, 'insert')

    def test_search(self):
        cases = [
            100,
            1000,
            10_000,
            100_000,
        ]

        print('Время поиска')
        for case in cases:
            print('------------------')
            print(f'{case} элементов:')
            print('------------------')
            searched = [randint(0, 999) for _ in range(case // 10)]
            arr = [randint(0, 999) for _ in range(case)]
            tree = BinaryTree()
            for item in arr:
                tree.insert(item)

            with timeout('Случайные элементы'):
                self.case(tree, searched, 'search')

            arr = sorted([randint(0, 999) for _ in range(case)])
            tree = BinaryTree()
            for item in arr:
                tree.insert(item)

            with timeout('Упорядоченные элементы'):
                self.case(tree, searched, 'search')

    def test_delete(self):
        cases = [
            100,
            1000,
            10_000,
            100_000,
        ]

        print('Время поиска')
        for case in cases:
            print('------------------')
            print(f'{case} элементов:')
            print('------------------')
            deleted = [randint(0, 999) for _ in range(case // 10)]
            arr = [randint(0, 999) for _ in range(case)]
            tree = BinaryTree()
            for item in arr:
                tree.insert(item)

            with timeout('Случайные элементы'):
                self.case(tree, deleted, 'remove')

            arr = sorted([randint(0, 999) for _ in range(case)])
            tree = BinaryTree()
            for item in arr:
                tree.insert(item)

            with timeout('Упорядоченные элементы'):
                self.case(tree, deleted, 'remove')
