F = open("Day 1/input.txt", "r")
F = F.readlines()

total = 0

for i in range(1, len(F)):
    if int(F[i]) > int(F[i - 1]):
        total += 1

print(f"Part 1: {total}")

total = 0

for i in range(3, len(F)):
    if int(F[i]) > int(F[i - 3]):
        total += 1

print(f"Part 2: {total}")
