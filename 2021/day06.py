import re
import util

from functools import lru_cache

def parse_input(data_path):
    line = next(util.read_lines(data_path))
    return [int(x) for x in line.split(',')]

def get_spawns(state, day, day_max):
    next_spawn = day + state + 1
    while next_spawn <= day_max:
        yield (8, next_spawn)
        next_spawn += 7

"""
In essence we are looking for multiples of 7 for values [1, 6],
starting from different offsets.
The first spawns will generate lots of unique values in the full range,
so the more we spawn, the more likely we are to repeat ourselves:
by leveraging caching we have a huge performance gain. 
"""
@lru_cache(maxsize=1024)
def spawn_rec(state, day, days):
    spawns = get_spawns(state, day, days)
    return 1 + sum(spawn_rec(x[0], x[1], days) for x in spawns)

def spawn(states, days):
    return sum(spawn_rec(x, 0, days) for x in states)
        
def solve_1(part, data_path):
    solve(part, data_path, parse_input, lambda x: spawn(x, 80))

def solve_2(part, data_path):
    solve(part, data_path, parse_input, lambda x: spawn(x, 256))

solve_1("Part 1", 'data/06_example.txt')
solve_1("Part 1", 'data/06_input.txt')

solve_2("Part 2", 'data/06_example.txt')
solve_2("Part 2", 'data/06_input.txt')
