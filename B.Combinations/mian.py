from typing import List

key_board = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def load_data() -> str:
    file = open('./input.txt', 'rt')
    return file.read()


def generate_word(n: str, prefix: str, arrs: List) -> None:
    if n == '':
        arrs.append(prefix)
        return
    for letter in key_board[int(n[0])]:
        prefix += letter
        generate_word(n[1:], prefix, arrs)
        prefix = prefix[:-1]


if __name__ == '__main__':
    cmd = load_data()
    arr = []
    generate_word(cmd, '', arr)
    print(' '.join(map(str, arr)))
