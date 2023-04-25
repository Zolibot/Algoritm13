from typing import Tuple, List


def load_data() -> Tuple[int, List[int]]:
    file = open('./input.txt', 'rt')
    length: int = int(file.readline())
    arr: List[int] = [int(x) for x in file.read().strip().split()]
    return length, arr


def counting_sort(length: int, arr: List[int]) -> None:
    if length <= 1 :
        return
    counted_values: List[int] = [0] * length
    minimum: min = min(arr)
    for value in arr:
        counted_values[value - minimum] += 1
    index: int = 0
    for value in range(minimum, length + minimum):
        for idx in range(counted_values[value - minimum]):
            arr[index] = value
            index += 1



if __name__ == '__main__':
    size, data = load_data()
    counting_sort(size, data)
    print(' '.join(map(str, data)))
    

