import re
import util

def parse_input(data_path):
    for line_parts in util.read_lines(data_path, lambda x: x.split(' -> ')):
        f = line_parts[0].split(',')
        t = line_parts[1].split(',')
        yield ((int(f[0]), int(f[1])), (int(t[0]), int(t[1])))

def is_ver(segment):
    return segment[0][0] == segment[1][0]

def is_hor(segment):
    return segment[0][1] == segment[1][1]

def stride(c0, c1):
    if c0 == c1:
        return 0
    if c0 < c1:
        return 1
    else:
        return -1

def get_coordinates(segment):
    co0 = segment[0]
    co1 = segment[1]
    stride_x = stride(co0[0], co1[0])
    stride_y = stride(co0[1], co1[1])

    i = 0
    j = 0
    while co0[0] + i != co1[0] or co0[1] + j != co1[1]:
        yield (co0[0] + i, co0[1] + j)
        i += stride_x
        j += stride_y
    yield (co1[0], co1[1])

            
def find_overlap(segments, hor_ver_only):
    if hor_ver_only:
        relevant_segments = [x for x in segments if is_hor(x) or is_ver(x)]
    else:
        relevant_segments = segments
    points = dict()
    for s in relevant_segments:
        for c in get_coordinates(s):
            if c in points:
                points[c] += 1
            else:
                points[c] = 1
    return len([x for x in points.values() if x > 1])        

def solve_1(part, data_path):
    solve(part, data_path, parse_input, lambda x: find_overlap(x, True))

def solve_2(part, data_path):
    solve(part, data_path, parse_input, lambda x: find_overlap(x, False))

solve_1("Part 1", 'data/05_example.txt')
solve_1("Part 1", 'data/05_input.txt')

solve_2("Part 2", 'data/05_example.txt')
solve_2("Part 2", 'data/05_input.txt')
