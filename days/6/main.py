import functools
from operator import add, mul

OPERATORS = {
    "*": mul,
    "+": add,
}

def load_data(file_path: str) -> list[list[str]]:
    with open(file_path, "r") as file:
        rows = [line.split() for line in file.readlines()]

    return list(map(list, zip(*rows)))

def parse_fixed_width_data(file_path: str, widths: list[int]) -> list[list[str]]:
    with open(file_path, "r") as f:
        data: list[list[str]] = []

        for line in f:
            line = line.rstrip("\n")

            start = 0
            row: list[str] = []
            for width in widths:
                row.append(line[start : start + width])
                start += width + 1 # +1 for the space
            data.append(row)

    return list(map(list, zip(*data)))

def calculate_column_widths(data_part_one: list[list[str]]) -> list[int]:
    widths = [max(len(item) for item in col) for col in data_part_one]
    return widths

def calculate_column(data: list[list[str]]) -> int:
    total = 0
    for column in data:
        operand = column[-1]
        op = OPERATORS[operand]
        total += functools.reduce(op, map(int, column[:-1]))
    return total

def calculate_column_part_two(data: list[list[str]]) -> int:
    total = 0
    for column in data:
        operand = column[-1]
        op = OPERATORS[operand.strip()]

        total += functools.reduce(
            op, [int("".join(group)) for group in zip(*column[:-1])]
        )
    return total

if __name__ == "__main__":
    example_data = load_data("days/6/example.txt")
    example_result = calculate_column(example_data)
    print(f"example: {example_result}")  # 4277556
    assert example_result == 4277556

    data = load_data("days/6/input.txt")
    result = calculate_column(data)
    print(f"result: {result}")  # 5171061464548
    assert result == 5171061464548

    example_data_part_two = parse_fixed_width_data("days/6/example.txt", calculate_column_widths(example_data))
    example_result_part_two = calculate_column_part_two(example_data_part_two)
    print(f"example part two: {example_result_part_two}")  # 3263827
    assert example_result_part_two == 3263827

    data_part_two = parse_fixed_width_data("days/6/input.txt", calculate_column_widths(data))
    result_part_two = calculate_column_part_two(data_part_two)
    print(f"result part two: {result_part_two}")  # 10189959087258
    assert result_part_two == 10189959087258