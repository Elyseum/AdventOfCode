import util
import re

required_passport_fields = [
  'byr',
  'iyr',
  'eyr',
  'hgt',
  'hcl',
  'ecl',
  'pid',
# 'cid' # Optional
]

def parse_passports(file_path):
  lines = util.readlines(file_path)
  lines_passport = util.chunk(lambda x: x == "", lines)
  return map(parse_passport, lines_passport)

"""
A passport is a list of (passport_field, passport_value) tuples.
It's parsed from multiple lines, each containing one or more words
of the form 'passport_field:passport_value'.
"""
def parse_passport(lines):
  parsed = (line.split(' ') for line in lines)
  parsed = (word for line in parsed for word in line)
  parsed = (x.split(':') for x in parsed)
  parsed = ((x[0], x[1]) for x in parsed)
  return list(parsed)

def has_fields(passport):
  passport_fields = [x[0] for x in passport]
  for field in required_passport_fields:
    if field not in passport_fields:
      return False
  return True

def count_valid_passports(passports):
  return sum(1 for x in passports if has_fields(x))

example_input = parse_passports('data/04_example.txt')
example_1 = count_valid_passports(example_input)
print(f'Puzzle 4: example 1 = {example_1}')

puzzle_input = parse_passports('data/04.txt')
part_1 = count_valid_passports(puzzle_input)
print(f'Puzzle 4: part 1 = {part_1}')

def is_valid_hgt(value):
  matches = re.search('^(\d+)(cm|in)$', value)
  if matches and matches[2] == 'cm':
    return int(matches[1]) in range(150, 194)
  elif matches and matches[2] == 'in':
    return int(matches[1]) in range(59, 77)
  return False

passport_field_validation = {
  'byr': lambda x: int(x) in range(1920, 2003),
  'iyr': lambda x: int(x) in range(2010, 2021),
  'eyr': lambda x: int(x) in range(2020, 2031),
  'hgt': is_valid_hgt,
  'hcl': lambda x: re.match('^\#[0-9a-f]{6}$', x) is not None,
  'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
  'pid': lambda x: re.match('^[0-9]{9}$', x) is not None,
  'cid': lambda x: True
}

def test_is_valid_field_value(field, value, exp):
  act = passport_field_validation[field](value)
  inp = f'{field}:{value}'
  print(f"Puzzle 4: Validating '{inp}'. Expected '{exp}', actual '{act}'")

test_is_valid_field_value('byr', 2002, True)
test_is_valid_field_value('byr', 2003, False)
test_is_valid_field_value('hgt', '60in', True)
test_is_valid_field_value('hgt', '190cm', True)
test_is_valid_field_value('hgt', '190in', False)
test_is_valid_field_value('hgt', '190', False)
test_is_valid_field_value('hcl', '#123abc', True)
test_is_valid_field_value('hcl', '#123abz', False)
test_is_valid_field_value('hcl', '123abc', False)
test_is_valid_field_value('ecl', 'brn', True)
test_is_valid_field_value('ecl', 'wat', False)
test_is_valid_field_value('pid', '000000001', True)
test_is_valid_field_value('pid', '0123456789', False)
  
def is_valid(passport):
  for (field, value) in passport:
    validator = passport_field_validation[field]
    if validator(value) is False:
      return False
  return True

def count_present_valid_passports(passports):
  present_valid = lambda x: has_fields(x) and is_valid(x)
  return sum(1 for passport in passports if present_valid(passport))

example_2_invalid = count_present_valid_passports(
  parse_passports('data/04_example_invalid.txt'))
print(f'Puzzle 4: example 2.invalid = {example_2_invalid} are valid')

example_2_valid = count_present_valid_passports(
  parse_passports('data/04_example_valid.txt'))
print(f'Puzzle 4: example 2.valid = {example_2_valid} are valid')

puzzle_input = parse_passports('data/04.txt')
part_2 = count_present_valid_passports(puzzle_input)
print(f'Puzzle 4: part 2 = {part_2}')

