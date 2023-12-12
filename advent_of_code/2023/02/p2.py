from dc import Game
from advent_of_code.utils.constants import DATA_PATH_2023


def main():

    tot = 0
    path = DATA_PATH_2023 / "02.txt"
    with open(path, "r") as f:
        for line in f.readlines():
            gp = Game.process(line)
            tot += gp.min_bag().power()

    print(tot)


if __name__ == "__main__":
    main()
