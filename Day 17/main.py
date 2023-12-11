OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> tuple[list[int], list[int]]:
    data: str = inp[0]
    data = data.replace("..", ".|.").replace(", ", "|")
    data = "".join([char for char in data if char.isnumeric() or char in "-|"])
    ints: list[int] = list(map(int, data.split("|")))
    return (ints[:2], ints[2:])


def inverse_trangular(x: int) -> float:
    return -0.5 + (2 * x + 0.25) ** 0.5


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    y_bounds: list[int]
    _, y_bounds = parse_inp(inp)

    return y_bounds[0] * (y_bounds[0] + 1) // 2


def simulate_single(x_vel: int, y_vel: int, x_bounds: list[int], y_bounds: list[int]) -> bool:
    x_pos: int
    y_pos: int
    x_pos, y_pos = 0, 0
    while y_pos >= y_bounds[0]:
        x_pos += x_vel
        y_pos += y_vel

        if x_vel > 0:
            x_vel -= 1

        y_vel -= 1

        if x_bounds[0] <= x_pos and x_pos <= x_bounds[1] and \
           y_bounds[0] <= y_pos and y_pos <= y_bounds[1]:
            return True
    return False


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    x_bounds: list[int]
    y_bounds: list[int]

    x_bounds, y_bounds = parse_inp(inp)
    total_count: int = 0
    for x_vel in range(0, x_bounds[1] + 1):
        for y_vel in range(y_bounds[0], -y_bounds[0]):
            if simulate_single(x_vel, y_vel, x_bounds, y_bounds):
                total_count += 1

    return total_count


def main() -> None:
    test_input: str = """x=20..30, y=-10..-5"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 45
    test_output_part_2_expected: OUTPUT_TYPE = 112

    file_location: str = "Day 17/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

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
