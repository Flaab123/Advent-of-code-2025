INPUT_FILE = "input.txt"


def main():
    max_joltages: list[int] = []
    input_numbers: list[str] = []

    with open(INPUT_FILE, "r") as file:
        input_numbers = [line.strip("\n") for line in file.readlines()]

    for number in input_numbers:
        max_joltages.append(get_joltage(number, 12))

    print(f"solution is {sum(max_joltages)}")
    return


def get_joltage(number: str, joltage_length: int) -> int:
    joltage_chars = ""
    joltage_idx = 0
    current_joltage_number_idx = -1
    while joltage_idx < joltage_length:
        last_joltage_idx = current_joltage_number_idx
        if (joltage_length - 1 - joltage_idx) == 0:
            string_to_search = number[current_joltage_number_idx + 1 :]
        else:
            string_to_search = number[current_joltage_number_idx + 1 : -1 * (joltage_length - 1 - joltage_idx)]
        highest_nr = 0
        for idx, char in enumerate(string_to_search):
            if int(char) > highest_nr:
                highest_nr = int(char)
                current_joltage_number_idx = last_joltage_idx + 1 + idx
        joltage_chars += str(highest_nr)
        joltage_idx += 1
    return int(joltage_chars)


if __name__ == "__main__":
    main()
