from unittest import TestCase
from random import randint, seed
from functools import partial
from time import monotonic
from array import array

from tester.timeout import timeout_deco

from .bucket import bucket_sort
from .counting import counting_sort
from .radix import radix_sort


class SortTest(TestCase):

    def test_sorts(self):
        sorts = [
            bucket_sort,
            partial(counting_sort, max_value=1000),
            partial(radix_sort, k=3)
        ]
        for sort in sorts:
            arr = [randint(0, 999) for _ in range(100)]
            for_sort = list(arr)
            sort(for_sort)
            arr = sorted(arr)
            assert for_sort == arr


class BenchmarkTest(TestCase):

    def sorts(self):
        return {
            'Блочная': bucket_sort,
            'Подсчет': partial(counting_sort, max_value=1000),
            'По основанию': partial(radix_sort, k=3)
        }

    def run_test(self, sort, arr, name):

        timeout_reached = False
        start = monotonic()

        try:
            sort(arr)
        except TimeoutError:
            timeout_reached = True

        time = monotonic() - start

        formatted_time = f'{(time * 1000):.0f} ms'
        print(f'{name}: {formatted_time if not timeout_reached else "timeout"}')

    def test_sorts(self):
        lists = self.sorts()
        cases = [
            100,
            1000,
            10_000,
            100_000,
            1_000_000,
            10_000_000
        ]

        print('Время сортировок')
        for case in cases:
            print(f'{case} элементов:')
            for name, sort in lists.items():
                sort = timeout_deco(60 * 2)(sort)
                seed(case)
                arr = [randint(0, 999) for _ in range(case)]
                self.run_test(sort, arr, name)
                print('------------------')

    def test_billion(self):
        lists = {
            'Блочная': bucket_sort,
            'Подсчет': partial(counting_sort, max_value=65536),
            'По основанию': partial(radix_sort, k=5)
        }

        print('Время сортировок')
        for name, sort in lists.items():
            path = 'line_sort/billion.tmp'
            with open(path, 'rb') as fp:
                arr = array('I')
                arr.fromfile(fp, 1_000_000_00)

            self.run_test(sort, arr.tolist(), name)
            print('------------------')
