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

def parse_lines(lines):
    return [parse_coordinate(line) for line in lines]

def bounding_box(coo):
    left_top = (min(x for x, y in coo), min(y for x, y in coo))
    right_bottom = (max(x for x, y in coo), max(y for x, y in coo))
    width = right_bottom[0] - left_top[0] + 1
    height = right_bottom[1] - left_top[1] + 1
    return left_top, width, height

def bounding_box_array(bounding_box):
    (left_top_x, left_top_y), box_width, box_height = bounding_box
    width = left_top_x + box_width
    height = left_top_y + box_height
    return [[None for x in range(height)] for y in range(width)]

def manhattan_distance(point1, point2):
    horizontal_distance = abs(point2[0] - point1[0])
    vertical_distance = abs(point2[1] - point1[1])
    return horizontal_distance + vertical_distance

def print_2d_array(array, input):
    input_set = set(input)
    width, height = len(array), len(array[0])
    for h in range(height):
        line = ""
        for w in range(width):
            value = array[w][h]
            if value is None or value is -1:
                line += "."
            elif (w, h) in input_set:
                line += chr(97 + value).swapcase()
            else:
                line += chr(97 + value)
        print(line)

def get_closest(point, input):
    distances = list(map(lambda x: manhattan_distance(point, x), input))
    return [i for (i, dist) in enumerate(distances) if dist is min(distances)]

def mark_positions(box_array, box, input):
    (left_top_x, left_top_y), box_width, box_height = box
    for x in range(left_top_x, left_top_x + box_width):
        for y in range(left_top_y, left_top_y + box_height):
            closest = get_closest((x, y), input)
            box_array[x][y] = closest[0] if len(closest) == 1 else -1

def count_finite_areas(box_array, box):
    """
    Counts all values in the box array.
    Ignores values on the border, because their areas are infinite.
    """
    (left_top_x, left_top_y), box_width, box_height = box

    ignore = set()
    for x in range(box_width):
        ignore.add(box_array[left_top_x + x][left_top_y])
        ignore.add(box_array[left_top_x + x][left_top_y + box_height - 1])
    for y in range(box_height):
        ignore.add(box_array[left_top_x][left_top_y + y])
        ignore.add(box_array[left_top_x + box_width - 1][left_top_y + y])
    
    values = []
    for x in range(left_top_x, left_top_x + box_width):
        for y in range(left_top_y, left_top_y + box_height):
            if box_array[x][y] not in ignore:
                values.append(box_array[x][y])
    return Counter(values).most_common(1)

def solve(input_lines, debug):
    input = parse_lines(input_lines)
    if debug:
        print("Example input: " + str(input))
    box = bounding_box(input)
    if debug:
        print("Bounding box: " + str(box))
    box_array = bounding_box_array(box)
    mark_positions(box_array, box, input)
    if debug:
        print("Box array:")
        print_2d_array(box_array, input)
    max_finite_area = count_finite_areas(box_array, box)
    print(max_finite_area)

solve(EXAMPLE_INPUT_LINES, True)

solve(read_lines("06.txt"), False)
