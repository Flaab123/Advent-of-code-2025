from collections import defaultdict

MANIFOLD_INPUT_PATH = "input.txt"


def main():
    manifold = read_manifold_input(path=MANIFOLD_INPUT_PATH)
    entry_id = get_manifold_beam_entry(manifold=manifold)
    final_indexes = propagate_beam(manifold=manifold, entry_idx=entry_id)
    print(sum(final_indexes.values()))
    return


def read_manifold_input(path: str) -> list[list[str]]:
    with open(path, "r") as file:
        parsed_file = [line.split()[0] for line in file.readlines()]
    manifold = []
    for line in parsed_file:
        new_line = []
        for char in line:
            new_line.append(char)
        manifold.append(new_line)
    return manifold


def get_manifold_beam_entry(manifold: list[list[str]]) -> int:
    first_line = manifold[0]
    return first_line.index("S")


def propagate_beam(manifold: list[list[str]], entry_idx: int) -> dict[int, int]:
    beam_indexes: dict[int, int] = defaultdict(int)
    beam_indexes[entry_idx] += 1
    for line in manifold:
        new_beam_indexes = defaultdict(int)
        for index, value in beam_indexes.items():
            if line[index] == "^":
                new_beam_indexes[index - 1] += value
                new_beam_indexes[index + 1] += value
            else:
                new_beam_indexes[index] += value
        beam_indexes = new_beam_indexes
    return beam_indexes


if __name__ == "__main__":
    main()
