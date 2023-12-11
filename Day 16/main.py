OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> str:
    data: str = inp[0]
    converter: dict[str, str] = {
        hex(value)[2:]: bin(value)[2:].zfill(4)
        for value
        in range(16)
    }

    ret: str = ""
    for digit in data:
        ret += converter[digit.lower()]

    return ret


def parse_packet(packet: str) -> tuple[int, int, int]:
    version_number: int = int(packet[:3], 2)
    type_id: int = int(packet[3:6], 2)

    if type_id == 4:
        length: int = 6
        value: str = ""
        while packet[length] != "0":
            value += packet[length + 1: length + 5]
            length += 5

        value += packet[length + 1: length + 5]
        length += 5

        return version_number, length, int(value, 2)

    length_type_id: int = int(packet[6], 2)

    total_length: int
    parsed_values: list[int] = []

    if length_type_id == 0:
        packet_length: int = int(packet[7:22], 2)
        total_length = 22 + packet_length

        packet = packet[22:]
        while packet_length > 0:
            parsed_packet_version, parsed_packet_length, parsed_packet_value = parse_packet(
                packet)
            packet = packet[parsed_packet_length:]
            packet_length -= parsed_packet_length
            version_number += parsed_packet_version
            parsed_values.append(parsed_packet_value)

    if length_type_id == 1:
        packet_amount: int = int(packet[7:18], 2)
        total_length = 18

        packet = packet[18:]
        for _ in range(packet_amount):
            parsed_packet_version, parsed_packet_length, parsed_packet_value = parse_packet(
                packet)
            packet = packet[parsed_packet_length:]
            total_length += parsed_packet_length
            version_number += parsed_packet_version
            parsed_values.append(parsed_packet_value)

    packet_value: int
    if type_id == 0:
        packet_value = sum(parsed_values)
    elif type_id == 1:
        packet_value = 1
        for val in parsed_values:
            packet_value *= val
    elif type_id == 2:
        packet_value = min(parsed_values)
    elif type_id == 3:
        packet_value = max(parsed_values)
    elif type_id == 5:
        packet_value = int(parsed_values[0] > parsed_values[1])
    elif type_id == 6:
        packet_value = int(parsed_values[0] < parsed_values[1])
    elif type_id == 7:
        packet_value = int(parsed_values[0] == parsed_values[1])

    return version_number, total_length, packet_value


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    return parse_packet(parse_inp(inp))[0]


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return parse_packet(parse_inp(inp))[2]


def main() -> None:
    test_input: str = """9C0141080250320F1802104A08"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 20
    test_output_part_2_expected: OUTPUT_TYPE = 1

    file_location: str = "Day 16/input.txt"
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
