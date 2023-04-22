from typing import List, Tuple


def load_data() -> Tuple[int, List[int]]:
    file = open('./input.txt', 'rt')
    length = int(file.readline())
    data = [int(x) for x in file.readline().split()]
    return length, data


def bubble_sort(length: int, digits: List[int]):
    index = length - 1
    while index != 0:
        for x in range(length-1):
            if digits[x] > digits[x+1] and (x+1) != length:
                tmp = digits[x+1]
                digits[x+1] = digits[x]
                digits[x] = tmp
            elif x == length-2:
                print(' '.join(map(str, digits)))
                index = 1
        length -= 1
        index -= 1


if __name__ == '__main__':
    size, arr = load_data()
    bubble_sort(size, arr)
