from typing import List, Tuple


def load_data() -> Tuple[List[int], List[int]]:
    file = open('./input.txt', 'rt')
    count_child = int(file.readline())
    appetites = [int(x) for x in file.readline().split()]
    count_cookies = int(file.readline())
    size_cookies = [int(x) for x in file.readline().split()]
    return appetites, size_cookies


if __name__ == '__main__':
    app, size = load_data()
    app.sort()
    size.sort()

    print(app)
    print(size)

    s = sum(size)

    count = 0
    for x in app:
        if s == x:
            count += 1
    print(count)