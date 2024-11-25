import util

"""Parses "forward 5" into ("forward", 5)."""
def parse_line(line):
    parts = line.split(' ')
    return (parts[0], int(parts[1]))

def parse_input(data_path):
    return list(util.read_lines(data_path, parse_line))

def move(instructions):
    horizontal = 0
    depth = 0
    for (direction, value) in instructions:
        if direction == "forward":
            horizontal += value
        elif direction == "down":
            depth += value
        elif direction == "up":
            depth -= value
    return horizontal * depth

def move_aim(instructions):
    horizontal = 0
    depth = 0
    aim = 0
    for (direction, value) in instructions:
        if direction == "forward":
            horizontal += value
            depth += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
    return horizontal * depth

def solve_1(part, data_path):
    solve(part, data_path, parse_input, move)

def solve_2(part, data_path):
    solve(part, data_path, parse_input, move_aim)

solve_1("Part 1", 'data/02_example.txt')
solve_1("Part 1", 'data/02_input.txt')

solve_2("Part 2", 'data/02_example.txt')
solve_2("Part 2", 'data/02_input.txt')
