F = open("Day 2/input.txt", "r")
F = F.readlines()

pos = [0, 0]
for i in F:
    direction = ["f", "d", "u"].index(i[0])
    amount = int(i.strip()[-1])

    pos[0] += [1, 0, 0][direction] * amount
    pos[1] += [0, 1, -1][direction] * amount

print(f"Part 1: {pos[0] * pos[1]}")

pos = [0, 0]
aim = 0
for i in F:
    direction = ["f", "d", "u"].index(i[0])
    amount = int(i.strip()[-1])

    pos[0] += [1, 0, 0][direction] * amount
    pos[1] += [1, 0, 0][direction] * amount * aim
    aim += [0, 1, -1][direction] * amount

print(f"Part 2: {pos[0] * pos[1]}")