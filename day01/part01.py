import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("part01.py <input file>")
        exit(1)

    contents: list[str]
    with open(sys.argv[1], "r") as f:
        contents = f.readlines()

    calibration_sum = 0
    for line in contents:
        digits: list[str] = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        calibration_sum += int(digits[0] + digits[-1])

    print(calibration_sum)
