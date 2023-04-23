from typing import List, Tuple


def load_data() -> Tuple[int, List[int]]:
    file = open('./input.txt', 'rt')
    length = int(file.readline())
    data = [int(x) for x in file.readline().split()]
    return length, data


def bubble_sort(length: int, digits: List[int]) -> None:
    index: int = length - 1
    idx: int = length - 1

    while index != 0:
        inner = 0
        check: int = 0
        while inner < idx:
            if digits[inner] > digits[inner+1]:
                digits[inner+1], digits[inner] = digits[inner], digits[inner+1]
                check += 1

            inner += 1
            if inner == idx:
                if check == 0:
                    if index == length - 1:
                        print(' '.join(map(str, digits)))
                    return
                idx -= 1
                index -= 1

                print(' '.join(map(str, digits)))


if __name__ == '__main__':
    size, arr = load_data()
    bubble_sort(size, arr)
