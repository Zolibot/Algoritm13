def load_data():
    file = open('./input.txt', 'rt')
    return int(file.read())


def generate_bracket(cp: int, first: int, second: int, prefix: str) -> None:
    if first == 0 and second == 0:
        print(prefix)
    else:
        if first > 0:
            generate_bracket(cp + 1, first - 1, second, prefix + '(')
        if cp > 0 and second > 0:
            generate_bracket(cp - 1, first, second - 1, prefix + ')')


if __name__ == '__main__':
    d = load_data()
    generate_bracket(0, d, d, '')
