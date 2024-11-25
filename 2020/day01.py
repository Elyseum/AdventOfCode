import util

"""
Iterate all numbers and check if the complement of the current exists.
If so, we found the solution.
Complexity is O(n) (instead of O(n*n)).
"""
def complement_solve(numbers, value):
  seen = set()
  for number in numbers:
    complement = value - number
    if complement in seen:
      return number * complement
    else:
      seen.add(number)
  return -1

example_input = list(util.readlines('data/01_example.txt', int))

example_1 = complement_solve(example_input, 2020)
print(f'Puzzle 1: example 1 = {example_1}')

puzzle_input = list(util.readlines('data/01.txt', int))

part_1 = complement_solve(puzzle_input, 2020)
print(f'Puzzle 1: part 1 = {part_1}')

"""
Recursive style: the complement (x, y, z) for a 'value'
is the complement of (x, y) for 'value - z'.
Complexity is O(n*n) (instead of O(n*n*n)).
"""
def complement3_solve(numbers, value):
  for number in numbers:
    complement2 = complement_solve(numbers, value - number)
    if complement2 is not -1:
      return number * complement2
  return -1

example_2 = complement3_solve(example_input, 2020)
print(f'Puzzle 1: example 2 = {example_2}')

part_2 = complement3_solve(puzzle_input, 2020)
print(f'Puzzle 1: part 2 = {part_2}')

