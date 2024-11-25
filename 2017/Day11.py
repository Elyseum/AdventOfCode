"""Day11"""

import Helpers

DIRECTIONS = {
    'n': (0, 1),
    'e': (1, 0),
    's': (0, -1),
    'w': (-1, 0),
    'ne': (0.5, 0.5),
    'se': (0.5, -0.5),
    'nw': (-0.5, 0.5),
    'sw': (-0.5, -0.5)
}

def move(point, direction):
    return (point[0] + direction[0], point[1] + direction[1])

def walk(instructions):
    point = (0, 0)
    positions = []
    for instruction in instructions:
        point = move(point, DIRECTIONS[instruction])
        positions.append((point, distance(point)))
    return positions

def distance(point):
    return abs(point[0]) + abs(point[1])

INSTRUCTIONS = Helpers.read_line_as_list("Day11.txt")
WALK = walk(INSTRUCTIONS)

END = WALK[-1]
print("End point: " + str(END[0]) + ". Distance: " + str(END[1]))
FURTHEST = max(WALK, key=lambda x: x[1])
print("Furthest point: " + str(FURTHEST[0]) + ". Distance: " + str(FURTHEST[1]))
