OUTPUT_TYPE = int

def str_assign(string: str, index: int, item: str) -> str:
    return string[:index] + item + string[index+1:]

def parse_inp(inp: list[str]) -> list[str]:
    inp = [f"@{row.replace(chr(0xa), '')}@" for row in inp]
    
    inp.insert(0, "@" * len(inp[0]))
    inp.append("@" * len(inp[0]))

    return inp

def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    grid: str = "".join(parse_inp(inp))
    x_length: int = len(inp[0].replace("\n", ""))
    prev_grid: str = ""
    time: int = 0
    conversion: dict[str, str] = {">": "<", "v": "V"}
    while prev_grid != grid:
        time += 1
        prev_grid = grid
        for delta, name in [(1, ">"), (x_length + 2, "v")]:
            tmp_grid: str = grid.replace(name, ".")
            for coord in range(len(grid)):
                if grid[coord] != name:
                    continue
                
                next_coord: int = coord + delta
                next_obj: str = grid[next_coord]

                if next_obj == "@": # off the world
                    tmp_next_obj: str = "."
                    next_coord -= delta
                    while tmp_next_obj != "@":
                        next_coord -= delta
                        tmp_next_obj = grid[next_coord]
                    next_coord += delta
                    next_obj = grid[next_coord]
                
                if next_obj != ".":
                    tmp_grid = str_assign(tmp_grid, coord, conversion[name])
                    continue
                
                tmp_grid = str_assign(tmp_grid, next_coord, conversion[name])
                tmp_grid = str_assign(tmp_grid, coord, ".")
            grid = tmp_grid
            grid = grid.lower().replace("<", ">")
    
    return time



def main() -> None:
    test_input: str = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 58

    file_location: str = "Day 25/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()


if __name__ == "__main__":
    main()
