import math
import IO

print("Solving Day 1")
print()

def req_fuel(mass):
    return math.floor(mass / 3) - 2

def req_fuel_total(mass):
    total = 0
    while mass > 0:
        mass = req_fuel(mass)
        if mass > 0:
            total += mass
    return total

###############################################################################
print("...Testing Part One...")
assert(req_fuel(12) == 2)
assert(req_fuel(14) == 2)
assert(req_fuel(1969) == 654)
assert(req_fuel(100756) == 33583)
print("All tests passed!")
print()
###############################################################################

###############################################################################
print("...Solving Part One...")

def calculate_fuel_req():
    input = IO.read_lines('01.txt', int)
    return sum(map(req_fuel, input))

print(f"Sum of fuel requirements: {calculate_fuel_req()}")
print()
###############################################################################

###############################################################################
print("...Testing Part Two...")
assert(req_fuel_total(14) == 2)
assert(req_fuel_total(1969) == 966)
assert(req_fuel_total(100756) == 50346)
print("All tests passed!")
print()
###############################################################################

###############################################################################
print("Solving Part Two...")

def calculate_total_fuel_req():
    input = IO.read_lines('01.txt', int)
    return sum(map(req_fuel_total, input))

print(f"Sum of total fuel requirements: {calculate_total_fuel_req()}")
###############################################################################
