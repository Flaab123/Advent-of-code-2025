RANGES_INPUT_FILE = "input_ranges.txt"
INGREDIENTS_INPUT_FILE = "input_ingredients.txt"

def main():
    ranges = read_and_create_ranges(RANGES_INPUT_FILE)
    merged_ranges = merge_overlapping_ranges(ranges)
    valid_ids = 0
    for rng in merged_ranges:
        valid_ids += rng.amount_of_valid_ids()
    return merged_ranges

class Range:
    def __init__(self, input_string: str | None = None, lower_number: int | None = None, higher_number: int| None = None):
        if input_string:
            self.lower_number = int(input_string.split("-")[0])
            self.higher_number = int(input_string.split("-")[1])
            return
        if lower_number and higher_number:
            self.lower_number = lower_number
            self.higher_number = higher_number
            return
        raise ValueError()

    def amount_of_valid_ids(self) -> int:
        return self.higher_number - self.lower_number + 1
    
def read_and_create_ranges(filepath:str) -> list[Range]:
    ranges = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            ranges.append(Range(input_string=line))
    return ranges

def check_if_ranges_overlap(range1: Range, range2: Range) -> bool:
    if range1.lower_number <= range2.higher_number and range1.higher_number >= range2.lower_number:
        return True
    return False

def merge_overlapping_ranges(ranges: list[Range]) -> list[Range]:
    ranges_were_merged = True
    while ranges_were_merged:
        ranges_were_merged = False
        for idx, range_to_check in enumerate(ranges):
            for idx_other_ranges, range_to_check_against in enumerate(ranges):  
                if idx == idx_other_ranges:
                    continue
                if check_if_ranges_overlap(range_to_check, range_to_check_against):
                    ranges.pop(idx_other_ranges)
                    ranges.pop(idx)
                    new_range = Range(lower_number=min([range_to_check.lower_number,range_to_check_against.lower_number]), 
                                      higher_number=max([range_to_check.higher_number,range_to_check_against.higher_number]))
                    ranges.append(new_range)
                    ranges_were_merged = True
                    break
            if ranges_were_merged:
                break
    return ranges

if __name__ == "__main__":
    ranges = main()
    

# test_ranges = [
#     Range(lower_number=1,higher_number=20),
#     Range(lower_number=8,higher_number=30),
#     Range(lower_number=24,higher_number=25),
#     Range(lower_number=25,higher_number=75),
#     Range(lower_number=55,higher_number=60),
#     Range(lower_number=44,higher_number=53),
#     Range(lower_number=80,higher_number=100),
# ]
# new_ranges = merge_overlapping_ranges(test_ranges)

