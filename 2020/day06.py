import util

def parse_groups(file_path):
  lines = util.readlines(file_path)
  lines_group = util.chunk(lambda x: x == "", lines)
  return map(lambda x: list(map(list, x)), lines_group)

def count_answers(count_group, groups):
  return sum(map(count_group, groups))

def given_by_any(members):
  answers = set()
  for member in members:
    for answer in member:
      answers.add(answer)
  return len(answers)

def given_by_all(members):
  answers = [0]*26
  for member in members:
    for answer in member:
      index = ord(answer)-ord('a')
      answers[index] = answers[index] + 1
  return sum(1 for x in answers if x is len(members))

example_input = list(parse_groups('data/06_example.txt'))
puzzle_input = list(parse_groups('data/06.txt'))

example_1 = count_answers(given_by_any, example_input)
print(f'Puzzle 6: example 1 = {example_1}')

part_1 = count_answers(given_by_any, puzzle_input)
print(f'Puzzle 6: part 1 = {part_1}')

example_2 = count_answers(given_by_all, example_input)
print(f'Puzzle 6: example 2 = {example_2}')

part_2 = count_answers(given_by_all, puzzle_input)
print(f'Puzzle 6: part 2 = {part_2}')

