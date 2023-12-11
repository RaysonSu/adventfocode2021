from itertools import combinations, permutations
from functools import reduce
from numpy import array as Matrix
from numpy import int_ as npint
from numpy import floating as npfloat
from numpy.linalg import norm
from numpy.typing import NDArray
OUTPUT_TYPE = int

# thing to make me sane
matrix_int = NDArray[npint]
vector_int = matrix_int
Vector = Matrix


def mul(vec: list[int], multiplier: int) -> list[int]:
    return [x * multiplier for x in vec]


def generate_cube_matrices() -> list[matrix_int]:
    identity: list[list[int]] = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    positive: tuple[tuple[list[int], ...], ...] = tuple(
        permutations(identity, 3))
    ret: list[matrix_int] = []
    for matrix in positive:
        for i in range(8):
            current: list[list[int]] = list(matrix)
            for row in range(3):
                current[row] = mul(current[row], (-1) ** ((i >> row) % 2))
            ret.append(Matrix(current))

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    inp.append("--")
    data: list[list[vector_int]] = []
    becaon_data: list[vector_int] = []
    for row in inp:
        row = row.strip()
        if row == "":
            continue

        if row.startswith("--"):
            data.append(becaon_data)
            becaon_data = []
            continue

        becaon_data.append(Vector(eval(f"[{row}]")))
    data = data[1:]

    identity_matrix: matrix_int = Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    zero_vector: vector_int = Vector([0, 0, 0])

    beacon_map: dict[int, tuple[matrix_int, vector_int]] = {
        0: (identity_matrix, zero_vector)
    }

    while len(beacon_map) != len(data):
        for index, beacon in enumerate(data):
            if index in beacon_map.keys():
                continue

            for index_2 in beacon_map.keys():
                try:
                    if index == 4 and index_2 == 1:
                        pass
                    offset: tuple[matrix_int, vector_int] = determine_offset(
                        data[index_2], beacon)
                    beacon_map[index] = (
                        beacon_map[index_2][0].dot(offset[0]),
                        beacon_map[index_2][0].dot(
                            offset[1]) + beacon_map[index_2][1]
                    )
                    break
                except ValueError as _:
                    continue
                except IndexError as _:
                    continue
    final_beacons: set[tuple] = set()
    for index, beacons in enumerate(data):
        for beacon_single in beacons:
            final_beacons.add(
                tuple(beacon_map[index][0].dot(
                    beacon_single) + beacon_map[index][1])
            )

    return len(final_beacons)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    inp.append("--")
    data: list[list[vector_int]] = []
    becaon_data: list[vector_int] = []
    for row in inp:
        row = row.strip()
        if row == "":
            continue

        if row.startswith("--"):
            data.append(becaon_data)
            becaon_data = []
            continue

        becaon_data.append(Vector(eval(f"[{row}]")))
    data = data[1:-1]

    identity_matrix: matrix_int = Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    zero_vector: vector_int = Vector([0, 0, 0])

    beacon_map: dict[int, tuple[matrix_int, vector_int]] = {
        0: (identity_matrix, zero_vector)
    }

    while len(beacon_map) != len(data):
        for index, beacon in enumerate(data):
            if index in beacon_map.keys():
                continue

            for index_2 in beacon_map.keys():
                try:
                    if index == 4 and index_2 == 1:
                        pass
                    offset: tuple[matrix_int, vector_int] = determine_offset(
                        data[index_2], beacon)
                    beacon_map[index] = (
                        beacon_map[index_2][0].dot(offset[0]),
                        beacon_map[index_2][0].dot(
                            offset[1]) + beacon_map[index_2][1]
                    )
                    break
                except ValueError as _:
                    continue
                except IndexError as _:  # very questionable
                    continue

    ret: int = 0
    for sensor in beacon_map.values():
        for sensor_2 in beacon_map.values():
            ret = max(ret, int(norm(sensor[1] - sensor_2[1], ord=1)))

    return int(ret)


def determine_offset(becaon_1: list[vector_int], becaon_2: list[vector_int]) -> tuple[matrix_int, vector_int]:
    start_info: combinations[tuple[vector_int, vector_int]]
    end_info: combinations[tuple[vector_int, vector_int]]
    start_info = combinations(becaon_1, 2)
    end_info = combinations(becaon_2, 2)

    start_map: dict[npfloat, tuple[vector_int, vector_int]] = {
        norm(points[0] - points[1], ord=3): points
        for points in start_info
    }
    end_map: dict[npfloat, tuple[vector_int, vector_int]] = {
        norm(points[0] - points[1], ord=3): points
        for points in end_info
    }

    start_set: set[npfloat] = set(start_map.keys())
    end_set: set[npfloat] = set(end_map.keys())

    intersection: set[npfloat] = start_set.intersection(end_set)

    if len(intersection) != 66:
        raise ValueError("Elements do not have 12 points in common.")

    start_points: list[vector_int] = [Vector(vec) for vec in
                                      {tuple(point) for points in intersection for point in start_map[points]}]
    end_points: list[vector_int] = [Vector(vec) for vec in
                                    {tuple(point) for points in intersection for point in end_map[points]}]

    start_sum: vector_int = reduce((lambda a, b: a + b), start_points)
    end_sum: vector_int = reduce((lambda a, b: a + b), end_points)
    end_points = [
        [
            end_point
            for end_point in end_points
            if norm((end_sum - 12 * end_point), ord=4) == norm((start_sum - 12 * point), ord=4)
        ][0]
        for point in start_points
    ]

    cube_matrices = generate_cube_matrices()
    for matrix in cube_matrices:
        correct: bool = True
        for start_point, end_point in zip(start_points, end_points):
            correct = correct and norm((
                start_point - start_points[0]) - matrix.dot(end_point - end_points[0]), ord=1) == 0
        if correct:
            break

    return matrix, start_points[0] - matrix.dot(end_points[0])


def main() -> None:
    test_input: str = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 79
    test_output_part_2_expected: OUTPUT_TYPE = 3621

    file_location: str = "Day 19/input.txt"
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
