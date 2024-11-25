import util

"""
"""
def parse_input(data_path):
    lines = util.read_lines(data_path)
    return (map(lambda l: l.split(' '), lines))

SCORES = { 'X': 1, 'Y': 2, 'Z': 3 }

"""
Plays a round and returns the score.
"""
def play_round(round):
    p1 = round[0]
    p2 = round[1]
    p1_r = p1 == 'A'
    p1_p = p1 == 'B'
    p1_s = p1 == 'C'
    p2_r = p2 == 'X'
    p2_p = p2 == 'Y'
    p2_s = p2 == 'Z'
    draw = (p1_r and p2_r) or (p1_p and p2_p) or (p1_s and p2_s)
    if draw:
        return SCORES[p2] + 3
    p2_wins = (p2_r and p1_s) or (p2_p and p1_r) or (p2_s and p1_p)
    if p2_wins:
        return SCORES[p2] + 6
    else:
        return SCORES[p2] + 0


def play_round_predict(round):
    p1 = round[0]
    p2 = round[1]
    p1_r = p1 == 'A'
    p1_p = p1 == 'B'
    p1_s = p1 == 'C'
    p2_l = p2 == 'X'
    if p2_l: # Expect to lose
        if p1_r:
            return SCORES['Z'] + 0
        elif p1_p:
            return SCORES['X'] + 0
        else:
            return SCORES['Y'] + 0
    p2_d = p2 == 'Y'
    if p2_d: # Expect to draw
        if p1_r:
            return SCORES['X'] + 3
        elif p1_p:
            return SCORES['Y'] + 3
        else:
            return SCORES['Z'] + 3
    else: # Expect to win
        if p1_r:
            return SCORES['Y'] + 6
        elif p1_p:
            return SCORES['Z'] + 6
        else:
            return SCORES['X'] + 6

def play(rounds):
    return sum(map(play_round, rounds))

def play_predict(rounds):
    return sum(map(play_round_predict, rounds))

def solve_1(part, data_path):
    util.solve(part, data_path, parse_input, play)

def solve_2(part, data_path):
    util.solve(part, data_path, parse_input, play_predict)

solve_1("Part 1", 'data/02_example.txt')
solve_1("Part 1", 'data/02_input.txt')

solve_2("Part 2", 'data/02_example.txt')
solve_2("Part 2", 'data/02_input.txt')

