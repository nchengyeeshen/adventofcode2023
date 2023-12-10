from sys import argv


def north(x, y):
    return x - 1, y


def south(x, y):
    return x + 1, y


def west(x, y):
    return x, y - 1


def east(x, y):
    return x, y + 1


if __name__ == "__main__":
    filename = argv[1] if len(argv) > 1 else "input.txt"
    with open(filename, "r") as f:
        contents = f.read()

    grid = contents.splitlines()

    starting_position = (-1, -1)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                starting_position = i, j
                break
        else:
            continue
        break

    M, N = len(grid), len(grid[0])

    seen = {starting_position}
    coords = [starting_position]
    while len(coords) > 0:
        x, y = coords.pop()
        cell = grid[x][y]

        # North
        if (
            x > 0
            and cell in "S|LJ"
            and grid[x - 1][y] in "|7F"
            and (x - 1, y) not in seen
        ):
            seen.add((x - 1, y))
            coords.append((x - 1, y))

        # South
        if (
            x + 1 < M
            and cell in "S|7F"
            and grid[x + 1][y] in "|LJ"
            and (x + 1, y) not in seen
        ):
            seen.add((x + 1, y))
            coords.append((x + 1, y))

        # West
        if (
            y > 0
            and cell in "S-J7"
            and grid[x][y - 1] in "-LF"
            and (x, y - 1) not in seen
        ):
            seen.add(((x, y - 1)))
            coords.append((x, y - 1))

        # East
        if (
            y + 1 < N
            and cell in "S-LF"
            and grid[x][y + 1] in "-J7"
            and (x, y + 1) not in seen
        ):
            seen.add(((x, y + 1)))
            coords.append((x, y + 1))

    print(len(seen) // 2)
