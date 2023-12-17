import re
from dataclasses import dataclass, fields

from advent_of_code.utils.constants import DATA_PATH_2023


@dataclass
class Race:
    time: int
    distance: int

    def is_win(self, n_millis):
        time_left = self.time - n_millis
        distance_traveled = 0
        for _ in range(time_left):
            distance_traveled += n_millis
        return distance_traveled > self.distance

    def count_wins(self):
        wins = 0
        for time in range(1, self.time):
            wins += self.is_win(time)
        return wins


@dataclass
class Races:
    races: list[Race]

    def __iter__(self):
        for field in fields(self):
            yield getattr(self, field.name)

    @classmethod
    def process(cls, data):
        times, dists = data.strip().split("\n")
        lst = []
        pat = r".*:\s+(\d+(?:\s+\d+)*)"
        for t, d in zip(
            [int(i) for i in re.search(pat, times).group(1).split()],
            [int(i) for i in re.search(pat, dists).group(1).split()],
        ):
            lst.append(Race(time=t, distance=d))

        return cls(races=lst)

    @classmethod
    def process_2(cls, data):
        times, dists = data.strip().split("\n")
        pat = r".*:\s+(\d+(?:\s+\d+)*)"
        return cls(
            [
                Race(
                    time=int(re.search(pat, times).group(1).replace(" ", "")),
                    distance=int(re.search(pat, dists).group(1).replace(" ", "")),
                ),
            ]
        )


def part_1(data):

    wins = 1
    for race in Races.process(data).races:
        wins *= race.count_wins()

    return wins


def part_2(data):

    return Races.process_2(data).races[0].count_wins()


def main():

    path = DATA_PATH_2023 / "06.txt"

    with open(path) as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))


main()
