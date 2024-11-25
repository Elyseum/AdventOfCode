import re
import util

from collections import defaultdict

def parse(path):
    for line in util.read_lines(path):
        parts = [x.strip() for x in line.replace(':', '|').split('|')]
        game_id = int(parts[0].replace('Card ', ''))
        winning = [int(x.strip()) for x in parts[1].split(' ') if len(x) > 0]
        owned = [int(x.strip()) for x in parts[2].split(' ') if len(x) > 0]
        yield (game_id, winning, owned)

def score(winning, owned):
    matches = len(util.intersection(winning, owned))
    return pow(2, matches-1) if matches > 0 else 0

def scores(games):
    return sum(score(winning, owned) for (_, winning, owned) in games)

def solve_1(part, path):
    util.solve(part, path, parse, scores)

def scores_with_copies(games):
    total_score = 0
    games_count = defaultdict(lambda: 1)
    for (game_id, winning, owned) in games:
        matches = len(util.intersection(winning, owned))
        # The score of a game is original + nr of copies
        game_count = games_count[game_id]
        total_score += game_count
        # Hand out a copy for each match.
        for i in range(matches):
            copy = game_id + 1 + i
            games_count[copy] += (1 * game_count)
    return total_score

def solve_2(part, path):
    util.solve(part, path, parse, scores_with_copies)

solve_1("Part 1", 'data/04_example.txt')
solve_1("Part 1", 'data/04_input.txt')

solve_2("Part 2", 'data/04_example.txt')
solve_2("Part 2", 'data/04_input.txt')

