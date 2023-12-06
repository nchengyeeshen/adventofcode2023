import sys


def apply(time, distance) -> int:
    count = 0
    for i in range(1, time):
        if (time - i) * i > distance:
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt" if len(sys.argv) < 2 else sys.argv[1]) as f:
        contents = f.read()

    l1, l2 = contents.splitlines()

    time_text = l1.split(":")[1]
    distance_text = l2.split(":")[1]

    # Part 1
    total = 1
    for time, distance in zip(
        list(map(int, time_text.split())), list(map(int, distance_text.split()))
    ):
        total *= apply(time, distance)
    print("Part 1:", total)

    # Part 2
    print(
        "Part 2:",
        apply(
            int("".join(time_text.split())),
            int("".join(distance_text.split())),
        ),
    )
