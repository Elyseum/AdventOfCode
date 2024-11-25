# Collection of utility methods to solve the puzzles

import pyperclip
import time

"""
Template to solve a puzzle.

"""
def solve(part, data_path, data_parser, executor):
    start = time.time()
    parsed = data_parser(data_path)
    result = executor(parsed)
    took = time.time() - start
    print(f"{part} ({data_path}): {result} (took {took}ms)")
    if result:
      pyperclip.copy(result)

"""
Reads the lines of a file into an enumerable,
removing new line character at the end of each line
and optionally applying additional mapping.
"""
def read_lines(file, mapper=None):
  with open(file) as f:
    lines = map(lambda x: x.rstrip('\n'), f.readlines())
    if mapper is not None:
      lines = map(mapper, lines)
    return lines

def read_parts(file):
  with open(file) as f:
    return [x.rstrip('\n') for x in f.read().split('\n\n')]

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

def chunk_size(size, elements):
    chunk_list = []
    for el in elements:
        if len(chunk_list) == size:
            yield list(chunk_list)
            chunk_list = []
        chunk_list.append(el)
    if len(chunk_list) > 0:
        yield list(chunk_list)

def transpose(lists):
  # Eeach column becomes a row.
  nr_columns = len(lists[0])
  transposed = [[] for x in range(nr_columns)]
  for i in range(nr_columns):
    for l in lists:
      transposed[i].append(l[i])
  return transposed

"""
Returns a list of elements that are appear in both of the given lists.
"""
def intersection(l1, l2):
  return list(set(x for x in l1 if x in l2))

def flatten(l):
  return [item for sublist in l for item in sublist]

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

def get_coordinates_adjacent(coo):
  row = coo[0]
  col = coo[1]
  yield (row-1, col-1)
  yield (row-1, col)
  yield (row-1, col+1)
  yield (row, col-1)
  yield (row, col+1)
  yield (row+1, col-1)
  yield (row+1, col)
  yield (row+1, col+1)

# Gets the coordinates of the elements in a given lst, starting from coo.
# E.g. if lst ['a','b','c'] starts at coo (1,2), we yield [(1,2), (1,3), (1,4)].
def get_coordinates_lst(lst, coo):
  for i in range(len(lst)):
    yield (coo[0], coo[1] + i)

