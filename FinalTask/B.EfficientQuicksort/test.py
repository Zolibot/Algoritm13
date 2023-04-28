""" Doc string. """
from random import choice
from typing import List

COUNT = 0


def partition(array, pivot):
    """ Doc string. """
    left = [x for x in array if x < pivot]
    center = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return left, center, right


def quicksort(array):
    """ Doc string. """
    global COUNT
    COUNT += 1
    if len(array) < 2:
        return array
    else:
        pivot = choice(array)
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


def swap(array: List[int], first: int, second: int) -> None:
    """ Doc string. """
    array[first], array[second] = array[second], array[first]


def partition_in_place(array: List[int], pivot: int):
    """ Doc string. """
    left = 0
    right = len(array) - 1

    while True:
        if array[left] >= pivot >= array[right]:
            swap(array, left, right)
            left += 1
            right -= 1

        if array[left] < pivot :
            left += 1

        if array[right] > pivot :
            right -= 1

        if right - left == -1:
            break

    return array


def quicksort_in_place(array: List[int]):
    """ Doc string. """
    global COUNT
    COUNT += 1
    if len(array) < 2:
        return array
    else:
        pivot = choice(array)
        partition_in_place(array, pivot)
        return quicksort(array)


if __name__ == "__main__":
    # arr = [9, 7, 8, 6, 5, 4, 3, 2, 1, 0]
    # print(quicksort(arr))
    # print(COUNT)
    # COUNT = 0
    

    arr = [4, 8, 9, 20, 1, 5, 3, 10]
    partition_in_place(arr, 5)
    print(arr)
    partition_in_place(arr, 4)
    print(arr)
    partition_in_place(arr, 3)
    print(arr)
    # print(quicksort_in_place(arr))
    # print(COUNT)
