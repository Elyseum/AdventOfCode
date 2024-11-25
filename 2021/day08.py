import math
import re
import util

def parse_line(line):
    parts = line.split(' | ')
    return (parts[0].split(' '), parts[1].split(' '))

def parse_input(data_path):
    return util.read_lines(data_path, parse_line)

def is_number(derived, pattern_number, pattern):
    if not derived:
        return False
    pattern_to_numbers = sorted(str(derived.index(x)) for x in pattern)
    return pattern_number == ''.join(pattern_to_numbers)

def is_0(derived, pattern):
    return is_number(derived, '012456', pattern)

def is_1(pattern):
    return len(pattern) == 2

def is_2(derived, pattern):
    return is_number(derived, '02346', pattern)

def is_3(derived, pattern):
    return is_number(derived, '02356', pattern)

def is_4(pattern):
    return len(pattern) == 4

def is_5(derived, pattern):
    return is_number(derived, '01356', pattern)
    
def is_6(derived, pattern):
    return is_number(derived, '013456', pattern)

def is_7(pattern):
    return len(pattern) == 3

def is_8(pattern):
    return len(pattern) == 7

def is_9(derived, pattern):
    return is_number(derived, '012356', pattern)

def derive_number(derived, pattern):
    if is_1(pattern): return 1
    if is_4(pattern): return 4
    if is_7(pattern): return 7
    if is_8(pattern): return 8
    if is_0(derived, pattern): return 0
    if is_2(derived, pattern): return 2
    if is_3(derived, pattern): return 3
    if is_5(derived, pattern): return 5
    if is_6(derived, pattern): return 6
    if is_9(derived, pattern): return 9
    return -1

def count_unique_outputs(signals):
    total = 0
    for (_, p_out) in signals:
        total += sum(1 for x in p_out if derive_number(None, x) != -1)
    return total

""" 
Intersect list of lists and return single remaining value,
or None when no single value (empty intersection or multiple remaining).
"""
def derive_single(lists):
    rem = set(lists[0])
    for l in lists[1:]:
        rem -= set(l)
    list_rem = list(rem)
    if len(list_rem) == 1:
        return list_rem[0]
    else:
        return None

def derive_pos_0(patterns):
    pattern_1 = next(x for x in patterns if is_1(x))
    pattern_7 = next(x for x in patterns if is_7(x))
    return derive_single([pattern_7, pattern_1])

def derive_pos_6(patterns):
    pattern_4 = next(x for x in patterns if is_4(x))
    pattern_7 = next(x for x in patterns if is_7(x))
    for p in [x for x in patterns if len(x) == 6]:
        rem = derive_single([p, pattern_4, pattern_7])
        if rem:
            return rem
    return []

def derive_pos_4(patterns, pos_0, pos_6):
    pattern_4 = next(x for x in patterns if is_4(x))
    pattern_8 = next(x for x in patterns if is_8(x))
    return derive_single([pattern_8, pattern_4, [pos_0], [pos_6]])

def derive_pos_1(patterns, pos_0, pos_4, pos_6):
    pattern_1 = next(x for x in patterns if is_1(x))
    for p in [x for x in patterns if len(x) == 6]:
        rem = derive_single([p, pattern_1, [pos_0], [pos_4], [pos_6]])
        if rem:
            return rem
    return []

def derive_pos_3(patterns, pos_0, pos_6):
    pattern_7 = next(x for x in patterns if is_7(x))
    for p in [x for x in patterns if len(x) == 5]:
        rem = derive_single([p, pattern_7, [pos_6]])
        if rem:
            return rem
    return []

def derive_pos_2(patterns, pos_0, pos_3, pos_4, pos_6):
    for p in [x for x in patterns if len(x) == 5]:
        rem = derive_single([p, [pos_0], [pos_3], [pos_4], [pos_6]])
        if rem:
            return rem
    return []

def derive_pos_5(patterns, pos_2):
    pattern_1 = next(x for x in patterns if is_1(x))
    return derive_single([pattern_1, [pos_2]])

"""
 0
1 2
 3
4 5
 6
"""
def derive_outputs(signals):
    derived = [''] * 7
    total = 0
    for (p_in, p_out) in signals:
        p = p_in + p_out
        # derive letter for each position
        derived[0] = derive_pos_0(p)
        derived[6] = derive_pos_6(p)
        derived[4] = derive_pos_4(p, derived[0], derived[6])
        derived[3] = derive_pos_3(p, derived[0], derived[6])
        derived[2] = derive_pos_2(p, derived[0], derived[3], derived[4], derived[6])
        derived[5] = derive_pos_5(p, derived[2])
        derived[1] = derive_pos_1(p, derived[0], derived[4], derived[6])
        # for each output, derive the number based on derived letters
        # combine into 4 digit number and add to total.
        total += int(''.join(str(derive_number(derived, p)) for p in p_out))
    return total

def solve_1(part, data_path):
    solve(part, data_path, parse_input, count_unique_outputs)

def solve_2(part, data_path):
    solve(part, data_path, parse_input, derive_outputs)

solve_1("Part 1", 'data/08_example.txt')
solve_1("Part 1", 'data/08_input.txt')

solve_2("Part 2", 'data/08_example.txt')
solve_2("Part 2", 'data/08_input.txt')
