# 86638599
from functools import total_ordering
from typing import Callable, List


@total_ordering
class Member(object):

    def __init__(self, name: str, task: str, score: str) -> None:
        self.name: str = name
        self.task: int = int(task)
        self.score: int = int(score)

    def __eq__(self, other) -> bool:
        if self.name == other.name:
            if self.task == other.task:
                if self.score == other.score:
                    return True
        return False

    def __ge__(self, other):
        if self.task > other.task:
            return True
        if self.task == other.task:
            if self.score < other.score:
                return True
            if self.score == other.score:
                if self.name < other.name:
                    return True
        return False

    def __str__(self) -> str:
        return self.name


def swap(num_array: List[int], first: int, second: int) -> None:
    num_array[first], num_array[second] = num_array[second], num_array[first]


def compare(competitor_1: Member, competitor_2: Member) -> bool:
    return competitor_1 > competitor_2


def partition(array: List[Member], low: int, high: int, func: Callable) -> int:
    pivot: int = array[high]
    great_num: int = low - 1
    for index in range(low, high):
        if func(array[index], pivot):
            great_num += 1
            swap(array, great_num, index)
    great_num += 1
    swap(array, great_num, high)
    return great_num


def quicksort(array: List[int], low: int, high: int, func: Callable) -> None:
    if low < high:
        top_point: int = partition(array, low, high, func)
        quicksort(array, low, top_point - 1, func)
        quicksort(array, top_point + 1, high, func)


def load_data() -> List[List[any]]:
    file = open('FinalTask/B.EfficientQuicksort/input.txt', 'rt')
    size: int = int(file.readline())
    members: List[Member] = []
    for _ in range(size):
        members.append(Member(*file.readline().split()))
    return members


if __name__ == '__main__':
    array = load_data()
    quicksort(array, 0, len(array) - 1, compare)
    for name in array:
        print(name)
    man1 = Member('saha', '5', '5000')
    man2 = Member('saha', '5', '5000')
    assert (man1 == man2) == True
    man1 = Member('saha', '6', '5000')
    man2 = Member('saha', '5', '5000')
    assert (man1 > man2) == True
    man1 = Member('saha', '5', '5000')
    man2 = Member('saha', '5', '2000')
    assert (man1 < man2) == True
