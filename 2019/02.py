import math
import IO

from datetime import datetime

print("Solving Day 2")
print()

def execute_int_code(instructions):
    pointer = -4 # Makes sure we start on 0 when staring the first iteration.
    while True:
        pointer += 4
        opcode  = instructions[pointer + 0]
        # Stop immediately so we don't cross input array boundaries.
        if opcode == 99:
            return instructions
        input_1_param   = instructions[pointer + 1]
        input_1         = instructions[input_1_param]
        input_2_param   = instructions[pointer + 2]
        input_2         = instructions[input_2_param]
        output_param    = instructions[pointer + 3]
        if opcode == 1:
            instructions[output_param] = input_1 + input_2
        else:
            instructions[output_param] = input_1 * input_2
    return instructions[0]

###############################################################################
print("...Testing Part One...")
assert(execute_int_code([1,0,0,0,99]) == [2,0,0,0,99])
assert(execute_int_code([2,3,0,3,99]) == [2,3,0,6,99])
assert(execute_int_code([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
assert(execute_int_code([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])
print("All tests passed!")
print()
###############################################################################

###############################################################################
print("...Solving Part One...")

def run_int_code():
    instructions = IO.read_line_list('02.txt', transform=int)
    instructions[1] = 12
    instructions[2] = 2
    return execute_int_code(instructions)[0]

print(f"Int code executed: {run_int_code()}")
print()
###############################################################################

###############################################################################
IO.log("Solving Part Two...")

def determine_int_code():
    original_instructions = IO.read_line_list('02.txt', transform=int)

    # Binary search a good starting point for i.
    i = 1
    while i < 99:
        instructions = original_instructions.copy()
        instructions[1] = i
        if execute_int_code(instructions)[0] >= 19690720:
            break
        i *= 2
    i_start = int(i / 2)
    print(f"i_start = {i_start}")

    for i in range(i_start, 100):
        for j in range(0, 100):
            instructions = original_instructions.copy()
            instructions[1] = i
            instructions[2] = j
            if execute_int_code(instructions)[0] == 19690720:
                print(f"i = {i}, j = {j}")
                return 100 * instructions[1] + instructions[2]
    return -1

IO.log(f"Determined Int Code: {determine_int_code()}")
###############################################################################
