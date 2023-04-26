def broken_search(nums, target) -> int:
    try:
        result = nums.index(target)
    except ValueError:
        result = -1
    return result


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    assert broken_search(arr, 1235) == -1


if __name__ == '__main__':
    test()