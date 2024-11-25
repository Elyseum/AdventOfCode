"""Day 05"""

import Helpers

def execute_jumps(jump_instructions):
    """Keep jumping until out of list, couting the steps. Returns steps"""
    steps = 0
    next_instruction = 0
    while next_instruction < len(jump_instructions):
        instruction = jump_instructions[next_instruction]
        jump_instructions[next_instruction] += 1
        next_instruction += instruction
        steps += 1

    return steps


JUMP_INSTRUCTIONS_EXAMPLE = [0, 3, 0, 1, -3]
print("Jumps until completed: " + str(execute_jumps(JUMP_INSTRUCTIONS_EXAMPLE[:])))

JUMP_INSTRUCTIONS = Helpers.read_lines_as_integers("Day05.txt")
print("Jumps until completed: " + str(execute_jumps(JUMP_INSTRUCTIONS[:])))
