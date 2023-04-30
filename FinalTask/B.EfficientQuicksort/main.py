# 86758263
from collections import namedtuple
from random import randrange
from typing import List

Info = namedtuple('Competitor', 'task fine name')


class Member:

    def __init__(self, name_member: str, task: str, fine: str) -> None:
        self.data = Info(-int(task), int(fine),  name_member)

    def __str__(self) -> str:
        return self.data.name


def _partition(array: List[Member], low: int, high: int) -> int:
    rand_pivot: int = randrange(low, high)
    array[rand_pivot], array[high] = array[high], array[rand_pivot]
    pivot: int = high
    great_num: int = low - 1
    for index in range(low, high):
        if array[index].data < array[pivot].data:
            great_num += 1
            array[great_num], array[index] = array[index], array[great_num]
    great_num += 1
    array[great_num], array[high] = array[high], array[great_num]
    return great_num


def quicksort(array: List[Member], low=0, high=None) -> None:
    if high is None:
        high = len(array) - 1
    if low < high:
        top_point: int = _partition(array, low, high)
        quicksort(array, low, top_point - 1)
        quicksort(array, top_point + 1, high)


def load_data() -> List[Member]:
    size: int = int(input())
    members = [Member(*input().split()) for _ in range(size)]
    return members


if __name__ == '__main__':
    competitors = load_data()
    quicksort(competitors)
    print(*competitors, sep='\n')
