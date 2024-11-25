import util

class TreeMap:

  def __init__(self, lines):
    self.rows = len(lines) # Down direction
    self.cols = len(lines[0]) # Right direction
    self.position = (0, 0) # Start position
    self.trees = set() # Positions of the trees
    for row, line in enumerate(lines):
      for col, char in enumerate(line):
        if char is '#': # Tree
          self.trees.add((row, col))

  def reset_start_position(self):
    self.position = (0, 0)

  def position_on_map(self):
    return self.position[0] <= self.rows

  """
  Moves a given number of rows and cols by updating the current 
  position and returns if the new position has a tree.
  """
  def move(self, nr_rows, nr_cols):
    current_row, current_col = self.position
    updated_row = current_row + nr_rows
    updated_col = current_col+ nr_cols
    self.position = (updated_row, updated_col)
    # The map repeats infinitely to the right,
    # we only keep the input copy in memory.
    if updated_row > self.rows:
      return False
    return (updated_row, updated_col % self.cols) in self.trees

  def traverse(self, right, down):
    self.reset_start_position()
    trees = 0
    while self.position_on_map():
      is_tree = self.move(down, right) # Switch order to match our system.
      if is_tree:
        trees += 1
    return trees

  def traverse_multiple(self, moves):
    trees_prod = 1
    for (right, down) in moves:
      trees_prod *= self.traverse(right, down)
    return trees_prod

example_input = list(util.readlines('data/03_example.txt'))

example_1 = TreeMap(example_input).traverse(right=3, down=1)
print(f'Puzzle 3: example 1 = {example_1}')

puzzle_input = list(util.readlines('data/03.txt'))
puzzle_1 = TreeMap(puzzle_input).traverse(right=3, down=1)
print(f'Puzzle 3: part 1 = {puzzle_1}')

example_2 = TreeMap(example_input).traverse_multiple([
  (1, 1),
  (3, 1),
  (5, 1),
  (7, 1),
  (1, 2)
])
print(f'Puzzle 3: example 2 = {example_2}')

puzzle_2 = TreeMap(puzzle_input).traverse_multiple([
  (1, 1),
  (3, 1),
  (5, 1),
  (7, 1),
  (1, 2)
])
print(f'Puzzle 3: part 2 = {puzzle_2}')
