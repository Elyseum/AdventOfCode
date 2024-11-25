import math
import re
import util

def parse_input(data_path):
    return util.read_lines(data_path)

COMPLEMENTS = { '(' : ')', '[' : ']', '{' : '}', '<' : '>' }
OPEN_BRACKETS = complements.keys()

def illegal_close(line):
    opened = []
    for l in line:
        if l in OPEN_BRACKETS:
            opened.append(l)
        elif l != COMPLEMENTS[opened.pop()]:
            return l
    return None

def fix_close(line):
    opened = []
    for l in line:
        if l in OPEN_BRACKETS:
            opened.append(l)
        else:
            opened.pop()
    return [COMPLEMENTS[x] for x in reversed(opened)]

def count_illegal(lines):
    scores = { ')' : 3, ']': 57, '}': 1197, '>': 25137 }
    illegal_closes = [illegal_close(x) for x in lines]
    return sum(scores[x] for x in illegal_closes if x)

def fix_incomplete(lines):
    scores = { ')' : 1, ']': 2, '}': 3, '>': 4 }
    totals = []
    for line in [x for x in lines if not illegal_close(x)]:
        total = 0
        for score in [scores[x] for x in fix_close(line)]:
            total *= 5
            total += score
        totals.append(total)
    return sorted(totals)[len(totals) // 2]

def solve_1(part, data_path):
    solve(part, data_path, parse_input, count_illegal)

def solve_2(part, data_path):
    solve(part, data_path, parse_input, fix_incomplete)

solve_1("Part 1", 'data/10_example.txt')
solve_1("Part 1", 'data/10_input.txt')

solve_2("Part 2", 'data/10_example.txt')
solve_2("Part 2", 'data/10_input.txt')
