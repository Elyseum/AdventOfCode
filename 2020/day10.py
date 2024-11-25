import util

example_input_1 = list(util.readlines('data/10_example_1.txt', int))
example_input_2 = list(util.readlines('data/10_example_2.txt', int))

def find_jolt_differences(adapters):
  adapters = list(adapters)
  adapters.sort(reverse = True)
  adapter_sequence = [0]
  current_voltage = 0
  voltage_differences = { 1: 0, 2: 0, 3: 0 }
  while len(adapters) > 0:
    next_adapter = adapters.pop()
    voltage_difference = next_adapter - current_voltage
    if voltage_difference in voltage_differences:
      voltage_differences[voltage_difference] += 1
      current_voltage = next_adapter
      adapter_sequence.append(next_adapter)
    else:
      break
  adapter_sequence.append(adapter_sequence[-1] + 3)
  voltage_differences[3] += 1
  return adapter_sequence, voltage_differences

def find(adapters):
  jolt_differences = find_jolt_differences(adapters)
  jolt_differences_sequence = jolt_differences[0]
  jolt_differences_count = jolt_differences[1]  
  return jolt_differences_count[1] * jolt_differences_count[3]

print(f'Puzzle 10: example 1 - {find(example_input_1)}')
print(f'Puzzle 10: example 2 - {find(example_input_2)}')

puzzle_input = list(util.readlines('data/10.txt', int))
print(f'Puzzle 10: part 1 - {find(puzzle_input)}')

def find_possible_sequences(adapters):
  jolt_differences = find_jolt_differences(adapters)
  longest_sequence = jolt_differences[0]
  longest_sequence.sort(reverse=True) # Iterate in same order as examples
  return possible_sequences(longest_sequence)

"""
Model adapter compatibility as a search tree.
The root is our adapter (highest value).
The children of an element are the adapters that are compatible with it:
* next adapter in the list (default case)
* next to one adapter in the list (in case the next is optional)
* next to two adapters in the list (in case the next to one is optional too)
Recursion step: the number of possible sequences of an element is the sum 
of the possible sequences of its children.
Recursion base case: An element with one child is a unique sequence (count 1).
For performance reasons we apply caching:
* the next to one list = 1 + next to two list
"""
def possible_sequences(adapters):
  # One adapter only has one possible sequence
  if len(adapters) == 1:
    return 1
  skip_next1 = len(adapters) >= 3 and adapters[0] - adapters[2] in [2, 3]
  skip_next2 = len(adapters) >= 4 and adapters[0] - adapters[3] == 3
  if skip_next1 and skip_next2:
    return (
      possible_sequences_cache(adapters[1:]) +
      possible_sequences_cache(adapters[2:]) +
      possible_sequences_cache(adapters[3:])
    )
  elif skip_next1:
    return (
      possible_sequences_cache(adapters[1:]) +
      possible_sequences_cache(adapters[2:])
    )
  else:
    return (
      possible_sequences_cache(adapters[1:])
    )

cache = {}
def possible_sequences_cache(adapters):
  key = '-'.join(map(str, adapters))
  if key in cache:
    return cache[key]
  else:
    value = possible_sequences(adapters)
    cache[key] = value
    return value

print(f'Puzzle 10: example 2.1 - {find_possible_sequences(example_input_1)}')
print(f'Puzzle 10: example 2.2 - {find_possible_sequences(example_input_2)}')
print(f'Puzzle 10: part 2 - {find_possible_sequences(puzzle_input)}')

