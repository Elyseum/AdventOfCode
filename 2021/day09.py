import math
import re
import util

def parse_input(data_path):
    heightmap = {}
    for y, line in enumerate(util.read_lines(data_path)):
        for x, char in enumerate(line):
            heightmap[(x, y)] = int(char)
    return heightmap

def get_adjacent(heightmap, coo):
    x, y = coo
    if (x  , y-1) in heightmap: yield ((x  , y-1), heightmap[(x  , y-1)])
    if (x-1, y  ) in heightmap: yield ((x-1, y  ), heightmap[(x-1, y  )])
    if (x+1, y  ) in heightmap: yield ((x+1, y  ), heightmap[(x+1, y  )])
    if (x  , y+1) in heightmap: yield ((x  , y+1), heightmap[(x ,  y+1)])
            
def calculate_risk(heightmap):
    total = 0
    for (coo, value) in heightmap.items():
        if value < min(val for (coo, val) in get_adjacent(heightmap, coo)):
            total += value + 1
    return total

def expand_basin(heightmap, visited, coo):
    basin = []
    to_visit = [coo]
    while len(to_visit) > 0:
        next_visit = to_visit.pop(0)
        if next_visit in visited:
            continue
        next_value = heightmap[next_visit]
        if next_value == 9:
            continue
        basin.append(next_value)
        visited.add(next_visit)
        for (coo, val) in get_adjacent(heightmap, next_visit):
            to_visit.append(coo)
    return basin

def find_basins(heightmap):
    basins = []
    visited = set()
    for (coo, value) in heightmap.items():
        basin = expand_basin(heightmap, visited, coo)
        basins.append(basin)
    basin_sizes = list(sorted(len(x) for x in basins))
    return math.prod(basin_sizes[-3:])

def solve_1(part, data_path):
    solve(part, data_path, parse_input, calculate_risk)

def solve_2(part, data_path):
    solve(part, data_path, parse_input, find_basins)

solve_1("Part 1", 'data/09_example.txt')
solve_1("Part 1", 'data/09_input.txt')

solve_2("Part 2", 'data/09_example.txt')
solve_2("Part 2", 'data/09_input.txt')
