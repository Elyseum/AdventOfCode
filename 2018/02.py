"""Puzzle 2."""

from collections import Counter

def read_box_ids(file):
    with open(file) as input_file:
        for line in input_file.readlines():
            yield line

def checksum_components(id):
    counts = Counter(id)
    return (2 in counts.values(), 3 in counts.values())

def checksum(ids):
    components = [checksum_components(id) for id in ids]
    component_two = len([x for x in components if x[0]])
    component_three = len([x for x in components if x[1]])
    return component_two * component_three

EXAMPLE = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
print(f"Checksum components for {EXAMPLE[0]} = {checksum_components(EXAMPLE[0])}")
print(f"Checksum components for {EXAMPLE[1]} = {checksum_components(EXAMPLE[1])}")
print(f"Checksum components for {EXAMPLE[2]} = {checksum_components(EXAMPLE[2])}")
print(f"Checksum components for {EXAMPLE[3]} = {checksum_components(EXAMPLE[3])}")
print(f"Checksum for example: {checksum(EXAMPLE)}")

BOX_IDS = list(read_box_ids("02.txt"))
print(f"Puzzle 2 (part 1): {checksum(BOX_IDS)}")

def different_by(nr_of_diffs, id1, id2):
    """
    True if id1 and id2 are different by given nr of diffs
    when comparing elements in the same position.

    Example
    -------
    "ABC" and "ABD" are different by 1 ("C" vs "D")
    "ABC" and "ADF" are different by 2 ("B" vs "D" and "C" vs "F")
    So different_by(1, "ABC", "ABD") is True, different_by(1, "ABC", "ADF") is False.
    """
    diffs = 0
    for i in range(len(id1)):
        if id1[i] != id2[i]:
            diffs += 1
        if diffs > nr_of_diffs:
            return False
    return diffs == nr_of_diffs

def common(id1, id2):
    result = ""
    for i in range(len(id1)):
        if id1[i] == id2[i]:
            result += id1[i]
    return result

print(f"Are 'abcde' and 'axcye' different by 1? {different_by(1, 'abcde', 'axcye')}")
print(f"Are 'fghij' and 'fguij' different by 1? {different_by(1, 'fghij', 'fguij')}")

def find_different_by(difference, ids):
    """Return elements that are different by given difference."""
    for i in range(len(ids) - 1):
        for j in range(i + 1, len(ids)):
            if different_by(difference, ids[i], ids[j]):
                yield (ids[i], ids[j])

EXAMPLE_IDS = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
print(f"First two ids that are different by 1: {next(find_different_by(1, EXAMPLE_IDS))}")

def common_first_two_diff_by_1(ids):
    first_diff = next(find_different_by(1, ids))
    return common(first_diff[0], first_diff[1])

print(f"Puzzle 2 (part 2): {common_first_two_diff_by_1(BOX_IDS)}")
