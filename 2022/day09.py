import util

def parse(path):
    for line in util.read_lines(path):
        direction, steps_str = line.split(' ')
        yield (direction, int(steps_str))

def touching(pos_t, pos_h):
    x_delta = abs(pos_h[0] - pos_t[0])
    y_delta = abs(pos_h[1] - pos_t[1])
    return x_delta < 2 and y_delta < 2

"""
Head moves according to a direction instruction.
"""
def move_head(pos_h, direction):
    if direction == 'U':
        return (pos_h[0], pos_h[1] + 1)
    elif direction == 'D':
        return (pos_h[0], pos_h[1] - 1)
    elif direction == 'L':
        return (pos_h[0] - 1, pos_h[1])
    else:
        return (pos_h[0] + 1, pos_h[1])

"""
Tail moves according to head direction.
"""
def move_tail(pos_t, pos_h):
    # No need to move when touching.
    if touching(pos_t, pos_h):
        return pos_t
    # Moving up
    if pos_t[0] == pos_h[0] and pos_t[1] < pos_h[1]:
        return (pos_t[0], pos_t[1] + 1)
    # Moving down
    if pos_t[0] == pos_h[0] and pos_t[1] > pos_h[1]:
        return (pos_t[0], pos_t[1] - 1)
    # Moving right
    if pos_t[0] < pos_h[0] and pos_t[1] == pos_h[1]:
        return (pos_t[0] + 1, pos_t[1])
    # Moving left
    if pos_t[0] > pos_h[0] and pos_t[1] == pos_h[1]:
        return (pos_t[0] - 1, pos_t[1])
    # Move up right
    if pos_t[0] < pos_h[0] and pos_t[1] < pos_h[1]:
        return (pos_t[0] + 1, pos_t[1] + 1)
    # Moving up left
    if pos_t[0] > pos_h[0] and pos_t[1] < pos_h[1]:
        return (pos_t[0] - 1, pos_t[1] + 1)
    # Moving down left
    if pos_t[0] > pos_h[0] and pos_t[1] < pos_h[1]:
        return (pos_t[0] - 1, pos_t[1] + 1)
    # Moving down left
    if pos_t[0] > pos_h[0] and pos_t[1] < pos_h[1]:
        return (pos_t[0] - 1, pos_t[1] + 1)
    # Moving down right
    if pos_t[0] < pos_h[0] and pos_t[1] > pos_h[1]:
        return (pos_t[0] + 1, pos_t[1] - 1)
    # Moving up right
    if pos_t[0] < pos_h[0] and pos_t[1] < pos_h[1]:
        return (pos_t[0] + 1, pos_t[1] + 1)
    # Moving up left
    if pos_t[0] > pos_h[0] and pos_t[1] < pos_h[1]:
        return (pos_t[0] - 1, pos_t[1] + 1)
    # Moving down left
    if pos_t[0] > pos_h[0] and pos_t[1] > pos_h[1]:
        return (pos_t[0] - 1, pos_t[1] - 1)
    print(str(pos_t) + " - " + str(pos_h))
    return -1

def move(instructions, rope_length=1):
    pos_h, pos_t = (0, 0), (0, 0)
    pos_ts = [pos_t for _ in range(rope_length)]
    steps_t = set()
    for (direction, step) in instructions:
        for _ in range(step):
            pos_h = move_head(pos_h, direction)
            prev = pos_h
            for i in range(len(pos_ts)):
                curr = pos_ts[i]
                updated = move_tail(curr, prev)
                moved = curr != updated
                if moved:
                    prev = updated
                    pos_ts[i] = updated
                else:
                    break
            # Track tail in case it was moved.
            steps_t.add(pos_ts[-1])
    return len(steps_t)

def solve_1(part, path):
    util.solve(part, path, parse, move)

def solve_2(part, data):
    util.solve(part, data, parse, lambda x: move(x, 9))

solve_1("Part 1", 'data/09_example.txt')
solve_1("Part 1", 'data/09_input.txt')

solve_2("Part 2", 'data/09_example.txt')
solve_2("Part 2", 'data/09_example_2.txt')
solve_2("Part 2", 'data/09_input.txt')

