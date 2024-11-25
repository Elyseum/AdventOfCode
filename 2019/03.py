import math
import IO
import time

from functools import reduce

print("Solving Day 3")
print()

def run_wire(instructions):
    """
    Runs the wire according to the give list of instructions.
    Yields all coordinates and length to reach it.
    """
    x = 0 # From left to right
    y = 0 # From bottom to top
    runlength = 0
    points = []
    for instruction in instructions:
        # Turn 'R18' into { direction = 'R', length = 18 }.
        direction = instruction[0]
        length = int(instruction[1:])
        for _ in range(0, length):
            runlength += 1
            if   direction == 'U': y += 1
            elif direction == 'D': y -= 1
            elif direction == 'L': x -= 1
            elif direction == 'R': x += 1
            points.append({ 'coordinates' : (x, y), 'runlength': runlength })
    return points

def run_wires_manhattan(wires):
    runs = map(run_wire, wires)

    # Map runs to coordinates and find their intersections.
    run_coordinates = []
    for run in runs:
        coordinates = set(map(lambda x: x['coordinates'], run))
        run_coordinates.append(coordinates)
    intersections = reduce(lambda x, y: x.intersection(y), run_coordinates)

    # Map intersection to Manhattan distance and take shortest.
    return min(map(lambda x: abs(x[0]) + abs(x[1]), intersections))

###############################################################################
print("...Testing Part One...")

assert(6 == run_wires_manhattan([
    ['R8','U5','L5','D3'],
    ['U7','R6','D4','L4']
]))

assert(159 == run_wires_manhattan([
    ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
    ['U62','R66','U55','R34','D71','R55','D58','R83']
]))

assert(135 == run_wires_manhattan([
    ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
    ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
]))

print("All tests passed!")
print()
###############################################################################

###############################################################################
print("...Solving Part One...")

def run_wires_part_1():
    wires = IO.read_lines_list('03.txt', ',')
    return run_wires_manhattan(wires)

part_1_start = time.time()
part_1_result = run_wires_part_1()
part_1_duration = time.time() - part_1_start
print(f"Running wires part 1: {part_1_result} (solved in {part_1_duration})")
###############################################################################

###############################################################################
print("...Testing Part Two...")

print("All tests passed!")
print()
###############################################################################

def run_wires_runlength(wires):
    runs = map(run_wire, wires)

    # Map each run to its coordinates.
    # Map the coordinates of each run to the runlength to that coordinate.
    coordinates = []
    runlengths = []
    for run in runs:
        coordinates.append(set(map(lambda x: x['coordinates'], run)))
        runlengths.append({ x['coordinates'] : x['runlength'] for x in run })

    # Find the intersection points (where all wires meet).
    intersection_points = reduce(lambda x, y: x.intersection(y), coordinates)

    # Map intersection to RunLength distance and take shortest.
    intersection_distances = []
    for intersection in intersection_points:
        intersection_distances.append(sum(map(lambda x: x[intersection], runlengths)))
    return min(intersection_distances)

###############################################################################
print("Solving Part Two...")

def run_wires_part_2():
    wires = list(IO.read_lines_list('03.txt', ','))
    return run_wires_runlength(wires)

part_1_start = time.time()
part_1_result = run_wires_part_2()
part_1_duration = time.time() - part_1_start
print(f"Running wires part 1: {part_1_result} (solved in {part_1_duration})")
###############################################################################
