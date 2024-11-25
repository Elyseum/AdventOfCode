import re
import util

def parse(path):
    return list(util.read_lines(path))

# E.g. grid[(x, y)] = char ('.' or a digit).
def create_lookup_special_chars(lines):
    lookup = {}
    for (row, line) in enumerate(lines):
        for (col, char) in enumerate(line):
            if char != '.' and not char.isdigit():
                lookup[(row, col)] = char
    return lookup

def sum_numbers(lines):
    lookup = create_lookup_special_chars(lines)
    sum = 0
    for (row, line) in enumerate(lines):
        parts = [x for x in re.split(r'(\d+)', line) if len(x) > 0]
        col = 0
        for part in parts:
            if part[0].isdigit():
                number = int(part)
                coo = util.get_coordinates_lst(part, (row, col))
                adj = set(util.flatten(map(util.get_coordinates_adjacent, coo)))
                if any(adj_coo in lookup for adj_coo in adj):
                    sum += number
            col += len(part)
    return sum

def solve_1(part, path):
    util.solve(part, path, parse, sum_numbers)

def create_lookup_gear_chars(lines):
    lookup = {}
    for (row, line) in enumerate(lines):
        for (col, char) in enumerate(line):
            if char == '*':
                lookup[(row, col)] = char
    return lookup

def sum_gear_ratio(lines):
    lookup = create_lookup_gear_chars(lines)
    gear_char_count = {}
    for (row, line) in enumerate(lines):
        parts = [x for x in re.split(r'(\d+)', line) if len(x) > 0]
        col = 0
        for part in parts:
            if part[0].isdigit():
                number = int(part)
                number_coo = (row, col)
                coo = util.get_coordinates_lst(part, number_coo)
                adj = set(util.flatten(map(util.get_coordinates_adjacent, coo)))
                for adj_coo in adj:
                    if adj_coo in lookup:
                        if adj_coo not in gear_char_count:
                            gear_char_count[adj_coo] = []
                        gear_char_count[adj_coo].append(number)
            col += len(part)
    return sum(n[0]*n[1] for n in gear_char_count.values() if len(n) == 2)

def solve_2(part, path):
    util.solve(part, path, parse, sum_gear_ratio)

solve_1("Part 1", 'data/03_example.txt')
solve_1("Part 1", 'data/03_input.txt')

solve_2("Part 2", 'data/03_example.txt')
solve_2("Part 2", 'data/03_input.txt')

