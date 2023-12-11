import numpy

OUTPUT_TYPE = int


def flatten_list(list_2d: list[list[int]]) -> list[int]:
    return [item for row in list_2d for item in row]


def parse_inp(inp: list[str]) -> list[list[int]]:
    return [[int(value) for value in row] for row in inp]


def valid_coord(coords: int) -> bool:
    return 0 <= coords and coords < 110 and (coords % 11 != 10)


def convert_to(index: int) -> int:
    data: tuple[int, int] = divmod(index, 10)
    return data[0] * 11 + data[1]


def convert_from(index: int) -> int:
    data: tuple[int, int] = divmod(index, 11)
    return data[0] * 10 + data[1]


def generate_neighbours(coords: int) -> list[int]:
    coords = convert_to(coords)
    ret: list[int] = [
        coords + 1,  # right
        coords + 12,  # right down
        coords + 11,  # down
        coords + 10,  # left down
        coords - 1,  # left
        coords - 12,  # left up
        coords - 11,  # up
        coords - 10,  # right up
    ]

    return [convert_from(coords) for coords in ret if valid_coord(coords)]


def print_array(grid: list[int]) -> None:
    for i in range(10):
        print("".join(map(lambda x: str(x) if x <=
              10 else "*", grid[10 * i: 10 * (i + 1)])))


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    light_levels: list[int] = flatten_list(parse_inp(inp))
    one_array: list[int] = [1 for _ in range(100)]
    ret: int = 0
    for _ in range(100):
        light_levels = list(numpy.add(light_levels, one_array))
        tens: list[int] = []
        while max(light_levels) >= 10:
            tens_current: list[int] = [index for index,
                                       value in enumerate(light_levels) if value >= 10]
            for ten in tens_current:
                neighbours: list[int] = generate_neighbours(ten)
                for neighbour in neighbours:
                    light_levels[neighbour] += 1
                tens.append(ten)

            for ten in tens_current:
                light_levels[ten] = 0
        for ten in tens:
            light_levels[ten] = 0
        ret += len(tens)

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    light_levels: list[int] = flatten_list(parse_inp(inp))
    one_array: list[int] = [1 for _ in range(100)]
    zero_array: list[int] = [0 for _ in range(100)]
    ret: int = 0
    while light_levels != zero_array:
        light_levels = list(numpy.add(light_levels, one_array))
        tens: list[int] = []
        while max(light_levels) >= 10:
            tens_current: list[int] = [index for index,
                                       value in enumerate(light_levels) if value >= 10]
            for ten in tens_current:
                neighbours: list[int] = generate_neighbours(ten)
                for neighbour in neighbours:
                    light_levels[neighbour] += 1
                tens.append(ten)

            for ten in tens_current:
                light_levels[ten] = 0
        for ten in tens:
            light_levels[ten] = 0
        ret += 1

    return ret


def main() -> None:
    test_input: str = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 1656
    test_output_part_2_expected: OUTPUT_TYPE = 195

    file_location: str = "Day 11/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = [line.strip() for line in input_file]

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed)

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
