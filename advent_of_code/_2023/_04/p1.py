from dataclasses import dataclass

from advent_of_code.utils.constants import DATA_PATH_2023


@dataclass
class ScratchCard:
    card_id: int
    winning_nums: set[int]
    our_nums: set[int]

    @classmethod
    def process(cls, data):
        card, nums = data.strip().split(":")
        card_id = int(card.split("Card")[-1].strip())
        win_nums, our_nums = nums.split("|")
        parsed_win_nums = {
            int(i) for i in win_nums.strip().replace("  ", " ").split(" ")
        }
        parsed_our_nums = {
            int(i) for i in our_nums.strip().replace("  ", " ").split(" ")
        }

        return cls(
            card_id=card_id, winning_nums=parsed_win_nums, our_nums=parsed_our_nums
        )

    def get_score(self):
        ct = 0
        for i in self.our_nums:
            if i in self.winning_nums:
                ct += 1

        return 2 ** (ct - 1) if ct != 0 else 0


def main():

    path = DATA_PATH_2023 / "04.txt"
    total = 0
    with open(path, "r") as f:
        for line in f.readlines():
            total += ScratchCard.process(line).get_score()

    print(total)


if __name__ == "__main__":
    main()
