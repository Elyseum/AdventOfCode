"""Day 06."""

import re
import sys
from collections import Counter

EXAMPLE_INPUT_LINES = [
    "1, 1",
    "1, 6",
    "8, 3",
    "3, 4",
    "5, 5",
    "8, 9"
]

def read_lines(file_name):
    with open(file_name) as file:
        return file.readlines()

def parse_coordinate(line):
    return tuple(map(int, re.findall(r'\d+', line)))

def parse_coordinates(lines):
    return [parse_coordinate(line) for line in lines]
    
def bouding_box(coo):
    left, top = min(x for x, y in coo), min(y for x, y in coo)
    right, bottom = max(x for x, y in coo), max(y for x, y in coo)
    return (left, right, top, bottom)

def enumerate_coordinates(box):
    left, right, top, bottom = box
    return ((x, y) for x in range(left, right + 1) for y in range(top, bottom + 1))

def enumerate_borders(box):
    left, right, top, bottom = box
    for x in range(left, right + 1):
        yield left + x, top
        yield left + x, bottom
    for y in range(top + 1, bottom):
        yield left, top + y
        yield right, top + y

def manhattan_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

def manhattan_distances(point, input):
    return list(map(lambda x: manhattan_distance(point, x), input))

def closest_manhattan_distances(point, input):
    distances = manhattan_distances(point, input)
    return [i for (i, dist) in enumerate(distances) if dist is min(distances)]

def solve(input_lines):
    coordinates = parse_coordinates(input_lines)
    box = bouding_box(coordinates)
    distances = list()
    infinite_dist = set()
    borders = set(enumerate_borders(box))
    for point in enumerate_coordinates(box):
        closest_distances = closest_manhattan_distances(point, coordinates)
        if len(closest_distances) > 1:
            continue
        elif point in borders:
            infinite_dist.add(closest_distances[0]) # Borders expand infinite
        else:
            distances.append(closest_distances[0])
    counter = Counter(x for x in distances if x not in infinite_dist)
    print(counter.most_common(1))

solve(EXAMPLE_INPUT_LINES)
# solve(read_lines("06.txt"))

def solve_2(input_lines, max_dist):
    coordinates = parse_coordinates(input_lines)
    box = bouding_box(coordinates)
    size = 0
    for point in enumerate_coordinates(box):
        if sum(manhattan_distances(point, coordinates)) < max_dist:
            size += 1
    print(size)

solve_2(EXAMPLE_INPUT_LINES, 32)
solve_2(read_lines("06.txt"), 10000)
