INPUT_FILE = "input.txt"


def main():
    max_joltages: list[int] = []
    input_numbers: list[str] = []

    with open(INPUT_FILE, "r") as file:
        input_numbers = [line.strip("\n") for line in file.readlines()]

    for number in input_numbers:
        max_joltages.append(get_joltage(number))

    print(f"solution is {sum(max_joltages)}")
    return


def get_joltage(number: str) -> int:
    highest_nr = 0
    higher_nr_idx = 0
    for idx, char in enumerate(number[:-1]):
        if int(char) > highest_nr:
            highest_nr = int(char)
            higher_nr_idx = idx

    second_highest_nr = 0
    for char in number[higher_nr_idx + 1 :]:
        if int(char) > second_highest_nr:
            second_highest_nr = int(char)

    return int(str(highest_nr) + str(second_highest_nr))


if __name__ == "__main__":
    main()
