import util
from collections import deque

def sliding_window(elements, window_length):
  window = deque(elements[:window_length])
  remaining = deque(elements[window_length:])
  yield list(window)
  while len(remaining) > 0:
    window.popleft()
    window.append(remaining.popleft())
    yield list(window)

"""
Returns true if the given list of numbers contains
two elements (e1 and e2) that are the sum components 
of the given number: e1 + e2 = number.
"""
def has_sum_components(numbers, number):
  seen_numbers = set()
  for component in numbers:
    complement = number - component
    if complement in seen_numbers:
      return True
    seen_numbers.add(component)
  return False

def find_sum_component_mismatch(numbers, preamble_length):
  # Performance + reuse hack:
  # The window contains the preamble and the to check number.
  # To be 100% correct, we should split those apart,
  # but it makes no difference in our implementation so we can
  # save us the effort.
  for window in sliding_window(numbers, preamble_length + 1):
    if has_sum_components(window, window[-1]) is False:
      return window[-1]
  raise Exception('Not found')
    
example_input = list(util.readlines('data/09_example.txt', int))
example_1 = find_sum_component_mismatch(example_input, 5)
print(f'Puzzel 09: example 1 - {example_1}')

puzzle_input = list(util.readlines('data/09.txt', int))
part_1 = find_sum_component_mismatch(puzzle_input, 25)
print(f'Puzzel 09: part 1 - {part_1}')

def find_encryption_weakness(numbers, invalid_number):
  for window_size in range(2, len(numbers)):
    for window in sliding_window(numbers, window_size):
      if sum(window) == invalid_number:
        return min(window) + max(window)
  return Exception('Not found')

example_2 = find_encryption_weakness(example_input, example_1)
print(f'Puzzel 09: example 2 - {example_2}')

part_2 = find_encryption_weakness(puzzle_input, part_1)
print(f'Puzzel 09: part 2 - {part_2}')

