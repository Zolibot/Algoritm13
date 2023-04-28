from typing import List


def swap(num_array: List[int], first: int, second: int) -> None:
    num_array[first], num_array[second] = num_array[second], num_array[first]


def partition(array: List[int], low: int, high: int) -> int:
    pivot: int = array[high]
    great_num: int = low - 1
    for idx in range(low, high):
        if array[idx] <= pivot:
            great_num += 1
            swap(array, great_num, idx)
    great_num += 1
    swap(array, great_num, high)
    return great_num


def quicksort(array: List[int], low: int, high: int) -> None:
    if low < high:
        top_point: int = partition(array, low, high)
        quicksort(array, low, top_point - 1)
        quicksort(array, top_point + 1, high)


if __name__ == '__main__':
    array = [10, -1, 8, 9, 1, 5]
    quicksort(array, 0, len(array) - 1)
    print(array)
