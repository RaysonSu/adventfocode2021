from numpy import array as nparray
from numpy import int_ as npint
from numpy.linalg import matrix_power
from numpy.typing import NDArray


OUTPUT_TYPE = int
ArrayInt = NDArray[npint]


def convert_to_int(string: str, converter: list[str]) -> int:
    for digit, char in enumerate(converter):
        string = string.replace(char, str(digit))

    return int(string, len(converter))


def parse_inp(inp: list[str]) -> tuple[ArrayInt, ArrayInt, ArrayInt, ArrayInt]:
    letters: set[str] = {char for row in inp for char in row}
    letters.remove(" ")
    letters.remove("-")
    letters.remove(">")
    letters_conv: list[str] = list(letters)

    chars: int = len(letters_conv)

    initial_string: str = inp[0].strip()
    initial_list: list[int] = [0 for _ in range(chars ** 2)]
    for index in range(len(initial_string) - 1):
        initial_list[convert_to_int(
            initial_string[index:index + 2], letters_conv)] += 1

    # a n^2 x 1 vector
    initial_vector: ArrayInt = nparray(initial_list)

    replacements: dict[str, list[int]] = {}
    for replacement in inp[2:]:
        replacement = replacement.strip()
        replaced: list[str] = replacement.split(" -> ")
        row: list[int] = [0 for _ in range(chars ** 2)]
        row[convert_to_int(replaced[0][0] + replaced[1], letters_conv)] += 1
        row[convert_to_int(replaced[1] + replaced[0][1], letters_conv)] += 1
        replacements[replaced[0]] = row

    iteration_2d_list: list[list[int]] = []
    for right_digit in letters_conv:
        for left_digit in letters_conv:
            iteration_2d_list.append(replacements[right_digit + left_digit])

    # a n^2 x n^2 matrix
    iteration_matrix: ArrayInt = nparray(iteration_2d_list).T

    projection_2d_list: list[list[int]] = []
    for right_digit in letters_conv:
        for left_digit in letters_conv:
            row = [0 for _ in range(chars)]
            row[convert_to_int(right_digit, letters_conv)] += 1
            projection_2d_list.append(row)

    # n^2 x n matrix
    projection_matrix: ArrayInt = nparray(projection_2d_list).T

    extra_list: list[int] = [0 for _ in range(chars)]
    extra_list[convert_to_int(initial_string[-1], letters_conv)] += 1

    # n x 1 vector
    extra_vector: ArrayInt = nparray(extra_list)

    return initial_vector, iteration_matrix, projection_matrix, extra_vector


def compute_iterations(inp: list[str], iterations: int) -> int:
    initial_vector: ArrayInt
    iteration_matrix: ArrayInt
    projection_matrix: ArrayInt
    extra_vector: ArrayInt

    initial_vector, \
        iteration_matrix, \
        projection_matrix, \
        extra_vector = parse_inp(inp)

    iterations_matrix: ArrayInt = matrix_power(
        iteration_matrix, iterations)
    finished_vector: ArrayInt = iterations_matrix.dot(initial_vector)
    projected_vector: ArrayInt = projection_matrix.dot(finished_vector)
    final_counts: ArrayInt = projected_vector + extra_vector
    return int(final_counts.max() - final_counts.min())


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    return compute_iterations(inp, 10)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return compute_iterations(inp, 40)


def main() -> None:
    test_input: str = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 1588
    test_output_part_2_expected: OUTPUT_TYPE = 2188189693529

    file_location: str = "Day 14/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = list(map(str.strip, input_file))

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
        pass

    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_file)}")
    else:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")


if __name__ == "__main__":
    main()
