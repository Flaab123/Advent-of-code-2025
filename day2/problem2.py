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
    print(invalid_numbers)
    print(f"The answer to problem 2 is: {sum(invalid_numbers)}")
    return invalid_numbers

def number_is_invalid(nr: int) -> bool:
    number_string = str(nr)
    number_of_digits = len(number_string)
    
    for divisor in get_valid_divisors(nr):
        number_parts = [number_string[div*divisor:(div+1)*divisor] for div in range(int(number_of_digits/divisor))]
        if len(set(number_parts)) == 1:
            return True
    return False

def get_valid_divisors(nr: int) -> list[int]:
    valid_divisors = []
    number_length = len(str(nr))
    for length_to_check in range(1,int(number_length/2)+1):
        if number_length % length_to_check == 0:
            valid_divisors.append(length_to_check)
    return valid_divisors

if __name__ == "__main__":
    main()