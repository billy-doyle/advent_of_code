from dataclasses import dataclass, fields

from advent_of_code.utils.constants import DATA_PATH_2023


@dataclass
class Bag:
    red: int = 0
    blue: int = 0
    green: int = 0

    def __iter__(self):
        for field in fields(self):
            yield field.name, getattr(self, field.name)


@dataclass
class Game:
    _id: int
    bag_list: list[Bag]

    @classmethod
    def process(cls, raw):
        _id, game = raw.strip().split(": ")
        _, game_id = _id.split(" ")
        bag_lst = []
        for game in game.split("; "):
            d = {}
            for each in game.split(", "):
                num, color = each.split(" ")
                d[color] = int(num)
            bag_lst.append(Bag(**d))

        return cls(_id=int(game_id), bag_list=bag_lst)

    def is_valid(self, master_bag):

        for color, value in master_bag:
            for bag in self.bag_list:
                remaining = value - getattr(bag, color)
                if remaining < 0:
                    return False

        return True


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
