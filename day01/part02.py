import sys


lookup = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def match(s: str, i: int) -> str:
    if s[i].isdigit():
        return s[i]

    for j in range(3, 6):
        substr = s[i : i + j]
        if substr in lookup:
            return lookup[substr]

    raise ValueError("cannot match character")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("part02.py <input file>")
        exit(1)

    contents: list[str]
    with open(sys.argv[1], "r") as f:
        contents = f.readlines()

    calibration_sum = 0
    for line in contents:
        digits: list[str] = []
        for i in range(len(line)):
            try:
                digits.append(match(line, i))
            except ValueError:
                continue
        calibration_sum += int(digits[0] + digits[-1])

    print(calibration_sum)
