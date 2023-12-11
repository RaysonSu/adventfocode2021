F = open("Day 6/input.txt", "r")
F = F.readlines()

def parse_input(inp: list[str]) -> list[int]:
    ret = []
    inp = inp[0]
    inp = inp.split(",")
    for i in range(9):
        ret.append(inp.count(str(i)))
    return ret

def tick(state: list[int]) -> list[int]:
    new = state.pop(0)
    state[6] += new
    state.append(new)
    return state


state = parse_input(F)

for _ in range(80):
    state = tick(state)

print(f"Part 1: {sum(state)}")

for _ in range(176):
    state = tick(state)

print(f"Part 2: {sum(state)}")
