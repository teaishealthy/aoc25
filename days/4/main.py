from typing import Sequence

EMPTY = "."
ROLL = "@"

Grid = Sequence[Sequence[str]]


def load_input(file_path: str) -> Grid:
    data: Grid = []
    with open(file_path, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def index_or_zero(x: int, y: int, grid: Grid) -> str:
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        return grid[y][x]
    return EMPTY


def get_surrounding_positions(x: int, y: int, grid: Grid) -> int:
    positions = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1),
    ]

    count = 0
    for pos_x, pos_y in positions:
        if index_or_zero(pos_x, pos_y, grid) == ROLL:
            count += 1
    return count


def evaluate_grid(grid: Sequence[Sequence[str]]) -> int:
    count = 0
    for x, _ in enumerate(grid[0]):
        for y, _ in enumerate(grid):
            if index_or_zero(x, y, grid) != ROLL:
                continue
            surrounding_rolls = get_surrounding_positions(x, y, grid)
            if surrounding_rolls < 4:
                count += 1
    return count


def evaluate_grid_part_two(grid: Grid) -> int:
    # fast enough for input size
    count = 0
    changed = True

    list_grid: Grid = [list(row) for row in grid]
    while changed:
        changed = False
        for x, _ in enumerate(list_grid[0]):
            for y, _ in enumerate(list_grid):
                if index_or_zero(x, y, list_grid) != ROLL:
                    continue
                surrounding_rolls = get_surrounding_positions(x, y, list_grid)
                if surrounding_rolls < 4:
                    count += 1
                    list_grid[y][x] = EMPTY
                    changed = True
    return count


if __name__ == "__main__":
    example = load_input("days/4/example.txt")
    example_result = evaluate_grid(example)
    print(f"example: {example_result}")  # 13
    assert example_result == 13

    input_data = load_input("days/4/input.txt")
    input_result = evaluate_grid(input_data)
    print(f"input: {input_result}")  # 1464
    assert input_result == 1464

    example_result_part_two = evaluate_grid_part_two(example)
    print(f"example part two: {example_result_part_two}")  # 43
    assert example_result_part_two == 43

    input_result_part_two = evaluate_grid_part_two(input_data)
    print(f"input part two: {input_result_part_two}")  # 4245
