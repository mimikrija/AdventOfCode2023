from santas_little_helpers.helpers import *
import re
from math import inf

numbers = re.compile(r'\d+')

input_data = read_input(5, separator='\n\n')

seeds = list(map(int, re.findall(numbers, input_data[0])))

mappings = list()

for chunk in input_data[1:]:
    chunk = chunk.split('\n')
    category = chunk[0][:-1]
    values = [list(map(int, re.findall(numbers, line))) for line in chunk[1:]]
    mappings.append(values)


# destination range | source range | range length

def get_seed_ranges(seed, mapping):
    for dest, source, length in mapping:
        delta = seed - source
        soil = dest + delta
        if delta >= 0 and dest <= soil < dest + length:
            return soil
    return seed

seed_ranges = [(first, first+len) for first, len in zip(seeds[::2], seeds[1::2])]


for mapping in mappings:
    new_seeds = [get_seed_ranges(s, mapping) for s in seeds]
    seeds = new_seeds

party_1 = min(seeds)

print_solutions(party_1)

def test_one():
    assert party_1 == 313045984

# ---- part 2


def all_in(me, you):
    ''' checks if me is completely within you (inclusive borders) '''
    me_left, me_right = me
    you_left, you_right = you
    return you_left <= me_left < me_right <= you_right

def no_overlap(me, you):
    me_left, me_right = me
    you_left, you_right = you
    return me_right < you_left or me_left > you_right

def intersect(me, you):
    ''' creates a new range by intersecting two ranges '''
    me_left, me_right = me
    you_left, you_right = you
    if no_overlap(me, you):
        return
    if all_in(me, you):
        return me
    if all_in(you, me):
        return you
    return (max(me_left, you_left), min(me_right, you_right))

def reduce_dest(source, destination, intersection):
    left = intersection[0] - source[0]
    right = source[1] - intersection[1]
    return (destination[0]+left, destination[1]-right)

def generate_mapping_ranges(mapping):
    # first sort the ranges based on source
    mapping = sorted(mapping, key=lambda x: x[1])
    holes = []
    sorted_ranges = []
    hole_left = mapping[0][1]
    hole_right = mapping[-1][1]+mapping[-1][-1]
    # then check if there are any holes:
    for (dl, _, l), (Dl, _, _) in zip(mapping, mapping[1:]):
        dest_right = dl + l
        if dest_right < Dl:
            holes.append((dest_right, Dl-1))
        # i also need to add infinity to holes :/

    for dl, sl, l in mapping:
        sorted_ranges.append(((sl, sl+l), (dl, dl+l)))
    
    if hole_left != 0:
        holes.append((0, hole_left))
    holes.append((hole_right, inf))
    return (sorted_ranges, holes)


sorted_ranges = [generate_mapping_ranges(mapping) for mapping in mappings]

# source, destination, holes

def generate_whatever(our_range, sorted_range):
    source_destination_ranges = sorted_range[0]
    holes = sorted_range[1]
    final_destination_ranges = []
    for source, dest in source_destination_ranges:
        intersection = intersect(our_range, source)
        if intersection:
            final_destination_ranges.append(reduce_dest(source, dest, intersection))
    for h in holes:
        intersection = intersect(our_range, h)
        if intersection:
            final_destination_ranges.append(reduce_dest(source, source, intersection))
    return final_destination_ranges



for s in seed_ranges:
    new_seeds = [s]
    for sorted_range in sorted_ranges:
        new_seeds = set([c for new_seed in new_seeds for c in generate_whatever(new_seed, sorted_range)])
    party_2 = min(c[0] for c in new_seeds)


print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 313045984

def test_two():
    assert party_2 == 20283860
