import math
import re
import util

def parse_input(data_path):
    energy_levels = {}
    for y, line in enumerate(util.read_lines(data_path)):
        for x, c in enumerate(line):
            energy_levels[(x, y)] = int(c)
    return energy_levels

def get_adjacent(energy_levels, coo):
    x, y = coo
    if (x  , y-1) in energy_levels: yield ((x  , y-1), energy_levels[(x  , y-1)])
    if (x-1, y-1) in energy_levels: yield ((x-1, y-1), energy_levels[(x-1, y-1)])
    if (x+1, y-1) in energy_levels: yield ((x+1, y-1), energy_levels[(x+1, y-1)])
    #if (x  , y  ) in energy_levels: yield ((x  , y+1), energy_levels[(x ,  y+1)])
    if (x-1, y  ) in energy_levels: yield ((x-1, y  ), energy_levels[(x-1, y  )])
    if (x+1, y  ) in energy_levels: yield ((x+1, y  ), energy_levels[(x+1, y  )])
    if (x  , y+1) in energy_levels: yield ((x  , y+1), energy_levels[(x  , y+1)])
    if (x-1, y+1) in energy_levels: yield ((x-1, y+1), energy_levels[(x-1, y+1)])
    if (x+1, y+1) in energy_levels: yield ((x+1, y+1), energy_levels[(x+1, y+1)])

def flash(energy_levels, times=100):
    flash_count = 0
    for time in range(times):
        to_flash = []
        flashed = set()
        for coo, val in energy_levels.items():
            if val > 8:
                to_flash.append(coo)
            energy_levels[coo] = val+1
        while len(to_flash) > 0:
            coo = to_flash.pop(0)
            energy_levels[coo] = 0
            flashed.add(coo)
            flash_count += 1
            for ac, av in get_adjacent(energy_levels, coo):
                if ac not in flashed and ac not in to_flash:
                    if av > 8:
                        to_flash.append(ac)
                    energy_levels[ac] = av+1
    return flash_count

def flash_sync(energy_levels):
    flash_count = 0
    time = -1
    while True:
        time += 1
        to_flash = []
        flashed = set()
        for coo, val in energy_levels.items():
            if val > 8:
                to_flash.append(coo)
            energy_levels[coo] = val+1
        while len(to_flash) > 0:
            coo = to_flash.pop(0)
            energy_levels[coo] = 0
            flashed.add(coo)
            flash_count += 1
            for ac, av in get_adjacent(energy_levels, coo):
                if ac not in flashed and ac not in to_flash:
                    if av > 8:
                        to_flash.append(ac)
                    energy_levels[ac] = av+1
        if len(flashed) == len(energy_levels):
            return time+1
    return -1

def solve_1(part, data_path):
    solve(part, data_path, parse_input, flash)

def solve_2(part, data_path):
    solve(part, data_path, parse_input, flash_sync)

solve_1("Part 1", 'data/11_example.txt')
solve_1("Part 1", 'data/11_input.txt')

solve_2("Part 2", 'data/11_example.txt')
solve_2("Part 2", 'data/11_input.txt')
