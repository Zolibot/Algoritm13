from typing import Tuple


def load_data() -> Tuple[str, str]:
    file = open('./input.txt', 'rt')
    s1 = file.readline()
    s2 = file.readline()
    return s1, s2


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
