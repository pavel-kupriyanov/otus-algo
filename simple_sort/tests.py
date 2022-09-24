from unittest import TestCase
from functools import partial
from time import monotonic
from random import seed, randint
from os import remove

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
from .quick import quick
from .merge import sort as merge
from .external import (
    external1,
    external2,
    external3,
    make_test_file,
    read_int
)


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
            heap,
            quick,
            merge
        ]
        for sort in sorts:
            arr = [randint(0, 1000) for _ in range(100)]
            for_sort = list(arr)
            sort(for_sort)
            arr = sorted(arr)
            assert for_sort == arr


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
            'Пирамидальная': heap,
            'Быстрая': quick,
            'Слияние': merge
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
                arr = [randint(0, 1000) for _ in range(case)]
                self.run_test(sort, arr, name)
                print('------------------')


class ExternalTest(TestCase):

    def is_sorted(self, name: str):
        last_num = float('-inf')
        with open(name) as fp:
            while last_num is not None:
                num = read_int(fp)
                if num is None:
                    break
                if num < last_num:
                    raise AssertionError('Unsorted')
                last_num = num

    def test_external(self):
        input_name = 'external_unsorted.tmp'
        output_name = 'external_sorted.tmp'

        make_test_file(100, 10, input_name)

        external1(10, input_name=input_name, output_name=output_name)
        self.is_sorted(output_name)
        remove(output_name)

        external2(input_name, output_name)
        self.is_sorted(output_name)
        remove(output_name)

        external3(input_name, output_name, 10)
        self.is_sorted(output_name)
        remove(output_name)

        remove(input_name)

    def test_timings(self):
        cases = [
            (100, 10),
            (1000, 10),
            (10_000, 10),
            (100_000, 10),
            (1_000_000, 10),
            (100, 100),
            (1000, 1000),
            (10_000, 10_000),
            (100_000, 100_000)
        ]

        input_name, output_name = 'unsorted.tmp', 'sorted.tmp'

        print('Время сортировок')
        for n, t in cases:
            sorts = {
                'Обычная': partial(external1, t=t, input_name=input_name, output_name=output_name),
                '2 Файла': partial(external2, input_name=input_name, output_name=output_name),
                '2 Файла с предсортировкой': partial(external3, batch_size=100, input_name=input_name,
                                                     output_name=output_name)
            }
            print(f'{n} элементов:')
            for name, sort in sorts.items():
                sort = timeout_deco(60 * 2)(sort)
                seed(n)
                make_test_file(n, t, input_name)
                self.run_test(sort, name)
                remove(input_name)
                remove(output_name)
                print('------------------')

    def run_test(self, sort, name):
        timeout_reached = False
        start = monotonic()

        try:
            sort()
        except TimeoutError:
            timeout_reached = True

        time = monotonic() - start

        formatted_time = f'{(time * 1000):.0f} ms'
        print(f'{name}: {formatted_time if not timeout_reached else "timeout"}')
