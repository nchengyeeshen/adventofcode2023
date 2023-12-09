import sys


def extrapolate(values: list[int]) -> int:
    sequences = [values]
    while True:
        seq = sequences[-1]
        if all(x == 0 for x in seq):
            break
        differences = []
        for i in range(1, len(seq)):
            differences.append(seq[i] - seq[i - 1])
        sequences.append(differences)

    v = 0
    for i in range(len(sequences) - 2, -1, -1):
        v = sequences[i][-1] + v
    return v


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    with open(filename, "r") as f:
        contents = f.read()

    values = [[int(v) for v in line.split()] for line in contents.splitlines()]
    print("Part 1:", sum(extrapolate(v) for v in values))
