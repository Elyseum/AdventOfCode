# Collection of utility methods to solve the puzzles

"""
Reads the lines of a file into an enumerable,
removing new line character at the end of each line
and optionally applying additional mapping.
"""
def readlines(file, mapper=None):
  with open(file) as f:
    lines = map(lambda x: x.rstrip('\n'), f.readlines())
    if mapper is not None:
      lines = map(mapper, lines)
    return lines

"""
Split an enumerable of elements into chunks,
using a split(element) as a trigger to start
a new chunk.
"""
def chunk(split, elements, include_split=False):
  chunk_list = list()
  for el in elements:
    if split(el):
      if include_split:
        chunk_list.append(el)
      yield chunk_list
      chunk_list = list()
    else:
      chunk_list.append(el)
  if len(chunk_list) > 0:
    yield chunk_list


### Grid stuff ###
    
def count_occurrences_grid(grid, value):
  occurrences = 0
  for x in range(0, len(grid)):
    for y in range(0, len(grid[x])):
      if grid[x][y] == value:
        occurrences += 1
  return occurrences

def print_grid(grid):
  for row in grid:
    print(''.join(row))
  print("")
