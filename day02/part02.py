import sys
from functools import reduce
from operator import mul

lookup = ["red", "blue", "green"]


def game_limits(game: list[str]) -> tuple[int, int, int]:
    limits = [0, 0, 0]
    for round in game:
        cubes = round.split(",")
        for cube in cubes:
            cube = cube.strip()
            num, color = cube.split(" ")
            limits[lookup.index(color)] = max(limits[lookup.index(color)], int(num))

    return limits[0], limits[1], limits[2]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("part02.py <input file>")
        exit(1)

    contents: list[str]
    with open(sys.argv[1], "r") as f:
        contents = f.readlines()

    power_sum = 0
    for line in contents:
        line = line[len("Game ") :]
        game_id_str, line = line.split(":")
        game_id = int(game_id_str)
        power_sum += reduce(mul, game_limits(line.split(";")))

    print(power_sum)
