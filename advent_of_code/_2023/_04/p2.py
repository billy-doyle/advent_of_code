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

    def get_matching_nums(self):
        ct = 0
        for i in self.our_nums:
            if i in self.winning_nums:
                ct += 1

        return ct


def main():

    path = DATA_PATH_2023 / "04.txt"

    with open(path, "r") as f:
        data = f.read()

    lines = data.strip().split("\n")
    final = [1] * len(lines)

    for i, line in enumerate(lines):
        # print(line.strip().split(":"))
        card = ScratchCard.process(line)
        n_matches = card.get_matching_nums()
        for j in range(i + 1, i + 1 + n_matches):
            final[j] += final[i]

    print(sum(final))


if __name__ == "__main__":
    main()
