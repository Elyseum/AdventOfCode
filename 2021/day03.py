import util

def parse_input(data_path):
    return list(util.read_lines(data_path))

def count_bits_value(bin_numbers, bit_pos, bit_val):
    return sum(1 for x in bin_numbers if x[bit_pos] == bit_val)

def diagnose(bin_numbers):
    bin_number_len = len(bin_numbers[0])

    counts_0 = {}
    for i in range(bin_number_len):
        counts_0[i] = count_bits_value(bin_numbers, i, "0")

    gamma_rate = ""
    epsilon_rate = ""
    min_0_count = len(bin_numbers ) / 2
    for i in range(bin_number_len):
        if counts_0[i] >= min_0_count:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def most_common_bit(bin_numbers, bit_pos):
    bit_count = count_bits_value(bin_numbers, bit_pos, "0")
    if bit_count * 2 == len(bin_numbers):
        return "1"
    elif bit_count * 2 > len(bin_numbers):
        return "0"
    else:
        return "1"

def least_common_bit(bin_numbers, bit_pos):
    most_common = most_common_bit(bin_numbers, bit_pos)
    if most_common == "0":
        return "1"
    else:
        return "0"

def o2_generator_rating(bin_numbers):
    filtered = bin_numbers
    bit_pos = 0
    while len(filtered) > 1:
        bit = most_common_bit(filtered, bit_pos)
        filtered = [x for x in filtered if x[bit_pos] == bit]
        bit_pos += 1
    return int(filtered[0], 2)

def co2_scrubber_rating(bin_numbers):
    filtered = bin_numbers
    bit_pos = 0
    while len(filtered) > 1:
        bit = least_common_bit(filtered, bit_pos)
        filtered = [x for x in filtered  if x[bit_pos] == bit]
        bit_pos += 1
    return int(filtered[0], 2)

def rating(bin_numbers):
    return o2_generator_rating(bin_numbers) * co2_scrubber_rating(bin_numbers)

def solve_1(part, data_path):
    solve(part, data_path, parse_input, diagnose)

def solve_2(part, data_path):
    solve(part, data_path, parse_input, rating)

solve_1("Part 1", 'data/03_example.txt')
solve_1("Part 1", 'data/03_input.txt')

solve_2("Part 2", 'data/03_example.txt')
solve_2("Part 2", 'data/03_input.txt')
