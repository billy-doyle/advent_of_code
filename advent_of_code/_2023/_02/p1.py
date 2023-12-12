from advent_of_code._2023._02.dc import Bag, Game
from advent_of_code.utils.constants import DATA_PATH_2023


def main():

    tot = 0
    master_bag = Bag(red=12, green=13, blue=14)
    path = DATA_PATH_2023 / "02.txt"
    with open(path, "r") as f:
        for line in f.readlines():
            gp = Game.process(line)
            tot += gp._id if gp.is_valid(master_bag) else 0

    print(tot)


if __name__ == "__main__":
    main()
