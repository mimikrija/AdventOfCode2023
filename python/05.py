from santas_little_helpers.helpers import *
import re

numbers = re.compile(r'\d+')

input_data = read_input(5, separator='\n\n')
#input_data = get_input('inputs/05e.txt', separator='\n\n')

seeds = list(map(int, re.findall(numbers, input_data[0])))

info = {}

for chunk in input_data[1:]:
    chunk = chunk.split('\n')
    category = chunk[0][:-1]
    values = [list(map(int, re.findall(numbers, line))) for line in chunk[1:]]
    info[category] = values


# destination range | source range | range length

def get_seed_ranges(seed, mapping):
    for dest, source, length in mapping:
        delta = seed - source
        soil = dest + delta
        if delta > 0 and dest <= soil < dest + length:
            return soil
    return seed




for _, mapping in info.items():
    new_seeds = [get_seed_ranges(s, mapping) for s in seeds]
    seeds = new_seeds

party_1 = min(seeds)

print_solutions(party_1)

def test_one():
    assert party_1 == 313045984
