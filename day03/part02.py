import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class CandidatePartNumber:
    num: int
    char_locs: set[tuple[int, int]]


@dataclass(frozen=True)
class Gear:
    x: int
    y: int

    @property
    def adjacent_locs(self) -> set[tuple[int, int]]:
        return {
            (self.x - 1, self.y),
            (self.x - 1, self.y - 1),
            (self.x - 1, self.y + 1),
            (self.x, self.y - 1),
            (self.x, self.y + 1),
            (self.x + 1, self.y),
            (self.x + 1, self.y - 1),
            (self.x + 1, self.y + 1),
        }


def main():
    if len(sys.argv) != 2:
        raise SystemExit("script.py <input file>")

    data: list[list[str]] = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            data.append([char for char in line])

    candidate_locs = set()
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char.isdigit() or char == ".":
                continue

            # Row before
            candidate_locs.add((x - 1, y))
            candidate_locs.add((x - 1, y - 1))
            candidate_locs.add((x - 1, y + 1))

            # Current row
            candidate_locs.add((x, y - 1))
            candidate_locs.add((x, y + 1))

            # Row after
            candidate_locs.add((x + 1, y))
            candidate_locs.add((x + 1, y - 1))
            candidate_locs.add((x + 1, y + 1))

    candidate_part_numbers = []
    for x, row in enumerate(data):
        start = None
        for y, char in enumerate(row):
            if char.isdigit():
                if start is None:
                    start = y
                continue
            if start is not None:
                candidate_part_numbers.append(
                    CandidatePartNumber(
                        num=int("".join(row[start:y])),
                        char_locs={(x, i) for i in range(start, y)},
                    )
                )
                start = None
        if start is not None:
            candidate_part_numbers.append(
                CandidatePartNumber(
                    num=int("".join(row[start : len(row)])),
                    char_locs={(x, i) for i in range(start, len(row))},
                )
            )

    part_numbers = [
        c
        for c in candidate_part_numbers
        if len(c.char_locs.intersection(candidate_locs)) > 0
    ]

    gears = [
        Gear(x=x, y=y)
        for x, row in enumerate(data)
        for y, char in enumerate(row)
        if char == "*"
    ]

    part_number_locs = {loc: pn for pn in part_numbers for loc in pn.char_locs}

    result = 0
    for gear in gears:
        pns_ids = set()
        intersect = gear.adjacent_locs.intersection(part_number_locs.keys())
        for v in intersect:
            pns_ids.add(id(part_number_locs[v]))
        pns = [pn for ident in pns_ids for pn in part_numbers if ident == id(pn)]
        if len(pns) == 2:
            ratio = 1
            for pn in pns:
                ratio *= pn.num
            result += ratio

    print(result)


if __name__ == "__main__":
    main()
