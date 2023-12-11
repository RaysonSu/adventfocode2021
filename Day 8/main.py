F = open("Day 8/input.txt", "r").readlines()

def parse_input(inp: list[str]) -> list[dict]:
    ret = []
    for i in inp:
        split_line = i.split("|")
        ret.append({"key": split_line[0].split(), "value": split_line[1].split()})
    return ret

def solve(line: list[str]) -> str:
    def invert(s: set) -> set:
        ret = set()
        for i in "abcdefg":
            if len(s.intersection(i)) == 0:
                ret.add(i)
        return ret
    new_line = [set("abcdefg")] * 8
    for i in line:
        new_line[len(i)] = new_line[len(i)].intersection(set(i))
    
    a = new_line[3].intersection(invert(new_line[2]))
    dg = invert(a).intersection(new_line[5])
    b = new_line[4].intersection(invert(new_line[2].union(dg)))
    f = new_line[6].intersection(invert(new_line[5].union(b)))
    c = new_line[2].intersection(invert(f))
    d = new_line[4].intersection(invert(new_line[2].union(b)))
    g = dg.intersection(invert(d))
    e = invert(new_line[6].union(d).union(c))

    return str(a)[2] + str(b)[2] + str(c)[2] + str(d)[2] + str(e)[2] + str(f)[2] + str(g)[2]

state = parse_input(F)

ret_1 = 0
ret_2 = 0

for pair in state:
    sol = ""
    key = solve(pair["key"])
    values = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    for i in range(10):
        new = ""
        for j in values[i]:
            new += key[ord(j) - 97]
        values[i] = new
    
    for i in range(10):
        values[i] = set(values[i])
    
    for i in range(4):
        sol += str(values.index(set(pair["value"][i])))
    
    ret_1 += sol.count("1") + sol.count("4") + sol.count("7") + sol.count("8")
    ret_2 += int(sol)

print(f"Part 1: {ret_1}")
print(f"Part 2: {ret_2}")
