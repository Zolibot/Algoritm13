from typing import List, Tuple


def is_between(number: int, arr: List[int]) -> bool:
    return arr[0] <= number <= arr[-1]


def get_answer(number: int, mid=0) -> int:
    if number == -1:
        return -1
    return number + mid


def broken_search(nums: List[int], target: int) -> int:
    length: int = len(nums)
    mid: int = length // 2

    if length <= 2:
        if nums[0] == target:
            return 0
        if nums[mid] == target:
            return mid
        return -1

    left: List[int] = nums[:mid]
    right: List[int] = nums[mid:]

    if is_between(target, left) and (left[-1] > left[0] or len(left) == 1):
        return get_answer(broken_search(left, target))
    elif is_between(target, right) and (right[-1] > right[0] or len(right) == 1):
        return get_answer(broken_search(right, target), mid)
    elif right[-1] < right[0]:
        return get_answer(broken_search(right, target), mid)
    elif left[-1] < left[0]:
        return get_answer(broken_search(left, target))
    else:
        return -1


def test():
    arr = [19, 21, 100, 101, 102, 103, 3, 5, 7, 12]
    assert broken_search(arr, 20) == -1
    assert broken_search(arr, 21) == 1
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    assert broken_search(arr, 1235) == -1
    arr = [19, 21, 100, 101, 102, 103, 3, 5, 7, 12]
    assert broken_search(arr, 5) == 7
    assert broken_search(arr, 21) == 1
    arr = [19, 21, 100, 0, 1, 2, 3, 5, 7, 12]
    assert broken_search(arr, 21) == 1
    assert broken_search(arr, 221) == -1
    arr = [0]
    assert broken_search(arr, 0) == 0
    assert broken_search(arr, 1) == -1
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert broken_search(arr, 5) == 4


if __name__ == "__main__":
    test()
