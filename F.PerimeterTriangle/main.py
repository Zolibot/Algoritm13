from typing import Tuple, List

def load_data() -> Tuple[int, List[int]]:
    with open('./input.txt', 'rt') as f:
        count = int(f.readline())
        length = [int(_) for _ in f.readline().split()]
        length.sort()
        length.reverse()
        return count, length


if __name__ == '__main__':
    count, length = load_data()
    for i, x in enumerate(length):
        if x < length[i+1]+length[i+2]:
            print(x+length[i+1]+length[i+2])
            break


