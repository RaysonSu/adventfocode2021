F = open("Day 5/input.txt", "r")
F = F.readlines()

def parse_input(inp: list[str]) -> list[tuple[list[int]]]:
    ret = []
    for i in inp:
        i = i.replace(",", " ")
        i = i.replace(" -> ", " ")
        i = i.split()
        start_x = int(i[0])
        start_y = int(i[1])
        end_x = int(i[2])
        end_y = int(i[3])

        ret.append(([start_x, start_y], [end_x, end_y]))
    return ret

def valid_line(line: tuple[list[int]]) -> bool:
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]

def is_diagonal(line: tuple[list[int]]) -> bool:
    if (line[1][0] - line[0][0]) != 0:
        return abs((line[1][1] - line[0][1]) / (line[1][0] - line[0][0])) == 1
    return False

def add_line(grid: list[list[int]], line: tuple[list[int]], line_type: bool) -> list[list[int]]:
    if valid_line(line) and line_type:
        for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
            for j in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                grid[j][i] += 1
    elif is_diagonal(line) and not line_type:
        slope = int((line[1][1] - line[0][1]) / (line[1][0] - line[0][0]))
        for i in range(abs(line[1][1] - line[0][1]) + 1):
            start = [line[0][0], line[1][0]].index(min(line[0][0], line[1][0]))
            y = line[start][1] + i * slope
            x = line[start][0] + i
            grid[y][x] += 1
    return grid

def make_grid(x: int, y: int) -> list[list[int]]:
    ret = []
    for _ in range(x):
        ret.append([0] * y)
    return ret

def print_grid(grid: list[list[int]]) -> None:
    for i in grid:
        p = ""
        for j in i:
            p += str(j)
        print(p)

grid = make_grid(1000, 1000)

for i in parse_input(F):
    grid = add_line(grid, i, True)
#    print_grid(grid)
#    print(f"{i[0][0]},{i[0][1]} -> {i[1][0]},{i[1][1]}")

ret = 0
for line in grid:
    for item in line:
        if item > 1:
            ret += 1

print(f"Part 1: {ret}")

for i in parse_input(F):
    grid = add_line(grid, i, False)
#    print_grid(grid)
#    print(f"{i[0][0]},{i[0][1]} -> {i[1][0]},{i[1][1]}")

ret = 0
for line in grid:
    for item in line:
        if item > 1:
            ret += 1

print(f"Part 2: {ret}")