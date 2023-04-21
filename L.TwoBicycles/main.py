from typing import Tuple, List


def load_data() -> Tuple[int, List[int], int]:
    file = open('./input.txt', 'rt')
    period = int(file.readline())
    data = [int(x) for x in file.readline().split()]
    price = int(file.readline())
    return period, data, price


def search_shopping_day(left: int, right: int, data: List[int], price: int):
    if price > data[right - 1]:
        return -1
    mid = (left + right) // 2

    if left == right:
        return mid // 2

    if mid == 0:
        return mid + 1

    if data[mid] >= price > data[mid - 1]:
        return mid + 1
    elif price < data[mid]:
        return search_shopping_day(left, mid, data, price)
    else:
        return search_shopping_day(mid+1, right, data, price)


if __name__ == '__main__':
    days, savings, cost = load_data()
    f = search_shopping_day(0, days, savings, cost)
    d = search_shopping_day(f, days, savings, cost*2)
    print(f, d)
