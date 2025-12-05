from typing import Callable


def load_input(file_path: str) -> list[range]:
    data: list[range] = []
    with open(file_path, "r") as file:
        for range_ in file.read().split(","):
            start, end = range_.strip().split("-")
            data.append(range(int(start), int(end) + 1))
    return data


def evaluate_ranges(data: list[range], f: Callable[[str], bool]) -> int:
    return sum(i for r in data for i in r if f(str(i)))


def is_repeated_part_two(string: str) -> bool:
    return string in (string + string)[1:-1]


def is_repeated(string: str) -> bool:
    if len(string) % 2 == 1:
        return False

    mid = len(string) // 2
    return string[:mid] == string[mid:]


if __name__ == "__main__":
    example = load_input("days/2/example.txt")
    input_data = load_input("days/2/input.txt")

    example_result = evaluate_ranges(example, is_repeated)
    input_result = evaluate_ranges(input_data, is_repeated)

    print(f"example: {example_result}")  # 1227775554
    print(f"input: {input_result}")  # 24043483400

    example_result_part_two = evaluate_ranges(example, is_repeated_part_two)
    input_result_part_two = evaluate_ranges(input_data, is_repeated_part_two)

    print("example part two:", example_result_part_two)  # 4174379265
    print("input part two:", input_result_part_two)  # 38262920235

    assert example_result == 1227775554
    assert input_result == 24043483400
    assert example_result_part_two == 4174379265
    assert input_result_part_two == 38262920235
