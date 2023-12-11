OUTPUT_TYPE = int

def exec_program(guess: int, program: list[str]) -> int:
    regs: dict[str, int] = {"w": 0, "x": 0, "y": 0, "z": 0}
    for line in program:
        parsed_line: list[str] = line.replace("\n", "").split(" ")
        if len(parsed_line) > 2:
            value = regs[parsed_line[2]] if parsed_line[2].isalpha() else int(parsed_line[2])
        if parsed_line[0] == "inp":
            guess, regs[parsed_line[1]] = divmod(guess, 10)
        elif parsed_line[0] == "add":
            regs[parsed_line[1]] += value
        elif parsed_line[0] == "mul":
            regs[parsed_line[1]] *= value
        elif parsed_line[0] == "div":
            regs[parsed_line[1]] //= value
        elif parsed_line[0] == "mod":
            regs[parsed_line[1]] %= value
        elif parsed_line[0] == "eql":
            regs[parsed_line[1]] = int(regs[parsed_line[1]] == value)
    
    return regs["z"]

def determine_pairs(program: list[str]) -> list[tuple[int, int]]:
    lines: list[str] = program[4::18]
    stack: list[int] = []
    ret: list[tuple[int, int]] = []

    for index, line in enumerate(lines):
        if line == "div z 1\n":
            stack.append(index)
        else:
            ret.append((stack.pop(), index))
    
    return ret

def convert(pair_index: tuple[int, int], pair: tuple[int, int]) -> int:
    return pair[0] * 10 ** pair_index[0] + pair[1] * 10 ** pair_index[1]

def compute(program: list[str], values: list[tuple[int, int]]) -> int:
    ret: int = 0
    pairs: list[tuple[int, int]] = determine_pairs(program)
    for index, pair in enumerate(pairs):
        for value in values:
            if exec_program(ret + convert(pair, value), program) < 26 ** (6 - index):
                break
        ret += convert(pair, value)

    return int(str(ret)[::-1])

def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    return compute(inp, [(9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1)])

def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return compute(inp, [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9)])


def main() -> None:
    file_location: str = "Day 24/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    print(f"Part 1: {main_part_1(input_file)}")
    print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()

