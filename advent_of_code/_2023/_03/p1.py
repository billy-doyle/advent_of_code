import re

from advent_of_code.utils.constants import DATA_PATH_2023


def main():

    path = DATA_PATH_2023 / "03.txt"

    with open(path) as f:
        board = [i.strip() for i in f.readlines()]

    chars = {}
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] not in ".01234566789":
                chars[(row, col)] = []

    for i, row in enumerate(board):
        for num in re.finditer(r"\d+", row):
            edge = {
                (i, c)
                for i in (i - 1, i, i + 1)
                for c in range(num.start() - 1, num.end() + 1)
            }
            for o in edge.intersection(chars.keys()):
                chars[o].append(int(num.group()))

    tot = 0
    for p in chars.values():
        tot += sum(p)

    print(tot)


if __name__ == "__main__":
    main()
