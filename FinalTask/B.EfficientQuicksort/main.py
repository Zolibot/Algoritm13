# 86681352
from functools import total_ordering
from typing import Callable, List, Tuple


@total_ordering
class Member(object):

    def __init__(self, name_member: str, task: str, fine: str) -> None:
        self.name: str = name_member
        self.task: int = int(task)
        self.fine: int = int(fine)

    def __eq__(self, other) -> bool:
        if self.name == other.name:
            if self.task == other.task:
                if self.fine == other.fine:
                    return True
        return False

    def __ge__(self, other):
        if self.task > other.task:
            return True
        if self.task == other.task:
            if self.fine < other.fine:
                return True
            if self.fine == other.fine:
                if self.name < other.name:
                    return True
        return False

    def __str__(self) -> str:
        return self.name


def swap(array: List[Member], first: int, second: int) -> None:
    array[first], array[second] = array[second], array[first]


def compare(competitor_1: Member, competitor_2: Member) -> bool:
    return competitor_1 > competitor_2


def partition(array: List[Member], low: int, high: int, func: Callable) -> int:
    # noinspection PyTypeChecker
    pivot: int = array[high]
    great_num: int = low - 1
    for index in range(low, high):
        if func(array[index], pivot):
            great_num += 1
            swap(array, great_num, index)
    great_num += 1
    swap(array, great_num, high)
    return great_num


def quicksort(array: List[Member], low: int, high: int, func: Callable) -> None:
    if low < high:
        top_point: int = partition(array, low, high, func)
        quicksort(array, low, top_point - 1, func)
        quicksort(array, top_point + 1, high, func)


def load_data() -> Tuple[List[Member], int]:
    size: int = int(input())
    members: List[Member] = []
    for _ in range(size):
        members.append(Member(*input().split()))
    return members, size


if __name__ == '__main__':
    competitors, length = load_data()
    quicksort(competitors, 0, length - 1, compare)
    for name in competitors:
        print(name)
