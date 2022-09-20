from bisect import bisect_left


def bubble(arr: list[int]):
    for i in range(len(arr), 0, -1):
        for j in range(i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_optimized(arr: list[int]):
    for i in range(len(arr), 0, -1):
        is_sorted = True
        for j in range(i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            return


def insert(arr: list[int]):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


def insert_shift(arr: list[int]):
    for i in range(1, len(arr)):
        for_insert = arr[i]
        for j in range(i):
            if for_insert < arr[j]:
                arr[j + 1:i + 1] = arr[j:i]
                arr[j] = for_insert
                break


def insert_optimized(arr: list[int]):
    for i in range(1, len(arr)):
        for_insert = arr[i]
        j = bisect_left(arr, for_insert, hi=i)
        arr[j + 1:i + 1] = arr[j:i]
        arr[j] = for_insert


def n_square(n: int):
    gap = n // 2
    while gap > 0:
        yield gap
        gap //= 2


def n_2k_minus_1(n: int):
    gap = 1
    while gap < n:
        yield gap
        gap = gap * 2 + 1


def n_4pow_k_plus_2pow_k_minus_1_plus_1(n: int):
    yield 1
    gap, k = 1, 1
    while gap < n:
        gap = 4 ** k + 2 ** (k - 1) + 1
        yield gap
        k += 1


def shell(arr: list[int], gap_gen=n_square):
    n = len(arr)
    for gap in gap_gen(n):
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j - gap] > arr[j]:
                arr[j - gap], arr[j] = arr[j], arr[j - gap]
                j -= gap
