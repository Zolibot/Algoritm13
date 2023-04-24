def merge(arr, lf, mid, rg):
    left = arr[lf: mid]
    right = arr[mid: rg]

    result = [None] * len(arr)

    size_left = len(left)
    size_right = len(right)

    left_idx = 0
    right_idx = 0
    result_idx = 0

    while left_idx < size_left and right_idx < size_right:
        if left[left_idx] <= right[right_idx]:
            result[result_idx] = left[left_idx]
            left_idx += 1
        else:
            result[result_idx] = right[right_idx]
            right_idx += 1
        result_idx += 1

    while left_idx < size_left:
        result[result_idx] = left[left_idx]
        left_idx += 1
        result_idx += 1
    while right_idx < size_right:
        result[result_idx] = right[right_idx]
        right_idx += 1
        result_idx += 1

    return result


def merge_sort(arr, lf, rg):
    if len(arr) == 1:
        return arr
    left = arr[lf: mid]
    right = arr[mid: rg]





    pass


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
