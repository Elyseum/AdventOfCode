"""Puzzle 1."""

from itertools import cycle

def read_frequency_changes(file):
    """
    Reads lines of file and returns the frequency changes as integers.

    Examples
    --------
    String "+5" is returned as int 5.
    String "-5" is returend as int -5.

    """
    with open(file) as input_file:
        for line in input_file.readlines():
            yield int(line) # int("+5") == 5, int("-5") == -5

CHANGES = list(read_frequency_changes("01.TXT"))

def change_frequency(changes, frequency=0):
    return sum(CHANGES, 0)

print(f"Puzzle 1 (part 1): {change_frequency(CHANGES)}")

def repeated_frequency(changes, frequency=0):
    """Keeps changing frequency until a value is repeated."""
    frequencies = set()
    frequencies.add(frequency)
    for change in cycle(changes):
        frequency += change
        if frequency in frequencies:
            return frequency
        else:
            frequencies.add(frequency)

print(f"Puzzle 1 (part 2 - test 1): {repeated_frequency([-1, 1])}")
print(f"Puzzle 1 (part 2 - test 2): {repeated_frequency([+3, +3, +4, -2, -4])}")
print(f"Puzzle 1 (part 2): {repeated_frequency(CHANGES)}")
