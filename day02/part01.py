import sys


lookup = {"red": 0, "blue": 1, "green": 2}


def validate(game: list[str], limits: tuple[int, int, int]) -> bool:
    for round in game:
        cubes = round.split(",")
        for cube in cubes:
            cube = cube.strip()
            num, color = cube.split(" ")
            if int(num) > limits[lookup[color]]:
                return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("part01.py <input file> <red> <blue> <green>")
        exit(1)

    limits = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])

    contents: list[str]
    with open(sys.argv[1], "r") as f:
        contents = f.readlines()

    id_sum = 0
    for line in contents:
        line = line[len("Game ") :]
        game_id_str, line = line.split(":")
        game_id = int(game_id_str)
        if validate(line.split(";"), limits):
            id_sum += game_id

    print(id_sum)
