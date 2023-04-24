from typing import List, Tuple, Callable


def load_data() -> Tuple[int, List[int]]:
    file = open('./C.SubSequence/input.txt', 'rt')
    s1 = file.readline()
    s2 = file.readline()
    return s1, s2


def compare(num1: int, num2: int) -> bool:
    if int(str(num1) + str(num2)) > int(str(num2) + str(num1)):
        return True
    return False


def sort_by_compare(size: int, arr: List[int], func: Callable) -> List[int]:
    for i in range(1, size):
        item_to_insert = arr[i]
        j = i
        while j > 0 and func(item_to_insert, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item_to_insert
    return arr


def sub_sequence(s1: str, s2: str) -> bool:
    size1 = len(s1)
    count = 0
    s1_index = 0
    for x in s2:
        if s1[s1_index] == x:
            count += 1
        s1_index += 1
        if count == size1-1:
            return True
        
    return False


if __name__ == '__main__':
    word1, word2 = load_data()
    result = sub_sequence(word1, word2)
    print(result)
