F = open("Day 9/input.txt", "r").readlines()


def get_map(F):
    fmap = []
    for i in F:
        row = []
        for j in i.strip():
            row.append(int(j))
        fmap.append(row)

    return fmap


def vaild_coord(x: int, y: int, grid: list[list[int]]):
    return x >= 0 and y >= 0 and y < len(grid) and x < len(grid[0])


def generate_edges(vec2):
    x, y = tuple(vec2)
    return [
        [x + 1, y],
        [x - 1, y],
        [x, y + 1],
        [x, y - 1],
    ]


def check_low_point(x: int, y: int, grid: list[list[int]]):
    if not vaild_coord(x, y, grid):
        return False
    ret = True
    value = grid[y][x]
    # can't be bothered fixing this
    if vaild_coord(x + 1, y, grid):
        ret = ret and grid[y][x + 1] > value
    if vaild_coord(x - 1, y, grid):
        ret = ret and grid[y][x - 1] > value
    if vaild_coord(x, y + 1, grid):
        ret = ret and grid[y + 1][x] > value
    if vaild_coord(x, y - 1, grid):
        ret = ret and grid[y - 1][x] > value
    return ret


grid = get_map(F)
ret = 0
low_points = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if check_low_point(j, i, grid):
            ret += grid[i][j] + 1

            low_points.append([j, i])

print(f"Part 1: {ret}")


def flood_fill(x, y, grid):
    base_list = []
    to_generate = [[x, y]]
    while to_generate != []:
        working = to_generate.pop(0)
        if working in base_list:
            continue

        for edge in generate_edges(working):
            if not vaild_coord(edge[0], edge[1], grid):
                continue
            if grid[edge[1]][edge[0]] == 9:
                continue
            if edge in base_list:
                continue

            to_generate.append(edge)

        base_list.append(working)
    return len(base_list)


sizes = []
for low_point in low_points:
    sizes.append(flood_fill(low_point[0], low_point[1], grid))

sizes.sort()
print(f"Part 2: {sizes[-1] * sizes[-2] * sizes[-3]}")
