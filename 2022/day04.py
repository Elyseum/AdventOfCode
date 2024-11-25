import util

def parse_range(str):
    part0, part1 = str.split('-')
    return range(int(part0), int(part1)+1)

def parse_input(data_path):
    for line in util.read_lines(data_path):
        part0, part1 = line.split(',')
        yield (parse_range(part0), parse_range(part1))

def full_overlap(r1, r2):
    return (r1[0] in r2 and r1[-1] in r2) or (r2[0] in r1 and r2[-1] in r1)

def count_full_overlap(ranges):
    return sum(1 for (r1, r2) in ranges if full_overlap(r1, r2))

def solve_1(part, data_path):
    util.solve(part, data_path, parse_input, count_full_overlap)

def partial_overlap(r1, r2):
    return r1[0] in r2 or r1[-1] in r2 or r2[0] in r1 or r2[-1] in r1

def count_partial_overlap(ranges):
    return sum(1 for (r1, r2) in ranges if partial_overlap(r1, r2))

def solve_2(part, data_path):
    util.solve(part, data_path, parse_input, count_partial_overlap)

solve_1("Part 1", 'data/04_example.txt')
solve_1("Part 1", 'data/04_input.txt')

solve_2("Part 2", 'data/04_example.txt')
solve_2("Part 2", 'data/04_input.txt')

