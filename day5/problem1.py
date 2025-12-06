RANGES_INPUT_FILE = "input_ranges.txt"
INGREDIENTS_INPUT_FILE = "input_ingredients.txt"


def main():
    ranges = read_and_create_ranges(RANGES_INPUT_FILE)
    ingredients = read_and_create_ingredients(INGREDIENTS_INPUT_FILE)
    fresh_ingredients = get_fresh_ingredients(ingredients=ingredients, ranges=ranges)
    print(len(fresh_ingredients))
    return


class Range:
    def __init__(self, input_string: str):
        self.lower_number = int(input_string.split("-")[0])
        self.higher_number = int(input_string.split("-")[1])
        pass

    def check_ingredient_is_fresh(self, ingredient: int) -> bool:
        if ingredient >= self.lower_number and ingredient <= self.higher_number:
            return True
        return False


def read_and_create_ranges(filepath: str) -> list[Range]:
    ranges = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            ranges.append(Range(input_string=line))
    return ranges


def read_and_create_ingredients(filepath: str) -> list[int]:
    ingredients = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            ingredients.append(int(line))
    return ingredients


def get_fresh_ingredients(ingredients: list[int], ranges: list[Range]) -> list[int]:
    fresh_ingredients = []
    for ingredient in ingredients:
        for freshness_range in ranges:
            if freshness_range.check_ingredient_is_fresh(ingredient):
                fresh_ingredients.append(ingredient)
                break
    return fresh_ingredients


if __name__ == "__main__":
    main()
