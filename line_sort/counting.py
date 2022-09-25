def counting_sort(arr: list[int], max_value: int):
    counters = [0] * max_value
    for item in arr:
        counters[item] += 1

    for i in range(1, len(counters)):
        counters[i] = counters[i] + counters[i - 1]

    temp = [...] * len(arr)
    for item in arr:
        index = counters[item] - 1
        temp[index] = item
        counters[item] -= 1

    arr[:] = temp
