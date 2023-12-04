import sys
from functools import reduce
from operator import mul


class POI:
    def __init__(self, symbol: str, coords: list[tuple[int, int]]) -> None:
        self.symbol = symbol
        self.coords = coords
        self.neighbors: list["POI"] = []


def main():
    grid: list[list[str]]
    with open(sys.argv[1], "r") as f:
        grid = [[c for c in line.strip()] for line in f]

    # Collect points of interest.
    pois = []
    coord_to_pois = {}
    for x, row in enumerate(grid):
        digits, coords = [], []

        for y, col in enumerate(row):
            if col.isdigit():
                digits.append(col)
                coords.append((x, y))
                continue

            # Symbol
            if col != ".":
                poi = POI(col, [(x, y)])
                pois.append(poi)
                coord_to_pois[(x, y)] = poi

            # Numbers
            if len(digits) > 0:
                poi = POI("".join(digits), coords)
                pois.append(poi)
                for coord in coords:
                    coord_to_pois[coord] = poi
                digits, coords = [], []

        # Flush leftover numbers
        if len(digits) > 0:
            poi = POI("".join(digits), coords)
            pois.append(poi)
            for coord in coords:
                coord_to_pois[coord] = poi
            digits, coords = [], []

    # Build up adjacency list.
    for poi in pois:
        neighboring_coords: list[tuple[int, int]] = [
            (coord[0] + i, coord[1] + j)
            for coord in poi.coords
            for i in range(-1, 2)
            for j in range(-1, 2)
        ]
        neighbor_pois: set["POI"] = set()
        for coord in neighboring_coords:
            other_poi = coord_to_pois.get(coord, None)
            if other_poi is None or other_poi is poi:
                continue
            neighbor_pois.add(other_poi)
        poi.neighbors = neighbor_pois

    print(
        "Sum of part numbers:",
        sum(
            int(poi.symbol)
            for poi in pois
            if poi.symbol.isdigit() and len(poi.neighbors) > 0
        ),
    )

    total_gear_ratios = 0
    for poi in pois:
        if poi.symbol != "*":
            continue

        neighbor_part_numbers = [n for n in poi.neighbors if n.symbol.isdigit()]
        if len(neighbor_part_numbers) != 2:
            continue

        total_gear_ratios += reduce(
            mul, (int(pn.symbol) for pn in neighbor_part_numbers)
        )
    print("Sum of all gear ratios:", total_gear_ratios)


if __name__ == "__main__":
    main()
