"""Day 10."""

import re
import time
from collections import Counter

EXAMPLE_INPUT_LINES = [
    "position=< 9,  1> velocity=< 0,  2>",
    "position=< 7,  0> velocity=<-1,  0>",
    "position=< 3, -2> velocity=<-1,  1>",
    "position=< 6, 10> velocity=<-2, -1>",
    "position=< 2, -4> velocity=< 2,  2>",
    "position=<-6, 10> velocity=< 2, -2>",
    "position=< 1,  8> velocity=< 1, -1>",
    "position=< 1,  7> velocity=< 1,  0>",
    "position=<-3, 11> velocity=< 1, -2>",
    "position=< 7,  6> velocity=<-1, -1>",
    "position=<-2,  3> velocity=< 1,  0>",
    "position=<-4,  3> velocity=< 2,  0>",
    "position=<10, -3> velocity=<-1,  1>",
    "position=< 5, 11> velocity=< 1, -2>",
    "position=< 4,  7> velocity=< 0, -1>",
    "position=< 8, -2> velocity=< 0,  1>",
    "position=<15,  0> velocity=<-2,  0>",
    "position=< 1,  6> velocity=< 1,  0>",
    "position=< 8,  9> velocity=< 0, -1>",
    "position=< 3,  3> velocity=<-1,  1>",
    "position=< 0,  5> velocity=< 0, -1>",
    "position=<-2,  2> velocity=< 2,  0>",
    "position=< 5, -2> velocity=< 1,  2>",
    "position=< 1,  4> velocity=< 2,  1>",
    "position=<-2,  7> velocity=< 2, -2>",
    "position=< 3,  6> velocity=<-1, -1>",
    "position=< 5,  0> velocity=< 1,  0>",
    "position=<-6,  0> velocity=< 2,  0>",
    "position=< 5,  9> velocity=< 1, -2>",
    "position=<14,  7> velocity=<-2,  0>",
    "position=<-3,  6> velocity=< 2, -1>"
]

def parse_line(line):
    x, y, vx, vy = map(int, re.findall(r'\-?\d+', line))
    return x, y, vx, vy

def move(i):
    x, y, vx, vy = i
    return x + vx, y + vy, vx, vy

def move_all(input):
    duration = 0
    while not is_readable(input):
        duration += 1
        input = list(map(move, input))
    print(f"Duration: {duration}")
    return input

def is_readable(input):
    points = set(map(lambda x_y: (x_y[0], x_y[1]), input))
    min_height = min(map(lambda x_y: x_y[1], input))
    for (x, y) in (x_y for x_y in points if x_y[1] is min_height):
        if (x, y + 4) in points and (x, y + 3) in points and (x, y + 2) in points and (x, y + 1) in points:
            return True
    return False

print("Example parsing: " + str(parse_line(EXAMPLE_INPUT_LINES[-1])))

EXAMPLE_INPUT = list(map(parse_line, EXAMPLE_INPUT_LINES))
print(EXAMPLE_INPUT)

def print_coordinates(coo):
    width_min, width_max = min(c[0] for c in coo), max(c[0] for c in coo)
    height_min, height_max = min(c[1] for c in coo), max(c[1] for c in coo)
    points = set(map(lambda x_y: f"{x_y[0]}_{x_y[1]}", coo))
    for y in range(height_min, height_max + 1):
        line = ""
        for x in range(width_min, width_max + 1):
            line += "#" if f"{x}_{y}" in points else "."
        print(line)

print_coordinates(EXAMPLE_INPUT)
print(is_readable(EXAMPLE_INPUT))
print("")
MOVED = move_all(EXAMPLE_INPUT)
print_coordinates(MOVED)
print(is_readable(MOVED))

def read_input(file_name):
    with open(file_name) as file:
        return map(parse_line, file.readlines())

INPUT = list(read_input("10.txt"))

start = time.time()
print_coordinates(move_all(INPUT))
elapsed = time.time() - start
print(f"Duration {elapsed}s")