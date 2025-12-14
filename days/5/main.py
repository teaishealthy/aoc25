from dataclasses import dataclass


@dataclass()
class Range:
    start: int
    end: int

    def __contains__(self, item: int) -> bool:  # type: ignore
        return self.start <= item <= self.end


def load_data(file_path: str) -> tuple[list[Range], list[int]]:
    with open(file_path, "r") as file:
        data = file.read()

    ranges: list[Range] = []
    numbers: list[int] = []

    ranges_unparsed, numbers_unparsed = data.split("\n\n")

    for line in ranges_unparsed.splitlines():
        start_str, end_str = line.split("-")
        ranges.append(Range(int(start_str), int(end_str) + 1))

    for number_str in numbers_unparsed.splitlines():
        numbers.append(int(number_str))

    return ranges, numbers


def count_fresh_ingredients(ranges: list[Range], numbers: list[int]) -> int:
    fresh_count = 0
    for number in numbers:
        if any(number in r for r in ranges):
            fresh_count += 1
    return fresh_count


def part_two(ranges: list[Range], _: list[int]) -> int:
    ranges = sorted(ranges, key=lambda r: r.start)
    start_range = ranges.pop(0)
    total = start_range.end - start_range.start
    current_end = start_range.end

    while ranges:
        next_range = ranges.pop(0)

        if next_range.start > current_end:
            total += next_range.end - next_range.start
            current_end = next_range.end
        else:
            total += next_range.end - current_end
            current_end = next_range.end

    return total


if __name__ == "__main__":
    example = load_data("days/5/example.txt")
    example_result = count_fresh_ingredients(*example)
    print(f"example: {example_result}")  # 3
    assert example_result == 3

    input_data = load_data("days/5/input.txt")
    input_result = count_fresh_ingredients(*input_data)
    print(f"input: {input_result}")  # 513
    assert input_result == 513

    example_part_two_result = part_two(*example)
    print(f"example part two: {example_part_two_result}")  # 14
    assert example_part_two_result == 14

    part_two_result = part_two(*input_data)
    print(f"input part two: {part_two_result}")  # 317002602865927
    assert part_two_result == 317002602865927
