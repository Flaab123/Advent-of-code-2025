INPUT_FILE = "input.txt"
START_POSITION = 50
DIAL_MAX = 100  # Max of dial is 99, but we need to increase by 1 so a dial value of 100 resets to 0

all_positions: list[int] = [START_POSITION]
with open(INPUT_FILE, "r") as file:
    current_position = START_POSITION
    for line in file.readlines():
        instruction = line[0]
        dial_moves = int(line[1:])
        if instruction == "L":
            dial_moves = -1 * dial_moves

        current_position = (current_position + dial_moves) % DIAL_MAX
        all_positions.append(current_position)

print(sum([x == 0 for x in all_positions]))
