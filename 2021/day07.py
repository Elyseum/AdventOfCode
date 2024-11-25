import math
import re
import util

def parse_input(data_path):
    line = next(util.read_lines(data_path))
    return [int(x) for x in line.split(',')]

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    s_numbers = sorted(numbers)
    mid1 = len(numbers) // 2 - 1
    mid2 = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return round((s_numbers[mid1] + s_numbers[mid2]) / 2)
    else:
        return s_numbers[mid2]

def min_fuel(numbers):
    # Median should be closest value of all values in the list.
    m1 = median(numbers)
    return sum(abs(m1 - x) for x in numbers)

def fuel_cost_exp(fr, to):
    dist = abs(to - fr)
    return (dist * (dist + 1)) // 2

def min_fuel_exp(numbers):
    # You find the target value by minimizing the cost function,
    # which is the sum of triangular numbers (derive + eq to 0).
    # The target value is 1/2 away from the average.
    mean_numbers = mean(numbers)
    mean_low = math.floor(mean_numbers)
    mean_high = math.ceil(mean_numbers)
    return min(
        sum(fuel_cost_exp(x, mean_low) for x in numbers),
        sum(fuel_cost_exp(x, mean_high) for x in numbers)
    )

def solve_1(part, data_path):
    solve(part, data_path, parse_input, min_fuel)

def solve_2(part, data_path):
    solve(part, data_path, parse_input, min_fuel_exp)

solve_1("Part 1", 'data/07_example.txt')
solve_1("Part 1", 'data/07_input.txt')

solve_2("Part 2", 'data/07_example.txt')
solve_2("Part 2", 'data/07_input.txt')
