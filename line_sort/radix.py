def radix_sort(arr: list[int], k: int):
    for i in range(1, k + 1):
        mod, div = 10 ** i, 10 ** (i - 1)
        counters = [0] * 10

        for item in arr:
            counters[item % mod // div] += 1

        for i in range(1, len(counters)):
            counters[i] = counters[i] + counters[i - 1]

        local_temp = arr[:]
        for item in reversed(arr):
            index = counters[item % mod // div] - 1
            local_temp[index] = item
            counters[item % mod // div] -= 1

        arr[:] = local_temp
