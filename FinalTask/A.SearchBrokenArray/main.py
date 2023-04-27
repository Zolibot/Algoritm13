from typing import List


def is_between(number: int, array: List[int]) -> bool:
    return array[0] <= number <= array[-1]


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
    elif is_between(target, right) and (
            right[-1] > right[0] or len(right) == 1):
        return get_answer(broken_search(right, target), mid)
    elif right[-1] < right[0]:
        return get_answer(broken_search(right, target), mid)
    elif left[-1] < left[0]:
        return get_answer(broken_search(left, target))
    else:
        return -1


def is_between2(number: int, array: List[int], index_start: int, index_end: int) -> bool:
    return array[index_start] <= number <= array[index_end]


def broken_search2(nums: List[int], target: int) -> int:
    length: int = len(nums)
    first: int = 0
    mid: int = length // 2
    end: int = length

    while True:
        if end - first <= 2:
            if nums[first] == target:
                return first
            if nums[mid] == target:
                return mid
            return -1

        if is_between2(target, nums, first, mid-1) and (
                nums[mid - 1] > nums[first] or (mid - first) == 1):
            end = mid
            mid = (end + first) // 2

        elif is_between2(target, nums, mid, end-1) and (
                nums[end - 1] > nums[mid] or (end - first) == 1):
            first = mid
            mid = (end + mid) // 2

        elif nums[mid] < nums[first]:
            end = mid
            mid = (end + first) // 2

        elif nums[end - 1] < nums[mid]:
            first = mid
            mid = (end + mid) // 2

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


def test2():
    arr = [19, 21, 100, 101, 102, 103, 3, 5, 7, 12]
    assert broken_search2(arr, 20) == -1
    assert broken_search2(arr, 21) == 1
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search2(arr, 5) == 6
    assert broken_search2(arr, 1235) == -1
    arr = [19, 21, 100, 101, 102, 103, 3, 5, 7, 12]
    assert broken_search2(arr, 5) == 7
    assert broken_search2(arr, 21) == 1
    arr = [19, 21, 100, 0, 1, 2, 3, 5, 7, 12]
    assert broken_search2(arr, 21) == 1
    assert broken_search2(arr, 221) == -1
    arr = [0]
    assert broken_search2(arr, 0) == 0
    assert broken_search2(arr, 1) == -1
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert broken_search2(arr, 5) == 4


def load_data():
    file = open('./FinalTask/A.SearchBrokenArray/input.txt', 'rt')
    _ = file.readline()
    target = int(file.readline())
    numbers = [int(x) for x in file.readline().strip().split()]
    return numbers, target


def binary_search(array: List[int], val: int) -> int:
    first = 0
    last = len(array) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if array[mid] == val:
            index = mid
        else:
            if val < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


if __name__ == "__main__":
    test()
    test2()
    arr, tar = load_data()
    d = broken_search2(arr, tar)
    print(d, 'answer')
    assert broken_search2(arr, 25) == 69
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert binary_search(arr, 5) == 4
