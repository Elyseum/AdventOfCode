import re
import util

from collections import defaultdict

def parse(path):
    chunks = list(util.chunk(lambda x: len(x) == 0, util.read_lines(path)))
    seeds = [int(x.strip()) for x in chunks[0][0].split(': ')[1].split(' ')]
    mappings = {}
    for chunk in chunks[1:]:
        mapping_name = chunk[0].replace(' map:', '')
        mapping_entries = list(parse_mappings(chunk[1:]))
        mappings[mapping_name] = mapping_entries
    return seeds, mappings

def parse_mappings(mappings):
    for mapping in mappings:
        yield [int(x.strip()) for x in mapping.split(' ')]

def map_source_to_destination(mapping_entries, source):
    for mapping_entry in mapping_entries:
        destination_range_start = mapping_entry[0]
        source_range_start = mapping_entry[1]
        range_length = mapping_entry[2]
        source_range_end = source_range_start + range_length - 1
        if source_range_start <= source and source <= source_range_end:
            delta = source - source_range_start
            return destination_range_start + delta
    # When no mapping is found, the destination is equal to the source.
    return source

location_map = {}

def derive_seed_to_location(mappings, seed):
    seed_key = 'seed_' + str(seed)
    if seed_key in location_map:
        return location_map[seed_key]

    soil = map_source_to_destination(mappings['seed-to-soil'], seed)
    soil_key = 'soil_' + str(soil)
    if soil_key in location_map:
        return location_map[soil_key]

    fertilizer = map_source_to_destination(mappings['soil-to-fertilizer'], soil)
    fert_key = 'fert_' + str(fertilizer)
    if fert_key in location_map:
        return location_map[fert_key]

    water = map_source_to_destination(mappings['fertilizer-to-water'], fertilizer)
    wate_key = 'wate_' + str(water)
    if wate_key in location_map:
        return location_map[wate_key]

    light = map_source_to_destination(mappings['water-to-light'], water)
    ligh_key = 'ligh_' + str(light)
    if ligh_key in location_map:
        return location_map[ligh_key]

    temperature = map_source_to_destination(mappings['light-to-temperature'], light)
    temp_key = 'temp_' + str(temperature)
    if temp_key in location_map:
        return location_map[temp_key]

    humidity = map_source_to_destination(mappings['temperature-to-humidity'], temperature)
    humi_key = 'humi_' + str(humidity)
    if humi_key in location_map:
        return location_map[humi_key]

    location = map_source_to_destination(mappings['humidity-to-location'], humidity)

    location_map[seed_key] = location
    location_map[soil_key] = location
    location_map[fert_key] = location
    location_map[wate_key] = location
    location_map[ligh_key] = location
    location_map[temp_key] = location
    location_map[humi_key] = location

    return location

def derive(input):
    seeds = input[0]
    mappings = input[1]
    return min(map(lambda x: derive_seed_to_location(mappings, x), seeds))

def solve_1(part, path):
    util.solve(part, path, parse, derive)

def seeds_from_ranges(seeds_ranges):
    i = 0
    while i < len(seeds_ranges):
        start = seeds_ranges[i]
        range_length = seeds_ranges[i+1]
        for j in range(range_length):
            yield start + j
        i += 2

def derive_range(input):
    seeds = seeds_from_ranges(input[0])
    mappings = input[1]
    return min(map(lambda x: derive_seed_to_location(mappings, x), seeds))

def solve_2(part, path):
    util.solve(part, path, parse, derive_range)

location_map = {}
solve_1("Part 1", 'data/05_example.txt')

location_map = {}
solve_1("Part 1", 'data/05_input.txt')

location_map = {}
solve_2("Part 2", 'data/05_example.txt')

location_map = {}
solve_2("Part 2", 'data/05_input.txt')

