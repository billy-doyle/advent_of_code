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

    def power(self):
        tot = 1
        for _, value in self:
            tot *= value

        return tot


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

    def min_bag(self):
        d = {}
        for field in fields(Bag):
            color = field.name
            d[color] = getattr(
                max(self.bag_list, key=lambda x: getattr(x, color)), color
            )

        return Bag(**d)


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
