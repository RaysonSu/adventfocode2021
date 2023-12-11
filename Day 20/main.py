OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> None:
    return


class CellularAutomata:
    def __init__(self, rule: list[bool]) -> None:
        self.rule: list[bool] = rule
        self.points: list[tuple[int, int]] = []
        self.boundary: bool = False

        self.determine_bounds()

    def add_point(self, points: tuple[int, int] | list[tuple[int, int]]) -> None:
        if isinstance(points, list):
            for point in points:
                self.points.append(point)
        else:
            self.points.append(points)
        self.determine_bounds()

    def determine_bounds(self) -> None:
        min_x: int = 10000
        min_y: int = 10000
        max_x: int = -10000
        max_y: int = -10000

        for x, y in self.points:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        self.bounds = (min_x, max_x, min_y, max_y)

    def in_bound(self, x: int, y: int) -> bool:
        return self.bounds[0] <= x and x <= self.bounds[1] and self.bounds[2] <= y and y <= self.bounds[3]

    def determine_future_point(self, x: int, y: int) -> bool:
        lookup: int = 0
        for y_diff in range(-1, 2):
            for x_diff in range(-1, 2):
                lookup = lookup << 1
                if (x + x_diff, y + y_diff) in self.points:
                    lookup = lookup + 1  # not elegant but works
                if not self.in_bound(x + x_diff, y + y_diff) and self.boundary:
                    lookup = lookup + 1

        return self.rule[lookup]

    def tick(self) -> None:
        new_points: list[tuple[int, int]] = []
        for x in range(self.bounds[0] - 1, self.bounds[1] + 2):
            for y in range(self.bounds[2] - 1, self.bounds[3] + 2):
                if self.determine_future_point(x, y):
                    new_points.append((x, y))

        self.boundary = self.rule[511 if self.boundary else 0]

        self.points = new_points
        self.determine_bounds()


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    rule: list[bool] = [char == "#" for char in inp[0]]
    cell: CellularAutomata = CellularAutomata(rule)
    grid: list[tuple[int, int]] = []

    for y, row in enumerate(inp[2:]):
        for x, char in enumerate(row.strip()):
            if char == "#":
                grid.append((x, y))

    cell.add_point(grid)
    cell.tick()
    cell.tick()

    return len(cell.points)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    rule: list[bool] = [char == "#" for char in inp[0]]
    cell: CellularAutomata = CellularAutomata(rule)
    grid: list[tuple[int, int]] = []

    for y, row in enumerate(inp[2:]):
        for x, char in enumerate(row.strip()):
            if char == "#":
                grid.append((x, y))

    cell.add_point(grid)
    for t in range(50):
        cell.tick()
        print(f"ticks: {t}")

    return len(cell.points)


def main() -> None:
    test_input: str = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 35
    test_output_part_2_expected: OUTPUT_TYPE = 3351

    file_location: str = "Day 20/input.txt"
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
