from array import array
from random import randint


def store_billion_to_file(name: str):
    arr = array('I', (randint(0, 65535) for _ in range(1_000_000_00)))
    with open(name, 'wb') as fp:
        arr.tofile(fp)


# store_billion_to_file('billion.tmp')