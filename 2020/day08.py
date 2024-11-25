import util

"""
Turns an instruction line into an (operation, number) tuple.
E.g.
* 'acc +1' -> ('acc', 1)
* 'acc -3' -> ('acc', -3)
"""
def parse_instruction(line):
  operation, number = line.split(' ')
  return (operation, int(number))

"""
Boots from the given instructions with loop protection enabled.
Returns if a loop was detected and the accumulator value at that time.
"""
def boot_no_loop(instructions):
  pointer = 0
  accumulator = 0
  visited = set() # Keep visited instructions to detect a loop
  # Keep executing as long as
  # * no loop is detected (loop protection)
  # * as long as we have instructions (terminated)
  while pointer not in visited and pointer < len(instructions):
    visited.add(pointer)
    operation, number = instructions[pointer]
    if operation == 'nop':
      pointer += 1
    elif operation == 'acc':
      accumulator += number
      pointer += 1
    elif operation == 'jmp':
      pointer += number
    else:
      raise Exception(f"Unclear what to do with '{operation}'")
  # If we still have instructions left, a loop was detected.
  loop_detected = pointer < len(instructions)
  return (loop_detected, accumulator)

example_input = list(util.readlines('data/08_example.txt', parse_instruction))
print(f'Day 08: example 1 - {boot_no_loop(example_input)}')

puzzle_input = list(util.readlines('data/08.txt', parse_instruction))
print(f'Day 08: puzzle 1 - {boot_no_loop(puzzle_input)}')

"""
For each jmp instruction in the give list of instructions,
yield a new list of instructions with that 'jmp' instruction
replaced with a 'nop' instruction.
"""
def alternative_instructions(instructions):
  for index, (operation, number) in enumerate(instructions):
    if operation == 'jmp':
      new_instructions = instructions.copy()
      new_instructions[index] = ('nop', number)
      yield new_instructions

def boot_fix(instructions):
  for alternative in alternative_instructions(instructions):
    loop_detected, accumulator = boot_no_loop(alternative)
    if not loop_detected:
      return accumulator    
  return -1

print(f'Day 08: example 2 - {boot_fix(example_input)}')
print(f'Day 08: puzzle 2 - {boot_fix(puzzle_input)}')
  
