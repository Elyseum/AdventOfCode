import util

"""
Parses a line into a structured rule:
(color, list_of_containing_bags)
with list_of_containing_bags = [(color, count)]
Example input:
* 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
* 'faded blue bags contain no other bags.'
"""
def parse_rule(line):
  parts = line.split(' bags contain ')
  color = parts[0]
  content = parts[1]
  if content == 'no other bags.':
    return (color, [])
  containing_bags = []
  for part in content.split(', '):
    content_parts = part.split(' ')
    content_count = int(content_parts[0])
    content_color = content_parts[1] + ' ' + content_parts[2]
    containing_bags.append((content_color, content_count))
  return (color, containing_bags)

def packing_options_direct(rules, color):
  options = set()
  for (rule_color, cont_bags) in rules:
    for (cont_bag_color, _) in cont_bags:
      if cont_bag_color == color:
        options.add(rule_color)
  return options

def packing_options(rules, color):
  options = set()
  colors_to_check = [color]
  while len(colors_to_check) > 0:
    color_to_check = colors_to_check.pop()
    cur = packing_options_direct(rules, color_to_check)
    for el in cur:
      if el not in options:
        options.add(el)
        colors_to_check.append(el)
  return options

def get_rule(rules, color):
  matches = [rule for rule in rules if rule[0] == color]
  if len(matches) is 1:
    return matches[0]
  else:
    return None

"""
Count of how many bags a bag of given color exists,
according to the rules.
The packing count is 
  1 (for the current bag) + 
  foreach_bag_inside
    packing_count(of the bag inside) * count of the bag inside 
"""
def packing_count(rules, color):
  rule = get_rule(rules, color)
  if rule is None:
    return 0
  count = 1 # Current bag
  containing_bags = rule[1]
  for cont_bag_color, cont_bag_count in containing_bags:
    count += cont_bag_count * packing_count(rules, cont_bag_color)
  return count

def packing_count_inside(rules, color):
  # Ignore the bag that wraps the other bags
  return packing_count(rules, color) - 1

example_input = list(util.readlines('data/07_example.txt', parse_rule))
example_1 = packing_options(example_input, 'shiny gold')
print(f'Puzzle 7: example 1 - {len(example_1)}')

puzzle_input = list(util.readlines('data/07.txt', parse_rule))
part_1 = packing_options(puzzle_input, 'shiny gold')
print(f'Puzzle 7: part 1 - {len(part_1)}')

example_2a = packing_count_inside(example_input, 'shiny gold')
print(f'Puzzle 7: example 2a - {example_2a}')

example_input_2 = list(util.readlines('data/07_example_2.txt', parse_rule))
example_2b = packing_count_inside(example_input_2, 'shiny gold')
print(f'Puzzle 7: example 2b - {example_2b}')

part_2 = packing_count_inside(puzzle_input, 'shiny gold')
print(f'Puzzle 7: part 2 - {part_2}')

