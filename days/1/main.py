def load_input(file_path: str) -> list[tuple[str, int]]:
    data: list[tuple[str, int]] = []
    with open(file_path, "r") as file:
        for line in file:
            direction, value = line[0], line[1:].strip()
            data.append((direction, int(value)))
    return data


def evaluate_dial(data: list[tuple[str, int]]) -> int:
    """Returns the amount of times the dial points to 0 after rotating."""
    count = 0
    position = 50
    for direction, k in data:
        if direction == "L":
            position -= k
        elif direction == "R":
            position += k
        position %= 100
        if position == 0:
            count += 1
    return count


def zeros(position: int, step: int, k: int) -> int:
    normalized_position = (-position * step) % 100
    if normalized_position == 0:
        normalized_position = 100
    if normalized_position > k:
        return 0
    return 1 + (k - normalized_position) // 100


def part_two(data: list[tuple[str, int]]) -> int:
    count = 0
    position = 50
    for direction, k in data:
        step = 1 if direction == "R" else -1
        count += zeros(position, step, k)
        position = (position + step * k) % 100

    return count


if __name__ == "__main__":
    example = load_input("days/1/example.txt")
    input_data = load_input("days/1/input.txt")

    example_result = evaluate_dial(example)
    input_result = evaluate_dial(input_data)
    print(f"example: {example_result}")  # 3
    print(f"input: {input_result}")  # 1145

    input_result_part_two = part_two(input_data)
    print(f"part two input: {input_result_part_two}")  # 6561

    assert example_result == 3
    assert input_result == 1145
    assert input_result_part_two == 6561
