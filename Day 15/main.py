import heapq


OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> None:
    return


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    inp = list(map(str.strip, inp))
    best_found: dict[tuple[int, int], int] = {(0, 0): 0}
    states: list[tuple[int, int, int]] = [(0, 0, 0)]
    heapq.heapify(states)
    while states:
        current_state: tuple[int, int, int] = heapq.heappop(states)

        if current_state[1] == (len(inp[0]) - 1) and current_state[2] == (len(inp) - 1):
            return current_state[0]

        for path in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x: int = current_state[1] + path[0]
            new_y: int = current_state[2] + path[1]

            if new_x < 0 or new_x >= len(inp[0]):
                continue

            if new_y < 0 or new_y >= len(inp):
                continue

            cost: int = current_state[0] + int(inp[new_y][new_x])

            if (new_x, new_y) in best_found.keys() and best_found[(new_x, new_y)] <= cost:
                continue

            best_found[(new_x, new_y)] = cost
            heapq.heappush(states, (cost, new_x, new_y))

    return 0


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    inp = list(map(str.strip, inp))
    best_found: dict[tuple[int, int], int] = {(0, 0): 0}
    states: list[tuple[int, int, int]] = [(0, 0, 0)]
    heapq.heapify(states)
    while states:
        current_state: tuple[int, int, int] = heapq.heappop(states)

        if current_state[1] == (5 * len(inp[0]) - 1) and current_state[2] == (5 * len(inp) - 1):
            return current_state[0]

        for path in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x: int = current_state[1] + path[0]
            new_y: int = current_state[2] + path[1]

            if new_x < 0 or new_x >= 5 * len(inp[0]):
                continue

            if new_y < 0 or new_y >= 5 * len(inp):
                continue

            cost: int = current_state[0] + (int(inp[new_y % len(inp)][new_x % len(inp[0])]) +
                                            new_y // len(inp) + new_x // len(inp[0]) - 1) % 9 + 1

            if (new_x, new_y) in best_found.keys() and best_found[(new_x, new_y)] <= cost:
                continue

            best_found[(new_x, new_y)] = cost
            heapq.heappush(states, (cost, new_x, new_y))
    return 0


def main() -> None:
    test_input: str = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 40
    test_output_part_2_expected: OUTPUT_TYPE = 315

    file_location: str = "Day 15/input.txt"
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
