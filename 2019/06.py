import math
import IO

print(f"Solving Day {__file__.split('.')[0]}")
print()

def parse_orbits(input):
    parts = input.split(')')
    return (parts[1], parts[0])

def get_direct_indirect_orbits(orbits):
    """Maps each object to its direct and indirect orbitting objects."""
    direct_orbits = {}
    for (x, y) in orbits:
        direct_orbits[x] = y
    # setup with direct orbits
    orbits_per_node = {}
    for (x, y) in orbits:
        orbits_per_node[x] = list([y])
    # add indirect orbits
    for (obj, _) in orbits:
        # for each object we chase the the indirect orbits,
        # starting from the direct orbit.
        current = direct_orbits[obj]
        while True:
            if current not in direct_orbits: # Can chase?
                break
            next = direct_orbits[current]
            if next in orbits_per_node[obj]: # Already chased?
                break
            orbits_per_node[obj].append(next)
            current = next
    return orbits_per_node

def count_direct_indirect_orbits(orbits):
    direct_indirect_orbits = get_direct_indirect_orbits(orbits)
    count_per_object = map(len, direct_indirect_orbits.values())
    return sum(count_per_object)

###############################################################################
print("...Testing Part One...")

assert(parse_orbits("COM)B") == ("B", "COM"))

example_part_1 = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L"
]
example_part_1_orbits = list(map(parse_orbits, example_part_1))
print(count_direct_indirect_orbits(example_part_1_orbits))

print("All tests passed!")
print()
###############################################################################

###############################################################################
print("...Solving Part One...")

part_1_orbits = list(IO.read_lines("06.txt", parse_orbits))
print(count_direct_indirect_orbits(part_1_orbits))

print()
###############################################################################

def first_intersection(list_1, list_2):
    """
    Returns the first element that is in both list,
    started by iterating list_1.
    When no intersection is found, an exception is raised.
    """
    for el in list_1:
        if el in list_2:
            return el
    raise Exception("No intersection")

def get_orbit_transfers(orbits, fr, to):
    orbits_di = get_direct_indirect_orbits(orbits)
    orbits_from = orbits_di[fr]
    orbits_to = orbits_di[to]
    intersection = first_intersection(orbits_from, orbits_to)
    orbits_shared_from = orbits_from[:orbits_from.index(intersection)]
    orbits_shared_to = orbits_to[:orbits_to.index(intersection)]
    return len(orbits_shared_from) + len(orbits_shared_to)

###############################################################################
print("...Testing Part Two...")

example_part_2 = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L",
    "K)YOU",
    "I)SAN"
]

example_part_2_orbits = list(map(parse_orbits, example_part_2))
print(get_orbit_transfers(example_part_2_orbits, 'YOU', 'SAN'))

print("All tests passed!")
print()
###############################################################################

###############################################################################
IO.log("Solving Part Two...")
orbit_transfers = get_orbit_transfers(part_1_orbits, 'YOU', 'SAN')
IO.log(f"Orbit transfers: {orbit_transfers}")

###############################################################################
