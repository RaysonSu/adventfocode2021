F = open("Day 3/input.txt", "r")
F = F.readlines()

amount = []
for _ in F[0].strip():
    amount.append(0)

for num in F:
    for i in range(len(num.strip())):
        amount[i] += int(num[i])

num = 0
for i in range(len(F[0].strip())):
    num += int(amount[-1 * i - 1] > len(F) / 2) * 2 ** i

num *= (2 ** len(F[0].strip()) - 1 - num)

print(f"Part 1: {num}")

oxygen = F.copy()
carbon = F.copy()

for i in range(len(F[0].strip())):
    ox_amount = 0
    for item in oxygen:
        ox_amount += int(item[i])
    
    ca_amount = 0
    for item in carbon:
        ca_amount += int(item[i])
    
    new_oxygen = []
    for item in oxygen:
        if bool(ox_amount >= (len(oxygen) / 2)) == bool(item[i] == "1"):
            new_oxygen.append(item)
    
    new_carbon = []
    for item in carbon:
        if bool(ca_amount >= (len(carbon) / 2)) != bool(item[i] == "1"):
            new_carbon.append(item)

#    print(oxygen)
#    print(carbon)

    if len(new_oxygen) > 0:
        oxygen = new_oxygen.copy()
    if len(new_carbon) > 0:
        carbon = new_carbon.copy()

print(f"Part 2: {int(oxygen[0], 2) * int(carbon[0], 2)}")
