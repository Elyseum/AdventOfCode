import util

def arrive(grid):
  change = [None]
  iterations = 0
  adjacent_coordinates = create_adjacent_coordinates(grid)
  while len(change) > 0:
    change.clear()
    # Collect the changes
    for x, y, coo in adjacent_coordinates:
      if grid[x][y] == 'L' and not has_min_seats(grid, coo, '#', 0):
        change.append((x, y, '#'))
      elif grid[x][y] == '#' and has_min_seats(grid, coo, '#', 4):
        change.append((x, y, 'L'))
    # Apply the changes
    for (x, y, value) in change:
      grid[x][y] = value
    iterations += 1
  return util.count_occurrences_grid(grid, '#')

def create_adjacent_coordinates(grid):
  coordinates = []
  x_range = range(0, len(grid))
  y_range = range(0, len(grid[0]))
  for x in x_range:
    for y in y_range:
      adjacent = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x  , y-1),           (x  , y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1)
      ]
      adjacent = [c for c in adjacent
                  if c[0] in x_range and c[1] in y_range]
      coordinates.append((x, y, adjacent))
  return coordinates

def has_min_seats(grid, coordinates, value, min_count):
  counter = 0
  for (x, y) in coordinates:
    if grid[x][y] == value:
      counter += 1
      if counter >= min_count:
        return True
  return False

example_input = list(util.readlines('data/11_example.txt', list))
print(f'Puzzle 11: ex. 1 - {arrive(example_input)}')

puzzle_input = list(util.readlines('data/11.txt', list))
print(f'Puzzle 11: part 1 - {arrive(puzzle_input)}')

def arrive_sight(grid):
  change = [None]
  iterations = 0
  adjacent_coo_sight = create_adjacent_coo_sight(grid)
  while len(change) > 0:
    change.clear()
    # Collect the changes
    for x, y, coo in adjacent_coo_sight:
      if grid[x][y] == 'L' and not has_min_seats_sight(grid, coo, '#', 0):
        change.append((x, y, '#'))
      elif grid[x][y] == '#' and has_min_seats_sight(grid, coo, '#', 5):
        change.append((x, y, 'L'))
    # Apply the changes
    for (x, y, value) in change:
      grid[x][y] = value
    iterations += 1
  return util.count_occurrences_grid(grid, '#')

def create_adjacent_coo_sight(grid):
  coordinates = []
  x_range = range(0, len(grid))
  y_range = range(0, len(grid[0]))
  for x in x_range:
    for y in y_range:
      adjacent = []
      adjacent.append(get_coo_in_sight(x_range, y_range, x, -1, y, -1))
      adjacent.append(get_coo_in_sight(x_range, y_range, x, -1, y, +0))
      adjacent.append(get_coo_in_sight(x_range, y_range, x, -1, y, +1))
      adjacent.append(get_coo_in_sight(x_range, y_range, x, +0, y, -1))
      adjacent.append(get_coo_in_sight(x_range, y_range, x, +0, y, +1))
      adjacent.append(get_coo_in_sight(x_range, y_range, x, +1, y, -1))
      adjacent.append(get_coo_in_sight(x_range, y_range, x, +1, y,  0))
      adjacent.append(get_coo_in_sight(x_range, y_range, x, +1, y, +1))
      coordinates.append((x, y, adjacent))
  return coordinates

def get_coo_in_sight(x_range, y_range, x, x_offset, y, y_offset):
  coordinates = []
  x_coo = x + x_offset
  y_coo = y + y_offset
  while x_coo in x_range and y_coo in y_range:
    coordinates.append((x_coo, y_coo))
    x_coo += x_offset
    y_coo += y_offset
  return coordinates

def has_min_seats_sight(grid, coo_sight, value, min_count):
  counter = 0
  for coo_direction in coo_sight:
    for (x, y) in coo_direction:
      # Ignore empty spaces
      if grid[x][y] == '.':
        continue
      # Visible match: count it and break to next direction
      # Return if min_count is met
      if grid[x][y] == value:
        counter += 1
        if counter >= min_count:
          return True
        break
      # No visible match: break to next direction
      else:
        break
  return False

example_input = list(util.readlines('data/11_example.txt', list))
print(f'Puzzle 11: ex. 2 - {arrive_sight(example_input)}')

puzzle_input = list(util.readlines('data/11.txt', list))
print(f'Puzzle 11: part 2 - {arrive_sight(puzzle_input)}')

