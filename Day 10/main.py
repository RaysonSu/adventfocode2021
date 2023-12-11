OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> None:
    return


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    OPEN: str = "[({<"
    SCORES: dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}
    PAIRS: dict[str, str] = {")": "(", "]": "[", "}": "{", ">": "<"}
    for line in inp:
        stack: str = ""

        line = line.strip()
        while line:
            target: str = line[0]
            line = line[1:]

            if target in OPEN:
                stack += target
                continue

            if stack[-1] == PAIRS[target]:
                stack = stack[:-1]
                continue

            ret += SCORES[target]
            break

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    OPEN: str = "[({<"
    SCORES: dict[str, str] = {"(": "1", "[": "2", "{": "3", "<": "4"}
    PAIRS: dict[str, str] = {")": "(", "]": "[", "}": "{", ">": "<"}

    scores: list[int] = []
    for line in inp:
        stack: str = ""

        line = line.strip()
        while line:
            target: str = line[0]
            line = line[1:]

            if target in OPEN:
                stack += target
                continue

            if stack[-1] == PAIRS[target]:
                stack = stack[:-1]
                continue

            break

        if line:
            continue

        stack = stack[::-1]
        for key, value in SCORES.items():
            stack = stack.replace(key, value)

        scores.append(int(stack, base=5))

    scores.sort()
    return scores[len(scores) // 2]


def main() -> None:
    test_input: str = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 26397
    test_output_part_2_expected: OUTPUT_TYPE = 288957

    file_location: str = "Day 10/input.txt"
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
