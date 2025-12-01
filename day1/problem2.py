INPUT_FILE = "input.txt"
START_POSITION = 50
DIAL_MAX = 100  # Max of dial is 99, but we need to increase by 1 so a dial value of 100 resets to 0

current_position = START_POSITION
zero_crossings = 0

with open(INPUT_FILE, "r") as file:
    for line in file.readlines():
        instruction = line[0]
        dial_moves = int(line[1:])

        for move in range(dial_moves):
            if instruction == "L":
                move = -1
            else:
                move = 1
            current_position = (current_position + move) % DIAL_MAX
            if current_position == 0:
                zero_crossings += 1

print(zero_crossings)

# 0 -> -100 (0) => 1
# 0 -> +100 (0) => 1
