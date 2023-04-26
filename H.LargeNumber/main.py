from typing import List, Tuple, Callable


def load_data() -> Tuple[int, List[int]]:
    file = open('./H.LargeNumber/input.txt', 'rt')
    length = int(file.readline())
    data = [int(x) for x in file.readline().split()]
    return length, data


def compare(num1: int, num2: int) -> bool:
    if int(str(num1) + str(num2)) > int(str(num2) + str(num1)):
        return True
    return False


def sort_by_compare(size: int, arr: List[int], func: Callable) -> List[int]:
    for i in range(1, size):
        item_to_insert = arr[i]
        j = i
        while j > 0 and func(item_to_insert, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item_to_insert
    return arr


if __name__ == '__main__':
    size, arr = load_data()
    result = sort_by_compare(size, arr, compare)
    print(''.join(map(str, result)))
