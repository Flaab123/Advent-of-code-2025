SCROLL_INPUT_FILE = "input.txt"

def main():
    scroll = read_scroll_input(SCROLL_INPUT_FILE)
    math_problems = process_instructions(scroll)
    solutions = solve_math_problems(math_problems=math_problems)
    print(sum(solutions))


class MathProblem:
    def __init__(self, number_strings: list[str], operation: str) -> None:
        self.numbers = [int(number) for number in number_strings]
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

def read_scroll_input(path: str) -> list[list[str]]:
    with open(path, "r") as file:
        scroll = [line.split() for line in file.readlines()]
    return scroll

def process_instructions(scroll: list[list[str]]) -> list[MathProblem]:
    scroll_problems = len(scroll[0])
    math_problems = []
    for problem in range(scroll_problems):
        numbers = [line[problem] for line in scroll[:-1]]
        operation = scroll[-1][problem]
        math_problems.append(MathProblem(number_strings=numbers, operation=operation))
    return math_problems

def solve_math_problems(math_problems: list[MathProblem]) -> list[int]:
    return [math_problem.solve_problem() for math_problem in math_problems]

if __name__ == "__main__":
    main()