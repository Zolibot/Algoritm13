from typing import Tuple, List


def load_data() -> Tuple[int, List[List[int]]]:
    file = open('./N.FlowerBeds/input.txt', 'rt')
    length: int = int(file.readline())
    double_arr: List[List[int]] = [
        list(map(int, file.readline().split())) for x in range(length)
    ]
    return length, double_arr


def sort_flower_bets():

    pass


def is_in_seq(arr1: List[int], arr2: List[int]) -> List[int]:
    if arr2[0] <= arr1[0] <= arr2[1]:
        arr1[0] = arr2[0]
    if arr2[0] <= arr1[1] <= arr2[1]:
        arr1[1] = arr2[1]
    return arr1


if __name__ == '__main__':
    size, data = load_data()
    print(size)
    print(data)

    print(is_in_seq([1, 3], [3, 5]))
    print(is_in_seq([-1, 4], [5, 6]))
