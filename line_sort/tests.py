from unittest import TestCase
from random import randint
from functools import partial

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
