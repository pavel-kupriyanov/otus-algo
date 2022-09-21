def heapify(arr: list[int], root: int, size: int):
    left, right = 2 * root + 1, 2 * root + 2,
    top = root

    if left < size and arr[left] > arr[top]:
        top = left

    if right < size and arr[right] > arr[top]:
        top = right

    if top == root:
        return

    arr[top], arr[root] = arr[root], arr[top]
    heapify(arr, top, size)


def heap(arr: list[int]):
    length = len(arr)
    for i in reversed(range(0, length // 2)):
        heapify(arr, i, length)

    for i in reversed(range(0, length)):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
