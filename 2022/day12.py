import math
import util

def parse(path):
    positions = {}
    for row, line in enumerate(util.read_lines(path)):
        for col, elevation in enumerate(line):
            positions[(row,col)] = elevation
    return positions

def can_reach(positions, fr, to):
    if not(to in positions):
        return False
    from_value = positions[fr]
    from_height = 'a' if from_value == 'S' else from_value
    to_value = positions[to]
    to_height = 'z' if to_value == 'E' else to_value
    height_difference = ord(to_height) - ord(from_height)
    return  height_difference <= 1

def get_next_steps(positions, walk):
    pos = walk[-1]
    for offset in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
        new_pos = (pos[0] + offset[0], pos[1] + offset[1])
        if can_reach(positions, pos, new_pos) and new_pos not in walk:
            yield new_pos

def travel(positions):
    # A walk is a list of positions.
    # The next step in a walk generates new walks, taking into account
    # - height restriction
    # - no loops
    start = next(x for x in positions.keys() if positions[x] == 'S')
    end = next(x for x in positions.keys() if positions[x] == 'E')
    print('Start walking from ' + str(start))
    print('Need to reach ' + str(end))
    walking = [[start]]
    reached = len(positions)
    print('Reached ' + str(reached))
    visited = set()
    visited.add(start)
    it = -1
    while len(walking) > 0:
        it += 1
        if it >= 30000:
            break
        walk = walking.pop()
        if end in walk:
            print('Ended')
            if len(walk) < reached:
                reached = len(walk)
        else:
            next_steps = list(get_next_steps(positions, walk))
            if end in next_steps:
                print('Found end')
                break
            for next_step in next_steps:
                new_walk = list(walk)
                new_walk.append(next_step)
                dist_end = abs(end[0] - next_step[0]) + abs(end[1] - next_step[1])
             #   if (len(new_walk) + dist_end) <= reached and next_step not in visited:
               # if next_step not in visited:
                walking.append(new_walk)
                #    visited.add(next_step)
                # walking = sorted(walking, key=lambda x: abs(end[0] - x[-1][0]) + abs(end[1] - x[-1][1]))
                walking = sorted(walking, key=lambda x: -1 * len(x))
    for walk in walking:
        print(walk)
    return reached

def solve_1(part, path):
    util.solve(part, path, parse, travel)

def solve_2(part, data):
    util.solve(part, data, parse, print)

solve_1("Part 1", 'data/12_example.txt')
solve_1("Part 1", 'data/12_input.txt')

#solve_2("Part 2", 'data/12_example.txt')
#solve_2("Part 2", 'data/12_input.txt')

