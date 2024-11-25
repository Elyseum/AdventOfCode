import math
import IO

from datetime import datetime

print(f"Solving Day {__file__.split('.')[0]}")
print()

def get_instr_val(instructions, pointer, param_mode):
    input_param = instructions[pointer]
    if param_mode is 0: # pointer mode
        return instructions[input_param]
    else:               # input mode
        return input_param

def execute_int_code(instructions, prog_input=None):
    pointer = 0
    while True:
        instruction = instructions[pointer]
        opcode  = instruction % 100
        input_1_mode = int(instruction / 100) % 10
        input_2_mode = int(instruction / 1000) % 10
        # Stop immediately so we don't cross input array boundaries.
        if opcode == 99:
            return instructions
        if opcode == 1:
            input_1 = get_instr_val(instructions, pointer + 1, input_1_mode)
            input_2 = get_instr_val(instructions, pointer + 2, input_2_mode)
            output_param = instructions[pointer + 3]
            instructions[output_param] = input_1 + input_2
            pointer += 4
        elif opcode == 2:
            input_1 = get_instr_val(instructions, pointer + 1, input_1_mode)
            input_2 = get_instr_val(instructions, pointer + 2, input_2_mode)
            output_param = instructions[pointer + 3]
            instructions[output_param] = input_1 * input_2
            pointer += 4
        elif opcode == 3:
            output_param = instructions[pointer + 1]
            instructions[output_param] = prog_input
            pointer += 2
        elif opcode == 4:
            input_1_param = instructions[pointer + 1]
            input_1 = instructions[input_1_param]
            print(input_1)
            pointer += 2
        elif opcode == 5:
            input_1 = get_instr_val(instructions, pointer + 1, input_1_mode)
            if input_1 != 0:
                pointer = get_instr_val(instructions, pointer + 2, input_2_mode)
            else:
                pointer += 3
        elif opcode == 6:
            input_1 = get_instr_val(instructions, pointer + 1, input_1_mode)
            if input_1 == 0:
                pointer = get_instr_val(instructions, pointer + 2, input_2_mode)
            else:
                pointer += 3
        elif opcode == 7:
            input_1 = get_instr_val(instructions, pointer + 1, input_1_mode)
            input_2 = get_instr_val(instructions, pointer + 2, input_2_mode)
            output_param = instructions[pointer + 3]
            if input_1 < input_2:
                instructions[output_param] = 1
            else:
                instructions[output_param] = 0
            pointer += 4
        elif opcode == 8:
            input_1 = get_instr_val(instructions, pointer + 1, input_1_mode)
            input_2 = get_instr_val(instructions, pointer + 2, input_2_mode)
            output_param = instructions[pointer + 3]
            if input_1 == input_2:
                instructions[output_param] = 1
            else:
                instructions[output_param] = 0
            pointer += 4
        else:
            raise Exception(f"Unknown opcode {opcode} (instruction {instruction})")
    raise Exception("Failed to complete")

###############################################################################
print("...Testing Part One...")
assert(execute_int_code([1,0,0,0,99]) == [2,0,0,0,99])
assert(execute_int_code([2,3,0,3,99]) == [2,3,0,6,99])
assert(execute_int_code([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
assert(execute_int_code([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])

execute_int_code([1002,4,3,4,33], 1)

assert(execute_int_code([3,0,4,0,99], 1))

print("All tests passed!")
print()
###############################################################################

###############################################################################
print("...Solving Part One...")

def run_int_code():
    instructions = IO.read_line_list('05.txt', transform=int)
    return execute_int_code(instructions, 1)[0]

print(f"Int code executed: {run_int_code()}")
print()
###############################################################################

print("...Testing Part Two...")

print("Test should print 0:")
execute_int_code([3,9,8,9,10,9,4,9,99,-1,8], 4)

print("Test should print 1:")
execute_int_code([3,9,8,9,10,9,4,9,99,-1,8], 8)

print("Test should print 0:")
execute_int_code([3,9,8,9,10,9,4,9,99,-1,8], 9)

print("Test should print 1000:")
execute_int_code(
    [
        3,21,1008,21,8,20,1005,20,22,107,8,21,
        20,1006,20,31,1106,0,36,98,0,0,1002,21,
        125,20,4,20,1105,1,46,104, 999,1105,1,
        46,1101,1000,1,20,4,20,1105,1,46,98,99
    ],
    8)

print("Test should print 0")
execute_int_code([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0)

print("Test should print 1")
execute_int_code([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 1)

print("All tests passed!")
print()
###############################################################################
IO.log("Solving Part Two...")

def determine_int_code():
    instructions = IO.read_line_list('05.txt', transform=int)
    return execute_int_code(instructions, 5)[0]

IO.log(f"Determined Int Code: {determine_int_code()}")
###############################################################################
