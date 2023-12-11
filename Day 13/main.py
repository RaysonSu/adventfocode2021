def str_assign(string: str, index: int, item: str) -> str:
    return string[:index] + item + string[index+1:]


def parse_inp(inp: list[str]) -> tuple[set[tuple[int, int]], list[tuple[bool, int]]]:
    points: set[tuple[int, int]] = set()
    index: int = 0
    while inp[index]:
        coords: list[str] = inp[index].split(",")[:2]
        x: int = int(coords[0])
        y: int = int(coords[1])  # so my-py is happy
        points.add((x, y))
        index += 1

    index += 1

    folds: list[tuple[bool, int]] = []
    while index < len(inp):
        direction: bool = "x" in inp[index]
        value: int = int(inp[index].split("=")[1])
        folds.append((direction, value))
        index += 1

    return points, folds


def main_part_1(inp: list[str]) -> int:
    points: set[tuple[int, int]]
    folds: list[tuple[bool, int]]
    points, folds = parse_inp(inp)

    fold: tuple[bool, int] = folds[0]
    new_points: set[tuple[int, int]] = set()
    for point in points:
        if fold[0]:
            new_points.add((fold[1] - abs(fold[1] - point[0]), point[1]))
        else:
            new_points.add((point[0], fold[1] - abs(fold[1] - point[1])))

    return len(new_points)


def main_part_2(inp: list[str]) -> str:
    points: set[tuple[int, int]]
    folds: list[tuple[bool, int]]
    points, folds = parse_inp(inp)

    for fold in folds:
        new_points: set[tuple[int, int]] = set()
        for point in points:
            if fold[0]:
                new_points.add((fold[1] - abs(fold[1] - point[0]), point[1]))
            else:
                new_points.add((point[0], fold[1] - abs(fold[1] - point[1])))
        points = new_points

    fixed_points: list[tuple[int, int]] = list(points)
    x_length: int = max([point[0] for point in fixed_points]) + 1
    y_length: int = max([point[1] for point in fixed_points]) + 1
    output = ("." * x_length + "\n") * y_length
    for point in fixed_points:
        output = str_assign(output, point[1] * (x_length + 1) + point[0], "#")

    return "\n" + output.strip()


def main() -> None:
    test_input: str = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: int = 17
    test_output_part_2_expected: str = """
#####
#...#
#...#
#...#
#####"""

    file_location: str = "Day 13/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = list(map(str.strip, input_file))

    test_output_part_1: int = main_part_1(test_input_parsed)
    test_output_part_2: str = main_part_2(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_file)}")
    else:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")


if __name__ == "__main__":
    main()
