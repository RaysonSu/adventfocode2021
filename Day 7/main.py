F = open("Day 7/input.txt", "r")
F = F.readlines()

def parse_input(inp: list[str]) -> list[int]:
    ret = []
    inp = inp[0]
    inp = inp.split(",")
    for i in inp:
        ret.append(int(i))
    return ret

def total_fuel(crabs: list[int], goal: int, part: int) -> int:
    ret = 0
    for i in crabs:
        distance = abs(i - goal)
        if part == 1:
            ret += distance
        else:
            ret += int(distance * (distance + 1) / 2)
    return ret

state = parse_input(F)

best = 1000000000
for i in range(min(state), max(state) + 1):
    best = min(best, total_fuel(state, i, 1))

print(f"Part 1: {best}")

best = 1000000000
for i in range(min(state), max(state) + 1):
    best = min(best, total_fuel(state, i, 2))

print(f"Part 2: {best}")
