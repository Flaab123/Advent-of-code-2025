INPUT_FILE = "input.txt"


def main():
    invalid_numbers: list[int] = []

    with open(INPUT_FILE, "r") as file:
        line = file.readline()

    ranges = line.split(",")

    for nr_range in ranges:
        first_nr = int(nr_range.split("-")[0])
        last_nr = int(nr_range.split("-")[1])
        for number_to_check in range(first_nr, last_nr +1):
            if number_is_invalid(number_to_check):
                invalid_numbers.append(number_to_check)

    print(f"The answer to problem 1 is: {sum(invalid_numbers)}")
    return

def number_is_invalid(nr: int) -> bool:
    number_string = str(nr)

    if len(number_string) % 2 == 1: # odd length number
        return False
    
    first_half = number_string[0:int(len(number_string)    / 2)]
    second_half = number_string[int(len(number_string)    / 2) :]

    if first_half == second_half:
        return True
    
    return False

if __name__ == "__main__":
    main()