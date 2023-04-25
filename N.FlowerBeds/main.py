from typing import Tuple, List


def load_data() -> Tuple[int, List[List[int]]]:
    file = open('./input.txt', 'rt')
    length: int = int(file.readline())
    double_arr: List[List[int]] = [
        list(map(int, file.readline().split())) for _ in range(length)
    ]
    return length, double_arr


def is_between(number, arr: List[int]) -> bool:
    return arr[0] <= number <= arr[1]


def get_merge_bets(arr1: List[int], arr2: List[int]) -> List[int]:
    if is_merge_bets(arr1, arr2):
        if is_between(arr1[0], arr2):
            arr1[0] = arr2[0]
        if is_between(arr1[1], arr2):
            arr1[1] = arr2[1]
    return arr1


def is_merge_bets(arr1: List[int], arr2: List[int]) -> bool:
    if is_between(arr1[0], arr2):
        if is_between(arr1[1], arr2):
            return True
        return True
    if is_between(arr2[0], arr1):
        if is_between(arr2[1], arr1):
            return True
        return True
    return False


def sort_flower_bets(length: int, arr: List[List[int]]) -> List[List[int]]:
    result: List[List[int]] = [arr[0]]
    count = 0
    for idx in range(length - 1):
        if not is_merge_bets(result[count], arr[idx + 1]):
            result.append(arr[idx + 1])
            count += 1
        else:
            result[count] = get_merge_bets(result[count], arr[idx + 1])
    return result


if __name__ == '__main__':
    size, data = load_data()
    data.sort()
    res = sort_flower_bets(size, data)
    for x, y in res:
        print(x, y)
