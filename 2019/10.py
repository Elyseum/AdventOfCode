import math
import IO

from collections import defaultdict

print(f"Solving Day {__file__.split('.')[0]}")
print()

###############################################################################
print("...Testing Part One...")

class Asteroid:

    MIN_DIR = -999999999
    MAX_DIR = +999999999

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self, x, y):
        return self.x == x and self.y == y

    def detect(self, asteroid):
        y_dir = self.y - asteroid.y
        x_dir = self.x - asteroid.x
        quarter = self.get_quarter(asteroid)
        # Dividing by zero should yield infinity, but we use max int instead.
        # Since Python 3 doesn't have a max int we invent one.
        if quarter == 1 or quarter == 4:
            direction = self.MIN_DIR if x_dir == 0 else + (y_dir / x_dir)
        else:
            direction = self.MAX_DIR if x_dir == 0 else - (y_dir / x_dir)
        return (quarter, direction)

    def get_quarter(self, asteroid):
        """Clockwise quarters"""
        if self.x <= asteroid.x and self.y > asteroid.y: return 1
        elif self.x <= asteroid.x and self.y <= asteroid.y: return 2
        elif self.x > asteroid.x and self.y <= asteroid.y: return 3
        else: return 4

    def get_distance(self, asteroid):
        x0 = self.x
        y0 = self.y
        x1 = asteroid.x
        y1 = asteroid.y
        return math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)

    def detectable_nr(self, asteroids):
        other = (x for x in asteroids if x != self)
        detections = map(self.detect, other)
        positions = map(lambda x: (x[0], x[1]), detections)
        return len(set(positions))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

def parse_asteroids(input):
    asteroids = []
    for (row, line) in enumerate(input):
        for (col, symbol) in enumerate(line):
            if symbol != '.': # Could be '#', 'X', ...
                asteroids.append(Asteroid(col, row))
    return asteroids

def best_asteroid(asteroids):
    return max(
        map(lambda x: (x, x.detectable_nr(asteroids)), asteroids),
        key=lambda x: x[1])

def vaporize_asteroids(asteroids):
    return 0

print("All tests passed!")
print()
###############################################################################

# Check if we can detect if astroids are in the same line of sight using rico
# detection: a1 and a2 are in the same line of sight from a0's point of view.
a0 = Asteroid(0, 0)
a1 = Asteroid(3, 1)
a2 = Asteroid(6, 2)
assert(a0.detect(a1)[0] == a0.detect(a2)[0]) # Different quarter
assert(a0.detect(a1)[1] == a0.detect(a2)[1]) # Same direction

# Special case: a0 is positioned between a1 and a2. All on the same
# horizontal line. They have the same rico, but both are detectable.
a0 = Asteroid(1, 0)
a1 = Asteroid(0, 0)
a2 = Asteroid(2, 0)
assert(a0.detect(a1)[0] != a0.detect(a2)[0]) # Different quarter
assert(a0.detect(a1)[1] == a0.detect(a2)[1]) # Same direction

print(best_asteroid(parse_asteroids([
    ".#..#",
    ".....",
    "#####",
    "....#",
    "...##"
])))

print(best_asteroid(parse_asteroids([
    "......#.#.",
    "#..#.#....",
    "..#######.",
    ".#.#.###..",
    ".#..#.....",
    "..#....#.#",
    "#..#....#.",
    ".##.#..###",
    "##...#..#.",
    ".#....####"
])))

print(best_asteroid(parse_asteroids([
    "#.#...#.#.",
    ".###....#.",
    ".#....#...",
    "##.#.#.#.#",
    "....#.#.#.",
    ".##..###.#",
    "..#...##..",
    "..##....##",
    "......#...",
    ".####.###."
])))

print(best_asteroid(parse_asteroids([
    ".#..#..###",
    "####.###.#",
    "....###.#.",
    "..###.##.#",
    "##.##.#.#.",
    "....###..#",
    "..#.#..#.#",
    "#..#.#.###",
    ".##...##.#",
    ".....#.#.."
])))

IO.log("Part 1: starting long example")
part_1_example = parse_asteroids([
    ".#..##.###...#######",
    "##.############..##.",
    ".#.######.########.#",
    ".###.#######.####.#.",
    "#####.##.#.##.###.##",
    "..#####..#.#########",
    "####################",
    "#.####....###.#.#.##",
    "##.#################",
    "#####.##.###..####..",
    "..######..##.#######",
    "####.##.####...##..#",
    ".#####..#.######.###",
    "##...#.##########...",
    "#.##########.#######",
    ".####.#.###.###.#.##",
    "....##.##.###..#####",
    ".#.#.###########.###",
    "#.#.#.#####.####.###",
    "###.##.####.##.#..##"
])
IO.log(best_asteroid(part_1_example))

###############################################################################
IO.log("...Solving Part One...")

part_1_asteroids = parse_asteroids(IO.read_lines("10.txt"))
IO.log(best_asteroid(part_1_asteroids))

print()
###############################################################################

def vaporize(asteroids, pos_x, pos_y):
    monitoring_st = next(filter(lambda x: x.position(pos_x, pos_y), asteroids))
    other_asteroids = [x for x in asteroids if x != monitoring_st]
    # Group asteroids by their direction as seen from the monitoring station.
    directed_asteroids = defaultdict(list)
    for asteroid in other_asteroids:
        quarter, direction = monitoring_st.detect(asteroid)
        directed_asteroids[(quarter, direction)].append(asteroid)
    # Sort the groups by distance to the monitoring station, shortes first.
    for value in directed_asteroids.values():
        value.sort(key=monitoring_st.get_distance)
    # Vaporize!
    vape_count = 1
    while len(directed_asteroids) > 0:
        for direction in sorted(directed_asteroids.keys()):
            vaped = directed_asteroids[direction].pop(0)
            # print(f"Count: {vape_count}, Vaporized: {vaped}, Direction: {direction}")
            yield (vape_count, vaped)
            if len(directed_asteroids[direction]) == 0:
                directed_asteroids.pop(direction)
            vape_count += 1

###############################################################################
print("...Testing Part Two...")

part_2_example_vaporized = vaporize(part_1_example, 11, 13)
part_2_example_index = [1, 2, 3, 10, 20, 50, 100, 199, 200, 201, 299]
for (count, asteroid) in part_2_example_vaporized:
    if count in part_2_example_index:
        print(f"The {count} asteroid to be vaporized is {asteroid}")

print("All tests passed!")
print()
###############################################################################

###############################################################################
print("Solving Part Two...")

part_2_asteroid = next(x[1] for x in vaporize(part_1_asteroids, 23, 20) if x[0] == 200)
print(part_2_asteroid)

###############################################################################
