import re
import util

"""
A board is parsed from a list of lines.
Each line is a string of comma separated numbers.
Additonal whitespace is used to format the layout of the numbers.
"""
def parse_board(lines):
    return Board([[int(n) for n in re.split('\s+', l.strip())] for l in lines])

"""
First line is numbers to draw: comma-separated list of numbers.
Second line is whitespace (and can be ignored).
Third line is the start of the first board.
Next boards are separated by an empty line.
"""
def parse_input(data_path):
    lines = list(util.read_lines(data_path)) 
    numbers = [int(x) for x in lines[0].split(',')]
    board_inputs = chunk(lambda x: len(x) == 0, lines[2:])
    boards = [parse_board(x) for x in board_inputs]
    return (numbers, boards)


class Board:

    """ 
    Create a board from a list of numbers.
    For example, [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
    """
    def __init__(self, lists_numbers):
        self.lists_numbers = lists_numbers
        self.rows = [set(x) for x in lists_numbers]
        self.cols = [set(x) for x in transpose(lists_numbers)]
        self.won = False

    """
    Registers drawn number and updates the board (if number is present).
    Returns True in case of bingo (full row or column).
    """
    def mark(self, number):
        for row in self.rows:
            row.discard(number)
            self.won |= len(row) == 0
        for col in self.cols:
            col.discard(number)
            self.won |= len(col) == 0
        return self.won

    def unmarked_numbers(self):   
        for row in self.rows:
            for el in row:
                yield el


def play_bingo(numbers, boards):
    for number in numbers:
        for board in boards:
            if board.mark(number):
                return sum(board.unmarked_numbers()) * number
    return -1

def lose_bingo(numbers, boards):
    for number in numbers:
        remaining_boards = [x for x in boards if not x.won]
        for board in remaining_boards:
            if board.mark(number) and len(remaining_boards) == 1:
                return sum(board.unmarked_numbers()) * number
    return -1


def solve_1(part, data_path):
    solve(part, data_path, parse_input, lambda x: play_bingo(x[0], x[1]))

def solve_2(part, data_path):
    solve(part, data_path, parse_input, lambda x: lose_bingo(x[0], x[1]))

solve_1("Part 1", 'data/04_example.txt')
solve_1("Part 1", 'data/04_input.txt')

solve_2("Part 2", 'data/04_example.txt')
solve_2("Part 2", 'data/04_input.txt')
