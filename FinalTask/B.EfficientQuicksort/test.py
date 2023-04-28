""" Doc string. """
import random
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


def partition_in_place(array: List[int], pivot: int, start: int, end: int):
    """ Doc string. """
    left = start
    right = end - 1
    print(pivot)

    while True:
        if array[left] >= pivot >= array[right]:
            swap(array, left, right)
            left += 1
            right -= 1

        if array[left] <= pivot:
            left += 1

        if array[right] > pivot:
            right -= 1

        if right - left <= 0:

            break

    return array


def quicksort_in_place(array: List[int], start: int, end: int):
    """ Doc string. """
    global COUNT
    COUNT += 1
    if end - start < 2:
        return array
    else:
        pivot = choice(array)
        partition_in_place(array, pivot, start, end-1)
        partition_in_place(array, pivot, start+1, end)
        return quicksort_in_place(array, start, end)


def sub_partition(array, start, end, idx_pivot):

    'returns the position where the pivot winds up'
    print(array)
    print(array[idx_pivot], idx_pivot)
    if not (start <= idx_pivot <= end):
        raise ValueError('idx pivot must be between start and end')

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1


def quicksort2(array, start=0, end=None):
    global COUNT
    COUNT += 1
    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return

    idx_pivot = random.randint(start, end)
    i = sub_partition(array, start, end, idx_pivot)
    #print array, i, idx_pivot
    quicksort2(array, start, i - 1)
    quicksort2(array, i + 1, end)


if __name__ == "__main__":
    # arr = [9, 7, 8, 6, 5, 4, 3, 2, 1, 0]
    # print(quicksort(arr))
    # print(COUNT)
    # COUNT = 0

    arr = [4, 8, 9, 9, 9, 9, 20, 1, 5, 3, 10]
    print(arr)
    quicksort2(arr)
    print(arr)
    print(COUNT)

    arr = ['alla',
           'gena',
           'gosha',
           'rita',
           'timofey',
    ]
