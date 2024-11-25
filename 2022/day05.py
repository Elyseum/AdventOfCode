import util

def instr(lines):
    for parts in map(lambda x: x.split(' '), lines):
        yield (int(parts[1]), int(parts[3]), int(parts[5]))

def stacks(lines):
    size = int(lines[-1].split(' ')[-2])
    stacks = [[] for x in range(0, size)]
    for stack_nr, stack in enumerate(stacks):
        for line in lines[0:-1]:
            stack_char = line[(stack_nr) * 4 + 1]
            if stack_char != ' ':
                stack.append(stack_char)
    return stacks

def parse(path):
    stacks_s, instr_s = util.read_parts(path)
    return stacks(stacks_s.split('\n')), instr(instr_s.split('\n'))

def move(stacks, instructions, one_by_one=True):
    for size, frm, to in instructions:
        to_move = stacks[frm-1][0:size]
        if (one_by_one):
            to_move.reverse()
        stacks[to-1] = to_move + stacks[to-1]
        stacks[frm-1] = stacks[frm-1][size:]
    return ''.join(map(lambda x: x[0], stacks))

def solve_1(part, path):
    util.solve(part, path, parse, lambda x: move(x[0], x[1]))

def solve_2(part, data):
    util.solve(part, data, parse, lambda x: move(x[0], x[1], False))

solve_1("Part 1", 'data/05_example.txt')
solve_1("Part 1", 'data/05_input.txt')

solve_2("Part 2", 'data/05_example.txt')
solve_2("Part 2", 'data/05_input.txt')

