from typing import Tuple, List, Dict


def load_data() -> Tuple[int, List[int], int]:
    with open('./input.txt', 'rt') as f:
        size = int(f.readline())
        id_school = [int(x) for x in f.readline().split()]
        k = int(f.readline())
        return size, id_school, k


if __name__ == '__main__':
    size, id_school, k = load_data()

    count_val = [[i, 0] for i in range(max(id_school) + 1)]
    for val in id_school:
        count_val[val][1] += 1
    count_val.sort(key=lambda x: x[1], reverse=True)

    for i in range(k):
        print(count_val[i][0], end=' ')
