import math
import util

def split_range(min_max_val, instruction):
  min_val, max_val = min_max_val
  diff = (max_val - min_val) / 2
  if instruction is 'F' or instruction is 'L':
    return (min_val, max_val - math.floor(diff) - 1)
  else:
    return (min_val + math.ceil(diff), max_val)

def decode_seat(instructions):
  rows = (0, 127)
  row_instructions = instructions[:7]
  for instruction in row_instructions:
    rows = split_range(rows, instruction)
  cols = (0, 7)
  col_instructions = instructions[7:]
  for instruction in col_instructions:
    cols = split_range(cols, instruction)
  seat_row = rows[0]
  seat_col = cols[0]
  seat_id = seat_row*8 + seat_col
  return { 'row': seat_row, 'col': seat_col, 'seat ID': seat_id }

print(decode_seat('BFFFBBFRRR'))
print(decode_seat('FFFBBBFRRR'))
print(decode_seat('BBFFBBFRLL'))

puzzle_input = list(util.readlines('data/05.txt'))

part_1 = max(map(lambda x : decode_seat(x)['seat ID'], puzzle_input))
print(f'Puzzle 5: part 1 = {part_1}')

def find_my_seat(instructions):
  seats = map(decode_seat, instructions)
  taken = set(map(lambda x: (x['row'], x['col']), seats))
  # Mine is the first free seat with both neighbours taken.
  for row in range(0, 128):
    for col in range(0, 8):
      seat = (row, col)
      seat_p = (row, col-1)
      seat_n = (row, col+1)
      if seat not in taken and seat_p in taken and seat_n in taken:
        return row*8 + col

part_2 = find_my_seat(puzzle_input)
print(f'Puzzle 5: part 2 = {part_2}')
  
