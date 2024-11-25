import util

"""Turn 'F10' into ('F', 10)."""
def parse_instruction(line):
  return (line[0], int(line[1:]))

def move(instructions):
  east, north, orientation = 0, 0, 'east'
  for (direction, distance) in instructions:
    if direction == 'F':
      if orientation == 'east': east += distance
      elif orientation == 'west': east -= distance
      elif orientation == 'north': north += distance
      elif orientation == 'south': north -= distance
      else: raise Exception(f'Unknown orientation {orientation}')
    elif direction == 'N': north += distance
    elif direction == 'S': north -= distance
    elif direction == 'E': east += distance
    elif direction == 'W': east -= distance
    elif direction == 'R': orientation = rotate(orientation, 'R', distance)
    elif direction == 'L': orientation = rotate(orientation, 'L', distance)
    else: raise Exception('Unknown direction ' + direction)
  return (east, north, orientation)

def rotate(orientation, direction, degrees):
  orientations = ['east', 'south', 'west', 'north']
  rotations = int(degrees / 90)
  if direction == 'L':
    rotations *= -1
  cur_direction_index = orientations.index(orientation)
  new_direction_index = (cur_direction_index + rotations) % 4
  return orientations[new_direction_index]

def manhattan_dist(position):
  east, north, orientation = position
  return abs(east) + abs(north)

example_input = list(util.readlines('data/12_example.txt', parse_instruction))
print(f'Puzzle 12: ex. 1 - {manhattan_dist(move(example_input))}')

puzzle_input = list(util.readlines('data/12.txt', parse_instruction))
print(f'Puzzle 12: part 1 - {manhattan_dist(move(puzzle_input))}')

def move_waypoint(instructions):
  east, north, orientation = 0, 0, 'east' # Position absolute to the grid.
  east_w, north_w = 10, 1 # Position relative to the position of the ship.
  for (direction, distance) in instructions:
    if direction == 'F':
      east += east_w * distance
      north += north_w * distance
    elif direction == 'N':
      north_w += distance
    elif direction == 'S':
      north_w -= distance
    elif direction == 'E':
      east_w += distance
    elif direction == 'W':
      east_w -= distance
    elif direction == 'R':
      east_w, north_w = rotate_coo(east_w, north_w, 'R', distance)
    elif direction == 'L':
      east_w, north_w = rotate_coo(east_w, north_w, 'L', distance)
    else:
      raise Exception('Unknown direction ' + direction)
  return (east, north, orientation)

def rotate_coo(x, y, direction, degrees):
  times = int(degrees / 90)
  for i in range(times):
    if direction == 'R':
      x, y = y, -x
    else:
      x, y = -y, x
  return (x, y)

print(f'Puzzle 12: ex. 2 - {manhattan_dist(move_waypoint(example_input))}')
print(f'Puzzle 12: part 2 - {manhattan_dist(move_waypoint(puzzle_input))}')

