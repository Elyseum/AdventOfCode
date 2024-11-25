import util
from collections import defaultdict

"""
Each tree knows its own height and the row and col its part of.
Row and col are lists with references to the trees (including this one) in it.
"""
class Tree:
    def __init__(self, height):
        self.height = height

    def height(self):
        return self.height

    def set_row(self, row):
        self.row = row

    def set_col(self, col):
        self.col = col

    def split(self, lst):
        index_self = lst.index(self)
        return (reversed(lst[:index_self]), lst[index_self+1:])

    def count_visible_self(self, trees):
        count = 0
        for tree in trees:
            count += 1
            if tree.height >= self.height:
                break
        return count

    def scenic_score(self):
        left, right = map(self.count_visible_self, self.split(self.row))
        up, down = map(self.count_visible_self, self.split(self.col))
        return left * right * up * down


def parse(path):
    trees = []
    rows = []
    for row in list(util.read_lines(path)):
        row_trees = [Tree(int(x)) for x in row]
        rows.append(row_trees)
        for tree in row_trees:
            tree.set_row(row_trees)
            trees.append(tree)
    cols = []
    for col_index in range(len(rows[0])):
        col_trees = [row[col_index] for row in rows]
        cols.append(col_trees)
        for tree in col_trees:
            tree.set_col(col_trees)
    return (rows, cols, trees)

def get_visible(trees):
    prev = -1
    for tree in trees:
        height = tree.height
        if height > prev:
            prev = height
            yield tree

def count_visible_outside(rows, cols, _):
    visible = set()
    for row in rows:
        visible.update(get_visible(row))
        visible.update(get_visible(reversed(row)))
    for col in cols:
        visible.update(get_visible(col))
        visible.update(get_visible(reversed(col)))
    return len(visible)

def max_scenic_score(rows, cols, trees):
    return max(map(lambda x: x.scenic_score(), trees))

def solve_1(part, path):
    util.solve(part, path, parse, lambda x: count_visible_outside(*x))

def solve_2(part, data):
    util.solve(part, data, parse, lambda x: max_scenic_score(*x))

solve_1("Part 1", 'data/08_example.txt')
solve_1("Part 1", 'data/08_input.txt')

solve_2("Part 2", 'data/08_example.txt')
solve_2("Part 2", 'data/08_input.txt')

