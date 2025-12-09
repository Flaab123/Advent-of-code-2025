COORDS_INPUT_PATH = "input.txt"
TEST_INPUT_PATH = "test_input.txt"


def main():
    coords = read_coords(path=COORDS_INPUT_PATH)
    areas = calculate_and_sort_areas(coords)
    print(max(areas))
    return


def read_coords(path: str) -> list[tuple[int, ...]]:
    coords = []
    with open(path, "r") as file:
        for line in file.readlines():
            parsed_coords = [int(coord) for coord in line.split(",")]
            coords.append(tuple(parsed_coords))
    return coords


def calculate_and_sort_areas(coords: list[tuple[int, ...]]) -> list[tuple[tuple[tuple[int, ...], ...], int]]:
    areas = []
    for idx, coords_1 in enumerate(coords[:-1]):
        for coords_2 in coords[idx + 1 :]:
            area = (abs(coords_1[0] - coords_2[0]) + 1) * (abs(coords_1[1] - coords_2[1]) + 1)
            areas.append(area)
    return areas


if __name__ == "__main__":
    main()
