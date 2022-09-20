from unittest import TestCase

from .popcnt import cached_popcnt, tricky_popcnt, simple_popcnt


class PopcntTest(TestCase):

    def test_popcnt(self):
        masks = {
            0b011011: 4,
            0b000000: 0,
            0b111111111: 9,
            0b1010101010101010101010101: 13
        }

        for n, expected in masks.items():
            assert simple_popcnt(n) == expected
            assert cached_popcnt(n) == expected
            assert tricky_popcnt(n) == expected
