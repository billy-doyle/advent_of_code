from advent_of_code.utils.constants import DATA_PATH_2023


def main():

    path = DATA_PATH_2023 / "01.txt"
    lst = []
    with open(path, "r") as f:
        for line in f.readlines():
            line_lst = []
            for char in line:
                if char.isdigit():
                    line_lst.append(char)

            lst.append(int(line_lst[0] + line_lst[-1]))

    print(sum(lst))


if __name__ == "__main__":
    main()
