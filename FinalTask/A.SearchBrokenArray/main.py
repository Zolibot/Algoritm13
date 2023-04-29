# 86570852
from typing import List, Tuple


def is_between(num: int, array: List[int], first: int, second: int) -> bool:
    return array[first] <= num <= array[second]


def is_rise(array: List[int], first: int, second: int) -> bool:
    return array[second] > array[first]


def broken_search(nums: List[int], goal: int) -> int:
    length: int = len(nums)
    first: int = 0
    mid: int = length // 2
    end: int = length

    def to_left():
        nonlocal end, mid, first
        end = mid
        mid = (end + first) // 2

    def to_right():
        nonlocal end, mid, first
        first = mid
        mid = (end + mid) // 2

    while end - first >= 2:
        if nums[mid] == goal:
            return mid

        if is_between(goal, nums, first, mid):
            if is_rise(nums, first, mid):
                to_left()
        elif is_between(goal, nums, mid, end-1):
            if is_rise(nums, mid, end):
                to_right()
        elif not is_rise(nums, first, mid):
            to_left()
        elif not is_rise(nums, mid, end):
            to_right()

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


def load_data() -> Tuple[List[int], int]:
    _ = int(input())
    target = int(input())
    data = [int(number) for number in input().split()]
    return data, target


if __name__ == "__main__":
    test()
    # array, number = load_data()
    # print(broken_search(array, number))
