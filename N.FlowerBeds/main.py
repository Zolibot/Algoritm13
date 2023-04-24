from typing import Tuple, List


def load_data() -> Tuple[int, List[List[int]]]:
    file = open('./input.txt', 'rt')
    length: int = int(file.readline())
    double_arr: List[List[int]] = [
        list(map(int, file.readline().split())) for x in range(length)
    ]
    return length, double_arr


def sort_flower_bets():
    pass


if __name__ == '__main__':
    size, data = load_data()
    print(size)
    print(data)
