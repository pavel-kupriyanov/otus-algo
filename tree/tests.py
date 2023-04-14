from unittest import TestCase
from random import shuffle, choices

from tester.timeout import timeout_deco, timeout

from .tree import BinaryTree
from .balanced import BalancedTree

#           4
#     2           6
#  1           5      8
ITEMS = [4, 2, 6, 5, 1, 8]

#           5
#     3           7
#  2     4      6      8
# 1
BALANCED_ITEMS = [8, 7, 6, 5, 4, 3, 2, 1]


class BalancedTreeTest(TestCase):
    def test_insert(self):
        tree = BalancedTree()
        for item in BALANCED_ITEMS:
            tree.insert(item)

        assert tree.root.value == 5
        assert tree.root.left.value == 3
        assert tree.root.left.left.left.value == 1

        assert tree.root.right.right.value == 8

    def test_search(self):
        tree = BalancedTree()
        for item in BALANCED_ITEMS:
            tree.insert(item)

        node = tree.search(999)
        assert node is None

        node = tree.search(1)
        assert node.value == 1

    def test_delete(self):
        tree = BalancedTree()
        for item in BALANCED_ITEMS:
            tree.insert(item)

        tree.remove(7)
        assert tree.search(7) is None
        assert tree.root.right.value == 8


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
        self._test_inserts(BinaryTree)

    def test_balanced_inserts(self):
        self._test_inserts(BalancedTree)

    def test_search(self):
        self._test_search(BinaryTree)

    def test_balanced_search(self):
        self._test_search(BalancedTree)

    def test_delete(self):
        self._test_delete(BinaryTree)

    def test_balanced_delete(self):
        self._test_delete(BalancedTree)

    def _test_inserts(self, tree_cls):
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
            arr = [i for i in range(case)]
            shuffle(arr)
            tree = tree_cls()
            with timeout('Случайные элементы'):
                self.case(tree, arr, 'insert')

            arr = [i for i in range(case)]
            tree = tree_cls()
            with timeout('Упорядоченные элементы'):
                self.case(tree, arr, 'insert')

    def _test_search(self, tree_cls):
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
            arr = [i for i in range(case)]
            shuffle(arr)
            searched = choices(arr, k=case // 10)
            tree = tree_cls()
            for item in arr:
                tree.insert(item)

            with timeout('Случайные элементы'):
                self.case(tree, searched, 'search')

            arr = [i for i in range(case)]
            searched = choices(arr, k=case // 10)
            tree = tree_cls()
            for item in arr:
                tree.insert(item)

            with timeout('Упорядоченные элементы'):
                self.case(tree, searched, 'search')

    def _test_delete(self, tree_cls):
        cases = [
            100,
            1000,
            10_000,
            100_000,
        ]

        print('Время удаления')
        for case in cases:
            print('------------------')
            print(f'{case} элементов:')
            print('------------------')
            arr = [i for i in range(case)]
            shuffle(arr)
            deleted = choices(arr, k=case // 10)
            tree = tree_cls()
            for item in arr:
                tree.insert(item)

            with timeout('Случайные элементы'):
                self.case(tree, deleted, 'remove')

            arr = [i for i in range(case)]
            deleted = choices(arr, k=case // 10)
            tree = tree_cls()
            for item in arr:
                tree.insert(item)

            with timeout('Упорядоченные элементы'):
                self.case(tree, deleted, 'remove')
