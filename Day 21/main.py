from collections import defaultdict
OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> list[int]:
    return [int(row.strip()[-1]) - 1for row in inp]


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    roll: int = 0
    scores: list[int] = [0, 0]
    positions: list[int] = parse_inp(inp)
    while max(scores) < 1000:
        rolled: int = (6 - roll) % 10
        positions[roll % 2] += rolled
        positions[roll % 2] %= 10
        scores[roll % 2] += positions[roll % 2] + 1
        roll += 1

    return min(scores) * roll * 3


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    roll: int = 0
    position: list[int] = parse_inp(inp)
    states: defaultdict[tuple[tuple[int, int], tuple[int, int]],
                        int] = defaultdict(lambda: 0)
    states[((position[0], position[1]), (0, 0))] = 1
    wins: list[int] = [0, 0]

    while states != {}:
        new_states: defaultdict[tuple[tuple[int, int],
                                      tuple[int, int]], int] = defaultdict(lambda: 0)
        for state, positions in states.items():
            for rolled, scale in enumerate([1, 3, 6, 7, 6, 3, 1], 3):
                new_state: tuple[tuple[int, int], tuple[int, int]] = (
                    state[0], state[1])

                if roll % 2 == 0:  # my simple way to get this bodged, can't to this with lists because then i con't use it as a dict key
                    new_pos: tuple[int, int] = (
                        (new_state[0][0] + rolled) % 10, new_state[0][1])
                    new_score: tuple[int, int] = (
                        new_state[1][0] + new_pos[0] + 1, new_state[1][1])
                else:
                    new_pos = (
                        new_state[0][0], (new_state[0][1] + rolled) % 10)
                    new_score = (
                        new_state[1][0], new_state[1][1] + new_pos[1] + 1)

                new_state = (new_pos, new_score)

                if new_state[1][roll % 2] >= 21:
                    wins[roll % 2] += positions * scale
                    continue

                new_states[new_state] += positions * scale

        roll += 1
        states = new_states

    return max(wins)


def main() -> None:
    test_input: str = """Player 1 starting position: 4
Player 2 starting position: 8"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 739785
    test_output_part_2_expected: OUTPUT_TYPE = 444356092776315

    file_location: str = "Day 21/input.txt"
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
