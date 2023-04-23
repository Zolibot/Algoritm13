from typing import List, Tuple


def load_data() -> Tuple[int, List[int]]:
    file = open('./J.Bubble/input.txt', 'rt')
    length = int(file.readline())
    data = [int(x) for x in file.readline().split()]
    return length, data


def bubble_sort(length: int, digits: List[int]) -> None:
    one_iter: int = length - 2
    index: int = length - 1
    idx: int = length - 1
    check: List[bool] = [False for x in range(length-1)]
    while index != 0:
        inner = 0
        while inner < idx:
            if digits[inner] > digits[inner+1]:
                # tmp = digits[inner+1]
                # digits[inner+1] = digits[inner]
                # digits[inner] = tmp
                digits[inner+1], digits[inner] = digits[inner], digits[inner+1]
                check[inner] = True
            inner += 1
            if inner == idx:
                idx -= 1
                index -= 1
                print(' '.join(map(str, digits)))
        if index == one_iter:
            index = sum(check) - 1


if __name__ == '__main__':
    size, arr = load_data()
    bubble_sort(size, arr)
