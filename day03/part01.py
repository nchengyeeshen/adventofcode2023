import sys
from dataclasses import dataclass


@dataclass
class CandidatePartNumber:
    num: int
    char_locs: set[tuple[int, int]]


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

    print(
        sum(
            c.num
            for c in candidate_part_numbers
            if len(c.char_locs.intersection(candidate_locs)) > 0
        )
    )


if __name__ == "__main__":
    main()
