from functools import reduce
from sys import argv


def extrapolate(values: list[int]) -> int:
    sequences = [values]
    while True:
        seq = sequences[-1]
        if all(x == 0 for x in seq):
            break
        differences = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
        sequences.append(differences)
    return reduce(lambda acc, x: acc + x[-1], reversed(sequences[:-1]), 0)


def part_one(values: list[list[int]]) -> int:
    return sum(extrapolate(v) for v in values)


def part_two(values: list[list[int]]) -> int:
    return sum(extrapolate(list(reversed(v))) for v in values)


if __name__ == "__main__":
    filename = argv[1] if len(argv) > 1 else "input.txt"
    with open(filename, "r") as f:
        contents = f.read()
    values = [[int(v) for v in line.split()] for line in contents.splitlines()]
    print("Part 1:", part_one(values))
    print("Part 2:", part_two(values))
