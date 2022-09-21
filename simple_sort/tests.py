from unittest import TestCase
from functools import partial
from time import monotonic
from random import seed, randint

from tester.timeout import timeout_deco

from .sorts import (
    bubble,
    bubble_optimized,
    insert,
    insert_shift,
    insert_optimized,
    shell,
    n_2k_minus_1,
    n_4pow_k_plus_2pow_k_minus_1_plus_1,
    select
)
from .heap import heap


class SortTest(TestCase):

    def test_sorts(self):
        sorts = [
            bubble,
            bubble_optimized,
            insert,
            insert_shift,
            insert_optimized,
            shell,
            partial(shell, gap_gen=n_2k_minus_1),
            partial(shell, gap_gen=n_4pow_k_plus_2pow_k_minus_1_plus_1),
            select,
            heap
        ]
        for sort in sorts:
            arr = list(range(11))
            for_sort = list(reversed(arr))
            sort(for_sort)
            assert for_sort == arr

    def test_shell(self):
        arr = [randint(0, 1000) for _ in range(100)]
        shell(arr, gap_gen=n_4pow_k_plus_2pow_k_minus_1_plus_1)
        assert arr


class BenchmarkTest(TestCase):

    def sorts(self):
        return {
            'Пузырек': bubble,
            'Оптимизированный пузырек': bubble_optimized,
            'Вставка': insert,
            'Вставка со смещением': insert_shift,
            'Оптимизированная вставка': insert_optimized,
            'Сортировка Шелла': shell,
            'Сортировка Шелла (2k - 1)': partial(shell, gap_gen=n_2k_minus_1),
            'Сортировка Шелла (4**k + 2**(k-1) + 1)': partial(shell, gap_gen=n_4pow_k_plus_2pow_k_minus_1_plus_1),
            'Выбор': select,
            'Пирамидальная': heap
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
            # 10_000_000
        ]

        @timeout_deco(3)
        def case(arr, size):
            for i in range(size):
                arr.append(i)

        print('Время сортировок')
        for case in cases:
            print(f'{case} элементов:')
            for name, sort in lists.items():
                sort = timeout_deco(60 * 2)(sort)
                seed(case)
                arr = [randint(0, 1000) for _ in range(case)]
                self.run_test(sort, arr, name)
                print('------------------')
