from advent_of_code.utils.constants import DATA_PATH_2023


def replace_word_int(line):

    words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for word, num in words.items():
        line = line.replace(word, f"{word}{num}{word}")

    return line


def main():

    path = DATA_PATH_2023 / "01.txt"
    lst = []
    with open(path, "r") as f:
        for line in f.readlines():
            line_lst = []
            line = replace_word_int(line)
            for char in line:
                if char.isdigit():
                    line_lst.append(char)

            lst.append(int(line_lst[0] + line_lst[-1]))

    print(sum(lst))


if __name__ == "__main__":
    main()
