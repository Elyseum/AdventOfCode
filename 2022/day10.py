import util

NOOP = 'noop'
ADDX = 'addx'

DURATION = { NOOP: 1, ADDX: 2 }

def parse(path):
    for line in util.read_lines(path):
        parts = line.split(' ')
        op = parts[0]
        arg = int(parts[1]) if len(parts) == 2 else None
        yield (op, arg)

def map_to_cycles(instructions):
    for op, arg in instructions:
        for _ in range(DURATION[op] - 1):
            yield (NOOP, None)
        yield (op, arg)

def run_1(instructions):
    reg_hist = [1]
    for op, arg in map_to_cycles(instructions):
        delta = 0 if op == NOOP else arg
        reg_hist.append(reg_hist[-1] + delta)
    return sum(map(lambda x: x * reg_hist[x - 1], [20, 60, 100, 140, 180, 220]))

def run_2(instructions):
    reg = 1
    screen = []
    for i, (op, arg) in enumerate(map_to_cycles(instructions)):
        pi = i // 40 * 40 + reg
        screen.append('#' if i in [pi - 1, pi, pi + 1] else '.')
        reg += 0 if op == NOOP else arg
    for row in range(len(screen) // 40):
        print(''.join(screen[(row*40):((row*40)+40)]))
    return None

def solve_1(part, path):
    util.solve(part, path, parse, run_1)

def solve_2(part, data):
    util.solve(part, data, parse, run_2)

solve_1("Part 1", 'data/10_example.txt')
solve_1("Part 1", 'data/10_input.txt')

solve_2("Part 2", 'data/10_example.txt')
solve_2("Part 2", 'data/10_input.txt')

