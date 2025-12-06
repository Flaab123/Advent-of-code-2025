SCROLL_INPUT_FILE = "input.txt"

def main():
    scroll = read_scroll_input(SCROLL_INPUT_FILE)
    math_problems = process_instructions(scroll)
    solutions = solve_math_problems(math_problems=math_problems)
    print(sum(solutions))


class MathProblem:
    def __init__(self, number_strings: list[str], operation: str) -> None:
        self.numbers = self.parse_numbers(number_strings)
        self.operation = operation
        pass

    def solve_problem(self) -> int:
        match self.operation:
            case "+":
                return sum(self.numbers)
            case "*":
                start = 1
                for num in self.numbers:
                    start = num * start
                return start
            case _:
                return 99999999999999999999999999999
            
    @staticmethod
    def parse_numbers(number_strings: list[str]) -> list[int]:
        longest_number = max([len(num) for num in number_strings])
        new_numbers = []

        for r_to_l_idx in range(longest_number):
            new_number = ""

            for orig_num in number_strings:
                try:
                    digit = orig_num[-1-r_to_l_idx]
                    if digit == " ":
                        digit = ""
                except IndexError:
                    digit = ""
                new_number += digit
            new_numbers.append(new_number)
        return [int(num) for num in new_numbers]
        
def read_scroll_input(path: str) -> list[str]:
    with open(path, "r") as file:
        scroll = [line.strip("\n") for line in file.readlines()]
    return scroll

def process_instructions(scroll: list[str]) -> list[MathProblem]:
    operations = scroll[-1]
    operations_indexes = []
    for idx, char in enumerate(operations):
        if char != " ":
            operations_indexes.append(idx)
    operations = operations.split()

    scroll_problems = len(operations)
    white_spaces_to_skip = [idx - 1 for idx in operations_indexes if idx != 0]
    white_spaces_to_skip.append(len(scroll[0]))

    math_problems = []
    for problem_idx in range(scroll_problems):
        numbers = [get_characters_from_line(line, problem_idx, operations_indexes, white_spaces_to_skip) for line in scroll[:-1]]
        operation = operations[problem_idx]
        math_problems.append(MathProblem(number_strings=numbers, operation=operation))
    return math_problems

def get_characters_from_line(line: str, problem_number: int, operations_indexes: list[int], skip_indexes: list[int]):
    idx_to_get = operations_indexes[problem_number]
    chars = line[idx_to_get]
    while True:
        idx_to_get += 1
        if idx_to_get in skip_indexes:
            break
        chars += line[idx_to_get]
    return chars


def solve_math_problems(math_problems: list[MathProblem]) -> list[int]:
    return [math_problem.solve_problem() for math_problem in math_problems]

if __name__ == "__main__":
    main()