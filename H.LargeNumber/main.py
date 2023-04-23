from typing import List, Tuple, Callable


def load_data() -> Tuple[int, List[int]]:
    file = open('./H.LargeNumber/input.txt', 'rt')
    length = int(file.readline())
    data = [int(x) for x in file.readline().split()]
    return length, data


def get_number_digit(number: int) -> int:
    prev = number
    while bin(number).count('1') > 0:
        prev = number
        number = number // 10
    return prev


def summa(num: int) -> int:
    return sum(list(map(int, str(num)))) / bin(num).count('1')


def compare(num1: int, num2: int) -> bool:
    if get_number_digit(num1) == get_number_digit(num2):
        sum1 = summa(num1)
        sum2 = summa(num2)

        if sum1 > sum2:
            return True

    return get_number_digit(num1) > get_number_digit(num2)


def sort_by_compare(size: int, arr: List[int], func: Callable) -> List[int]:
    for i in range(1, size):
        item_to_insert = arr[i]
        j = i
        while j > 0 and func(item_to_insert, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item_to_insert
    return arr


test1 = "6\n9 10 1 1 1 6"
ancser = '9611110'
test2 = "38\n82 58 66 34 64 37 40 97 93 52 28 98 90 64 19 22 21 83 56 70 46 17 31 51 55 41 68 18 98 89 88 74 6 6 31 36 35 8"
ansver = '9898979390898888382747068666664645856555251464140373635343131282221191817'


def load_data1(file: str) -> Tuple[int, List[int]]:
    file = file.split('\n')
    length = int(file[0])
    data = [int(x) for x in file[1].split()]
    return length, data


if __name__ == '__main__':
    size, arr = load_data()
    size, arr = load_data1(test1)
    result = sort_by_compare(size, arr, compare)
    print(''.join(map(str, result)))
    print(result)
    size, arr = load_data1(test2)
    result = sort_by_compare(size, arr, compare)
    print(''.join(map(str, result)))
    print(result)

    print(summa(64), summa(6))
    print(bin(4).count('1'))
