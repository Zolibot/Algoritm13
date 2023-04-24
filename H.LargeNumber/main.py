from typing import List, Tuple, Callable


def load_data() -> Tuple[int, List[int]]:
    file = open('./input.txt', 'rt')
    length = int(file.readline())
    data = [int(x) for x in file.readline().split()]
    return length, data


def get_number_digit(number: int) -> int:
    prev = number
    index = 0
    while number > 0:
        prev = number
        number = number // 10
        index += 1
    return index


def get_last_digit(number: int) -> int:
    prev = number
    while number > 0:
        prev = number
        number = number // 10
    return prev


def summa(num: int) -> float:
    x = get_number_digit(num)
    return sum(list(map(int, str(num)))) / x


def compare(num1: int, num2: int) -> bool:
    sum1 = summa(num1)
    sum2 = summa(num2)

    s1 = get_last_digit(num1)
    s2 = get_last_digit(num2)

    i1 = get_number_digit(num1)
    i2 = get_number_digit(num2)

    if s1 == s2 and i1 == i2:
        if sum1 == sum2:
            return num1 > num2
        return sum1 > sum2
    elif i1 != i2:
        return s1 > s2

    return s1 > s2


def sort_by_compare(size: int, arr: List[int], func: Callable) -> List[int]:
    for i in range(1, size):
        item_to_insert = arr[i]
        j = i
        while j > 0 and func(item_to_insert, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item_to_insert
    return arr


def load_data1(file: str) -> Tuple[int, List[int]]:
    file = file.split('\n')
    length = int(file[0])
    data = [int(x) for x in file[1].split()]
    return length, data


if __name__ == '__main__':
    size, arr = load_data()
    result = sort_by_compare(size, arr, compare)
    print(''.join(map(str, result)))
    print(result)
