from unittest import TestCase
from functools import partial

from .sorts import (
    bubble,
    bubble_optimized,
    insert,
    insert_shift,
    insert_optimized,
    shell,
    n_2k_minus_1,
    n_4pow_k_plus_2pow_k_minus_1_plus_1
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
            partial(shell, gap_gen=n_4pow_k_plus_2pow_k_minus_1_plus_1)
        ]
        for sort in sorts:
            arr = list(range(11))
            for_sort = list(reversed(arr))
            sort(for_sort)
            assert for_sort == arr
