OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> None:
    return


def str_assign(string: str, index: int, item: str) -> str:
    return string[:index] + item + string[index+1:]


def add(digit_1: str, digit_2: str) -> str:
    if digit_1 in "[,]":
        return digit_1

    alphabet: str = "0123456789abcdefghijklmnopqrstuvwxyzABIJKLMNOPQRSTUVWXYZ+-"
    return alphabet[alphabet.index(digit_1) + alphabet.index(digit_2)]


def split(digit: str) -> str:
    alphabet: str = "0123456789abcdefghijklmnopqrstuvwxyzABIJKLMNOPQRSTUVWXYZ+-"

    value: int = alphabet.index(digit)
    if value < 10:
        return digit

    return f"[{alphabet[value // 2]},{alphabet[value // 2 + value % 2]}]"


def reduction(num: str) -> str:
    depth: int = 0
    for index, value in enumerate(num + " "):
        if value == "[":
            depth += 1
        elif value == "]":
            depth -= 1

        if depth < 0:
            ValueError(f"Sharts something has gone wrong: {num}")
        elif depth > 4:
            break

    if index < len(num):
        for left_index, value in list(enumerate(num[:index]))[::-1]:
            if value not in "[,]":
                break

        for right_index, value in enumerate(num[index + 4:]):
            if value not in "[,]":
                break

        right_index += index + 4

        num = str_assign(num, left_index, add(num[left_index], num[index + 1]))
        num = str_assign(num, right_index, add(
            num[right_index], num[index + 3]))
        num = num[:index] + "0" + num[index + 5:]

        return num

    for index, value in enumerate(num + " "):
        if value.isalpha():
            break

    if index < len(num):
        num = num[:index] + split(num[index]) + num[index + 1:]

    return num


def full_reduction(num: str) -> str:
    prev_num: str = ""

    while num != prev_num:
        prev_num = num
        num = reduction(num)

    return num


def add_num(num1: str, num2: str) -> str:
    if num1 == "":
        return full_reduction(num2)

    if num2 == "":
        return full_reduction(num1)

    return full_reduction(f"[{num1},{num2}]")


def magnitude(num: int | list) -> int:
    if isinstance(num, int):
        return num

    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    ret: str = ""
    for num in inp:
        num = num.replace("\n", "")
        ret = add_num(ret, num)
    return magnitude(eval(ret))


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    for num1 in inp:
        num1 = num1.replace("\n", "")
        for num2 in inp:
            num2 = num2.replace("\n", "")
            ret = max(ret, magnitude(eval(add_num(num1, num2))))
    return ret


def main() -> None:
    test_input: str = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 4140
    test_output_part_2_expected: OUTPUT_TYPE = 3993

    file_location: str = "Day 18/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_file)}")
    else:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")


if __name__ == "__main__":
    main()
