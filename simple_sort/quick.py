def quick(arr: list[int], left: int = 0, right: int = -1):
    if right == -1:
        right = len(arr) - 1

    if left >= right:
        return

    left_pointer, right_pointer = left, right
    mid = arr[right]

    while left_pointer <= right_pointer:

        while arr[left_pointer] < mid:
            left_pointer += 1

        while arr[right_pointer] > mid:
            right_pointer -= 1

        if left_pointer <= right_pointer:
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
            left_pointer += 1
            right_pointer -= 1

    quick(arr, left, right_pointer)
    quick(arr, left_pointer, right)


def quick_alter(arr: list[int], left: int = 0, right: int = -1):
    if right == -1:
        right = len(arr) - 1

    p = arr[right]

    left_border = left - 1
    right_border = left

    while right_border <= right:
        if arr[right_border] <= p:
            left_border += 1
            arr[left_border], arr[right_border] = arr[right_border], arr[left_border]

        right_border += 1

    if left < left_border - 1:
        quick_alter(arr, left, left_border - 1)

    if left_border + 1 < right:
        quick_alter(arr, left_border + 1, right)
