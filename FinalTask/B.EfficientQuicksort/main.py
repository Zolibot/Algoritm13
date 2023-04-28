from typing import List, Callable


def swap(num_array: List[int], first: int, second: int) -> None:
    num_array[first], num_array[second] = num_array[second], num_array[first]


def compare(num_array: List[int], index: int, pivot: List[any]) -> bool:
    man1: List[any] = array[index]
    man2: List[any] = pivot
    if man1[1] > man2[1]:
        return True
    elif man1[1] == man2[1] and man1[2] < man2[2]:
        return True
    elif man1[1] == man2[1] and man1[2] == man2[2] and man1[0] < man2[0]:
        return True
    return False


def partition(array: List[int], low: int, high: int, func: Callable) -> int:
    pivot: int = array[high]
    great_num: int = low - 1
    for index in range(low, high):
        if func(array, index, pivot):
            great_num += 1
            swap(array, great_num, index)
    great_num += 1
    swap(array, great_num, high)
    return great_num


def quicksort(array: List[int], low: int, high: int, func: Callable) -> None:
    if low < high:
        top_point: int = partition(array, low, high, func)
        quicksort(array, low, top_point - 1, func)
        quicksort(array, top_point + 1, high, func)


def load_data() -> List[List[any]]:
    file = open('./input.txt', 'rt')
    size: int = int(file.readline())
    return [
        [int(x) if x.isdigit() else x for x in file.readline().split()]
        for _ in range(size)
    ]


if __name__ == '__main__':
    array = load_data()
    quicksort(array, 0, len(array) - 1, compare)
    for name, _, _ in array:
        print(name)
