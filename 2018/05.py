"""Puzzle 05."""

import time

def read_polymer(file_name):
    with open(file_name) as file:
        return file.readline()

def react(unit1, unit2):
    # return unit1.upper() == unit2 or unit1 == unit2.upper()
    return unit1.swapcase() == unit2 or unit1 == unit2.swapcase()

print(f"'a' and 'A' react? {react('a', 'A')}")
print(f"'A' and 'a' react? {react('A', 'a')}")
print(f"'a' and 'a' react? {react('a', 'a')}")

def resolve(polymer, max_length=None, ignore1=None, ignore2=None):
    reacted = [] # stack
    for unit in polymer:
        if max_length and len(reacted) >= max_length:
            return None
        if ignore1 and unit == ignore1:
            continue
        if ignore2 and unit == ignore2:
            continue
        if len(reacted) > 0 and react(reacted[-1], unit):
            reacted.pop()
        else:
            reacted.append(unit)
    return ''.join(reacted)

print(f"Resolve('aA'): '{resolve('aA')}'")
print(f"Resolve('abBA'): '{resolve('abBA')}'")
print(f"Resolve('abAB'): '{resolve('abAB')}'")
print(f"Resolve('aabAAB'): '{resolve('aabAAB')}'")

EX = "dabAcCaCBAcCcaDA"
EX_RESOLVED = resolve(EX)
print(f"Resolve('{EX}'): '{EX_RESOLVED}' (length {len(EX_RESOLVED)})")

POLYMER = read_polymer("05.txt")
POLYMER_RESOLVED = resolve(POLYMER)
print(f"Puzzle 5 (part 1): {len(POLYMER_RESOLVED)}")

def clean(polymer, unit):
    return (x for x in polymer if x != unit and x != unit.swapcase())

def shortest(polymer):
    shortest_len = len(polymer)
    distinct_units = set((x.lower() for x in polymer))
    for unit in distinct_units:
        resolved = resolve(polymer, shortest_len, unit, unit.swapcase())
        if resolved and len(resolved) < shortest_len:
            shortest_len = len(resolved)
    return shortest_len

start = time.time()
SHORTEST_POLYMER_RESOLVED = shortest(POLYMER)
elapsed = time.time() - start
print(f"Puzzle 5 (part 1): {SHORTEST_POLYMER_RESOLVED} (in {elapsed}s)")
