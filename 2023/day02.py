import math
import util

COLORS = ['red', 'green', 'blue']

def parse(path):
    lines = util.read_lines(path)
    return map(parse_game, lines)

def parse_game(line):
    parts = line.split(': ')
    return {
        'id': int(parts[0].split(' ')[1]),
        'sets': list(map(parse_set, parts[1].split('; ')))
    }

def parse_set(set_s):
    game_set = {}
    for draw_s in set_s.split(', '):
        draw_s_parts = draw_s.split(' ')
        draw_color = draw_s_parts[1]
        draw_count = int(draw_s_parts[0])
        game_set[draw_color] = draw_count
    for color in COLORS:
        if color not in game_set:
            game_set[color] = 0
    return game_set

def possible(bag, game):
    game_id = game['id']
    game_sets = game['sets']
    for game_set in game_sets:
        for color in COLORS:
            if game_set[color] > bag[color]:
                return 0
    return game_id

def count_possible_games(bag, games):
    return sum(map(lambda game: possible(bag, game), games))

def solve_1(part, path):
    bag = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    util.solve(part, path, parse, lambda x: count_possible_games(bag, x))

def power_min_colors(game):
    min_colors = map(lambda x: max(game_set[x] for game_set in game['sets']), COLORS)
    return math.prod(min_colors)

def solve_2(part, path):
    util.solve(part, path, parse, lambda game: sum(map(power_min_colors, game)))

solve_1("Part 1", 'data/02_example.txt')
solve_1("Part 1", 'data/02_input.txt')

solve_2("Part 2", 'data/02_example.txt')
solve_2("Part 2", 'data/02_input.txt')

