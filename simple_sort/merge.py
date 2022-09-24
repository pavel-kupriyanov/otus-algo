def sort(arr: list[int], left: int = 0, right: int = -1):
    if right == -1:
        right = len(arr) - 1

    if left >= right:
        return

    mid = (left + right) // 2
    sort(arr, left, mid)
    sort(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr: list[int], left: int, mid: int, right: int):
    new = []
    left_pointer, right_pointer = left, mid + 1

    while left_pointer <= mid and right_pointer <= right:

        if arr[left_pointer] < arr[right_pointer]:
            new.append(arr[left_pointer])
            left_pointer += 1
        else:
            new.append(arr[right_pointer])
            right_pointer += 1

    while left_pointer <= mid:
        new.append(arr[left_pointer])
        left_pointer += 1

    while right_pointer <= right:
        new.append(arr[right_pointer])
        right_pointer += 1

    arr[left:right + 1] = new
