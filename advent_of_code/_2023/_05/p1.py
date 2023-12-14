from collections import Counter

from advent_of_code.utils.constants import DATA_PATH_2023

path = DATA_PATH_2023 / "05.txt"

with open(path) as f:
    data = f.read()

spl = data.split("\n\n")
seeds = spl[0]
maps = spl[1:]

d = {}
for line in maps:
    i = line.split("\n")
    key, _ = i[0].split(" ")
    d[key] = []
    nums = []
    for j in i[1:]:
        x = [int(x) for x in j.split()]
        nums.append(x)
    d[key].extend(nums)

d[key].pop()
int_seeds = [int(i) for i in seeds.split()[1:]]


def seed_to_blah(
    seed_num,
    dest_range_start,
    source_range_start,
    range_length,
):

    source_range_end = source_range_start + range_length - 1
    if source_range_start <= seed_num <= source_range_end:
        shift = dest_range_start - source_range_start
        return seed_num + shift

    return seed_num


locations = []
for seed in int_seeds:

    for conversion, conversion_vals in d.items():
        test = []
        for mapping in conversion_vals:
            test.append(seed_to_blah(seed, *mapping))

        c = Counter(test)
        seed = c.most_common()[-1][0]

    locations.append(seed)

print(min(locations))
