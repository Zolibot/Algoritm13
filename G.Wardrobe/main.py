from typing import Tuple, List


def load_data() -> Tuple[int, List[int]]:
    file = open('./G.Wardrobe/input.txt', 'rt')
    length: int = int(file.readline())
    arr: List[int] = [int(x) for x in file.read().strip().split()]
    return length, arr


def counting_sort(length: int, arr: List[int]) -> None:
    if length <= 1:
        return None
    counted_values: List[int] = [0] * (max(arr) + 1)

    for item in arr:
        counted_values[item] += 1

    result = [
        num for num, count in enumerate(counted_values) for i in range(count)
    ]
    return result


if __name__ == '__main__':
    size, data = load_data()
    s = counting_sort(size, data)
    if s:
        print(' '.join(map(str, s)))
