import util

def parse_input(data_path):
    return util.read_lines(data_path)

def parse_line_number_chars(string):
    digits = [int(x) for x in string if x.isdigit()]
    return digits[0] * 10 + digits[-1]

def sum_numbers_as_chars(lines):
    return sum(map(parse_line_number_chars, lines))

def solve_1(part, data_path):
    util.solve(part, data_path, parse_input, sum_numbers_as_chars)

def replace_words_with_digits(line):
    # Keep text because words can overlap.
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")
    return line

def sum_numbers_as_words(lines):
    return sum_numbers_as_chars(map(replace_words_with_digits, lines))

def solve_2(part, data_path):
    util.solve(part, data_path, parse_input, sum_numbers_as_words)

solve_1("Part 1", 'data/01_example.txt')
solve_1("Part 1", 'data/01_input.txt')

solve_2("Part 2", 'data/01_example_02.txt')
solve_2("Part 2", 'data/01_input.txt')

