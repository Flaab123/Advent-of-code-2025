INPUT_FILE = "input.txt"
grid_lines: list[list[str]] = []



class Grid:
    directions = [
        [1,1],
        [-1,-1],
        [-1,1],
        [1,-1],
        [0,1],
        [0,-1],
        [1,0],
        [-1,0],
    ]
    available_cells = 0

    def __init__(self) -> None:
        with open(INPUT_FILE, "r") as file:
            self.grid = [[char for char in line.strip("\n")] for line in file.readlines()]

        self.grid_width = len(self.grid[0])
        self.grid_height = len(self.grid)


    def find_available_cells(self) -> None:
        for row_idx, _ in enumerate(self.grid):
            for col_idx, _ in enumerate(self.grid[row_idx]):
                neighbour_values = self._get_neighboring_cells(row_coord=row_idx, col_coord=col_idx)
                if neighbour_values.count("@") < 4 and self.grid[row_idx][col_idx] == "@":
                    self.available_cells += 1

    def _get_neighboring_cells(self, row_coord:int, col_coord:int) -> list[str | None]:
        cell_values = []
        for direction in self.directions:
            new_row_coord = row_coord + direction[0]
            new_col_coord = col_coord + direction[1]
            if new_col_coord < 0 or new_col_coord > self.grid_width-1:
                continue
            if new_row_coord < 0 or new_row_coord > self.grid_height -1:
                continue
            cell_values.append(self.grid[new_row_coord][new_col_coord])
        return cell_values


def main():
    grid = Grid()
    cells = grid.find_available_cells()
    print(grid.available_cells)

if __name__ == "__main__":
    main()