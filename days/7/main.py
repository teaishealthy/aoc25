import dataclasses
from typing import NamedTuple


class Field(NamedTuple):
    x: int
    y: int


class Splitter(Field): ...


class Beam(Field): ...


class Start(Field): ...


@dataclasses.dataclass
class Lab:
    start: Start
    fields: list[list[Field]]
    splitters: list[Splitter]
    beams: list[Beam]
    total_splits: int = 0

    def place_beam(self, x: int, y: int) -> bool:
        beam = Beam(x, y)
        if x >= len(self.fields[0]) or x < 0 or y >= len(self.fields):
            return False

        if self.fields[y][x] in self.splitters:
            changed = 0
            changed += self.place_beam(x - 1, y)
            changed += self.place_beam(x + 1, y)
            if changed > 0:
                self.total_splits += 1

        else:
            if self.fields[y][x] in self.beams:
                return False  # Beam already present

            self.beams.append(beam)
            self.fields[y][x] = beam

        return True

    def tick_start(self) -> bool:
        return self.place_beam(self.start.x, self.start.y + 1)

    def tick(self) -> None:
        for beam in self.beams[:]:
            self.place_beam(beam.x, beam.y + 1)
            self.beams.remove(beam)


def load_data(filename: str) -> Lab:
    fields: list[list[Field]] = []
    splitters: list[Splitter] = []
    beams: list[Beam] = []
    start: Start | None = None
    with open(filename, "r") as file:
        for y, line in enumerate(file):
            row: list[Field] = []
            for x, char in enumerate(line.strip()):
                if char == "^":
                    splitter = Splitter(x, y)
                    row.append(splitter)
                    splitters.append(splitter)
                elif char == "S":
                    start = Start(x, y)
                    row.append(start)
                else:
                    assert char == "."
                    row.append(Field(x, y))
            fields.append(row)
    assert start is not None

    return Lab(start=start, fields=fields, splitters=splitters, beams=beams)


def print_fields(lab: Lab) -> None:
    for row in lab.fields:
        for field in row:
            if isinstance(field, Splitter):
                print("^", end="")
            elif isinstance(field, Start):
                print("S", end="")
            elif isinstance(field, Beam):
                print("|", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    lab = load_data("days/7/example.txt")
    lab.tick_start()
    while lab.beams:
        lab.tick()

    print("example:", lab.total_splits)

    lab = load_data("days/7/input.txt")
    lab.tick_start()
    while lab.beams:
        lab.tick()
    print("input:", lab.total_splits)
