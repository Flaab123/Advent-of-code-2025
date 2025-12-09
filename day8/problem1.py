COORDS_INPUT_PATH = "input.txt"
N_PAIRS = 1000


def main():
    coords = read_coords(path=COORDS_INPUT_PATH)
    distance_mapping = calculate_and_sort_distances(coords=coords)
    coord_pairs = get_top_n_coord_pairs(distance_mapping=distance_mapping)
    circuits = get_circuits(coord_pairs)
    
    circuit_lengths = [len(circ) for circ in circuits]
    circuit_lengths.sort()
    circuit_lengths = circuit_lengths[::-1]
    result = 1
    for length in circuit_lengths[0:3]:
        result = result * length
    print(result)

    return


def read_coords(path: str) -> list[tuple[int, ...]]:
    coords = []
    with open(path, "r") as file:
        for line in file.readlines():
            parsed_coords = [int(coord) for coord in line.split(",")]
            coords.append(tuple(parsed_coords))
    return coords


def calculate_and_sort_distances(coords: list[tuple[int, ...]]) -> list[tuple[tuple[tuple[int, ...], ...], int]]:
    distances = []
    for idx, coords_1 in enumerate(coords[:-1]):
        for coords_2 in coords[idx + 1 :]:
            distance = (
                (coords_1[0] - coords_2[0]) ** 2 + (coords_1[1] - coords_2[1]) ** 2 + (coords_1[2] - coords_2[2]) ** 2
            )
            distances.append(tuple([tuple([coords_1, coords_2]), distance]))
    distances.sort(key=lambda x: x[1])
    return distances


def get_top_n_coord_pairs(
    distance_mapping: list[tuple[tuple[tuple[int, ...], ...], int]],
) -> list[tuple[tuple[int, ...], ...]]:
    coord_pairs = []
    filtered_distances = distance_mapping[0:N_PAIRS]
    for mapping in filtered_distances:
        coord_pairs.append(mapping[0])
    return coord_pairs


def get_circuits(coord_pairs: list[tuple[tuple[int, ...], ...]]) -> list[set[tuple]]:
    circuits: list[set] = []
    for pair in coord_pairs:
        coords_1 = pair[0]
        coords_2 = pair[1]

        circuits.append(set([coords_1, coords_2]))
        circuits = check_and_merge_circuits(circuits)
    return circuits


def check_and_merge_circuits(circuits: list[set]) -> list[set]:
    if len(circuits) == 1:
        return circuits

    merged_circuits = []
    circuits_were_merged = True
    while circuits_were_merged:
        circuits_were_merged = False
        merged_circuits = circuits
        for idx, circuit_1 in enumerate(circuits[:-1]):
            for circuit_2 in circuits[idx + 1 :]:
                if circuit_1.intersection(circuit_2):
                    merged_circuits.remove(circuit_1)
                    merged_circuits.remove(circuit_2)
                    merged_circuits.append(circuit_1.union(circuit_2))
                    circuits_were_merged = True
                    break
            if circuits_were_merged:
                break

    return merged_circuits


if __name__ == "__main__":
    main()
