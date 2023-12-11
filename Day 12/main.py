OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> dict[str, list[str]]:
    ret: dict[str, list[str]] = {}
    for path in inp:
        start: str
        end: str
        start, end = tuple(path.split("-"))

        if start in ret.keys():
            ret[start].append(end)
        else:
            ret[start] = [end]

        if end in ret.keys():
            ret[end].append(start)
        else:
            ret[end] = [start]

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    paths: dict[str, list[str]] = parse_inp(inp)
    current_states: list[list[str]] = [["start"]]
    ret: int = 0

    while current_states:
        working: list[str] = current_states.pop()
        if working[-1] not in paths.keys():
            continue

        for direction in paths[working[-1]]:
            new: list[str] = working.copy()
            if direction == "end":
                ret += 1
            elif direction.isupper() or direction not in new:
                new.append(direction)
                current_states.append(new)

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    paths: dict[str, list[str]] = parse_inp(inp)
    current_states: list[list[str]] = [["start"]]
    finished: list[list[str]] = []

    while current_states:
        working: list[str] = current_states.pop()
        if working[-1] not in paths.keys():
            continue

        for direction in paths[working[-1]]:
            new: list[str] = working.copy()
            new.append(direction)

            if direction == "end":
                if new not in finished:
                    finished.append(new)
            elif direction == "start":
                continue
            elif direction.isupper():
                current_states.append(new)
            else:
                # check that it's failed
                filtered: list[str] = list(filter(str.islower, new))
                if len(filtered) <= len(set(filtered)) + 1:
                    current_states.append(new)

    return len(finished)


def main() -> None:
    test_input: str = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 10
    test_output_part_2_expected: OUTPUT_TYPE = 36

    file_location: str = "Day 12/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = list(map(str.strip, input_file))

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
