import util
import re

"""
Example input: '1-3 a: abcde'
Example output: (range(1, 3), 'a', 'abcde')
"""
def parse_pwd_policy(pwd_policy_str):
  parsed = re.search("(\d+)-(\d+) ([a-z]): ([a-z]+)", pwd_policy_str)
  pwd_char_range = range(int(parsed[1]), int(parsed[2]) + 1)
  pwd_char = parsed[3]
  pwd = parsed[4]
  return (pwd_char_range, pwd_char, pwd)

def is_valid_pwd(pwd_policy):
  pwd_char_range, pwd_char, pwd = pwd_policy
  return pwd.count(pwd_char) in pwd_char_range

example_input = list(util.readlines('data/02_example.txt', parse_pwd_policy))

example_1 = sum(1 for x in example_input if is_valid_pwd(x))
print(f'Puzzle 2: example 1 = {example_1}')

puzzle_input = list(util.readlines('data/02.txt', parse_pwd_policy))

part_1 = sum(1 for x in example_input if is_valid_pwd(x))
print(f'Puzzle 2: part 1 = {part_1}')

def is_valid_pwd_fixed(pwd_policy):
  pwd_char_range, pwd_char, pwd = pwd_policy
  pwd_char_pos_1 = pwd_char_range.start - 1 # 0-based index
  pwd_char_pos_2 = pwd_char_range.stop - 2 # 0-based index + stop exclusive
  match_1 = pwd_char_pos_1 < len(pwd) and pwd[pwd_char_pos_1] is pwd_char
  match_2 = pwd_char_pos_2 < len(pwd) and pwd[pwd_char_pos_2] is pwd_char
  return (match_1 or match_2) and (not (match_1 and match_2))

example_2 = sum(1 for x in example_input if is_valid_pwd_fixed(x))
print(f'Puzzle 2: example 2 = {example_2}')

part_2 = sum(1 for x in puzzle_input if is_valid_pwd_fixed(x))
print(f'Puzzle 2: part 2 = {part_2}')

