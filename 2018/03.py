"""Puzzle 3."""

import re
import time
from collections import Counter

class Claim:

    def __init__(self, input_str):
        """ Expected input string: "#123 @ 3,2: 5x4""" 
        parts = re.search(r"(#\d+)\s@\s(\d+),(\d+): (\d+)x(\d+)", input_str)
        self.id = parts[1]
        self.top = (int(parts[2]), int(parts[3]))
        self.size = (int(parts[4]), int(parts[5]))

    def __str__(self):
        return f"id: '{self.id}', top: '{self.top}', size: '{self.size}'"

    def surface_coordinates(self):
        """Coordinates from left to right from top to bottom."""
        for height in range(self.size[1]):
            for width in range(self.size[0]):
                yield (self.top[0] + width, self.top[1] + height)

def read_claims(file):
    with open(file) as input_file:
        for line in input_file.readlines():
            yield Claim(line)

EXAMPLE_CLAIM = Claim("#123 @ 3,2: 5x4")
print(f"Example claim: {EXAMPLE_CLAIM}")
EXAMPLE_CLAIM_SURFACE = list(EXAMPLE_CLAIM.surface_coordinates())
print(f"Example claim surface: {EXAMPLE_CLAIM_SURFACE}")

CLAIMS = list(read_claims("03.txt"))

def overlapping_surfaces(claims):
    counter = Counter()
    for claim in claims:
        counter.update(claim.surface_coordinates())
    return [value for value in counter.values() if value > 1]

def puzzle3_1():
    start = time.time()
    overlap = len(overlapping_surfaces(CLAIMS))
    elapsed = time.time() - start
    print(f"Puzzle 3 (part 1): {overlap} (duration {elapsed}s)")

puzzle3_1()

def claim_without_overlap(claims):
    claims_per_coordinate = dict()
    has_overlap = set()
    for claim in claims:
        for coordinate in claim.surface_coordinates():
            if coordinate in claims_per_coordinate:
                claims_for_coordinate = claims_per_coordinate[coordinate]
                claims_for_coordinate.add(claim.id)
                has_overlap.update(claims_for_coordinate)
            else:
                claims_per_coordinate[coordinate] = set([claim.id])
    return next(claim.id for claim in claims if claim.id not in has_overlap)

def puzzle3_2():
    start = time.time()
    no_overlap = claim_without_overlap(CLAIMS)
    elapsed = time.time() - start
    print(f"Puzzle 3 (part 2): {no_overlap} (duration {elapsed}s)")

puzzle3_2()