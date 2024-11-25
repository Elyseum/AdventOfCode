import math
import re
import util

def parse_input(data_path):
    for line in util.read_lines(data_path):
        parts = line.split('-')
        yield (parts[0], parts[1])

def count_paths(connections):
    paths = []
    for fr, to in connections:
        if fr == "start":
            paths.append([fr, to])
    expanded = True
    while expanded:
        expanded = False
        for path in paths:
            if path[-1] == "end":
                continue
    print(paths)
    return -1

def is_large(cave):
    return cave.isupper()

def solve_1(part, data_path):
    solve(part, data_path, parse_input, count_paths)

def solve_2(part, data_path):
    solve(part, data_path, parse_input, flash_sync)

solve_1("Part 1", 'data/12_example_small.txt')
solve_1("Part 1", 'data/12_example.txt')
# solve_1("Part 1", 'data/12_input.txt')

# solve_2("Part 2", 'data/12_example.txt')
# solve_2("Part 2", 'data/12_input.txt')
