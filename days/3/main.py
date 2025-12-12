def load_input(file_path: str) -> list[str]:
    data: list[str] = []
    with open(file_path, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def largest_concatenation_subsequence(batteries: list[int], n: int) -> int:
    m = len(batteries)

    len_one_values = batteries[:]

    for length in range(2, n + 1):
        current_values = [0] * m
        start = length - 2

        for end in range(length - 1, m):
            battery_value = batteries[end]
            best_value = 0

            for previous_index in range(start, end):
                composed_value = len_one_values[previous_index] * 10 + battery_value
                if composed_value > best_value:
                    best_value = composed_value

            current_values[end] = best_value

        len_one_values = current_values
    return max(len_one_values)


def largest_possible_joltage(data: list[str], n: int) -> int:
    total = 0
    for bank in data:
        batteries = list(map(int, bank))
        total += largest_concatenation_subsequence(batteries, n)
    return total


if __name__ == "__main__":
    example = load_input("days/3/example.txt")
    input_data = load_input("days/3/input.txt")

    example_result = largest_possible_joltage(example, 2)
    print(f"example: {example_result}")  # 357
    assert example_result == 357

    input_result = largest_possible_joltage(input_data, 2)
    print(f"input: {input_result}")  # 17359
    assert input_result == 17359

    example_result_part_two = largest_possible_joltage(example, 12)
    print(f"example part two: {example_result_part_two}")  # 3121910778619
    assert example_result_part_two == 3121910778619

    input_result_part_two = largest_possible_joltage(input_data, 12)
    print(f"input part two: {input_result_part_two}")  # 172787336861064
    assert input_result_part_two == 172787336861064
