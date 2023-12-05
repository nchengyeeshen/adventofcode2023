from collections import defaultdict
from sys import argv


class Almanac:
    def __init__(self):
        self.listings: defaultdict[
            str, dict[str, list[tuple[int, int, int]]]
        ] = defaultdict(lambda: defaultdict(list))

    def register(
        self,
        src_category: str,
        dest_category: str,
        src_range_start: int,
        dest_range_start: int,
        range_length: int,
    ):
        mappings = self.listings[src_category][dest_category]
        mappings.append((src_range_start, dest_range_start, range_length))

    def maps_to(self, src_category: str, dest_category: str, num: int) -> int:
        for mapping in self.listings[src_category][dest_category]:
            src_range_start, dest_range_start, range_length = mapping

            if src_range_start <= num <= src_range_start + (range_length - 1):
                return dest_range_start + (num - src_range_start)
        return num


def parse_input(lines: list[str]) -> tuple[list[int], "Almanac"]:
    seeds: list[int] = []
    almanac = Almanac()

    src_category, dest_category = "", ""
    for line in lines:
        if len(line) == 0:
            # Do nothing
            pass
        elif line.startswith("seeds:"):
            parts = line.split(":")
            assert len(parts) == 2
            seeds = [int(x) for x in parts[1].split()]
        elif line.endswith("map:"):
            parts = line.split(" ")
            assert len(parts) == 2
            parts = parts[0].split("-")
            assert len(parts) == 3
            src_category, dest_category = parts[0], parts[-1]
        elif line[0].isdigit():
            parts = line.split()
            assert len(parts) == 3
            digits = [int(x) for x in parts]
            almanac.register(
                src_category, dest_category, digits[1], digits[0], digits[2]
            )

    return seeds, almanac


def location(almanac: "Almanac", seed: int) -> int:
    num = seed
    for src, dest in [
        ("seed", "soil"),
        ("soil", "fertilizer"),
        ("fertilizer", "water"),
        ("water", "light"),
        ("light", "temperature"),
        ("temperature", "humidity"),
        ("humidity", "location"),
    ]:
        num = almanac.maps_to(src, dest, num)
    return num


if __name__ == "__main__":
    filename = argv[1] if len(argv) > 1 else "input.txt"
    with open(filename, "r") as f:
        data = f.read().strip().splitlines()

    seeds, almanac = parse_input(data)

    # Part 1
    locations = [location(almanac, seed) for seed in seeds]
    print("Lowest location number:", min(locations))
