from typing import Tuple, List


def load_data() -> Tuple[int, int, List[int]]:
    with open('./input.txt', 'rt') as f:
        count_house, money = [int(_) for _ in f.readline().split()]
        houses_cost = [int(_) for _ in f.readline().split()]
        return count_house, money, houses_cost


if __name__ == '__main__':
    count_house, money, houses_cost = load_data()
    houses_cost.sort()
    index = 0
    for x in houses_cost:
        money -= x
        if money >= 0:
            index += 1
        else:
            break

    print(index)
