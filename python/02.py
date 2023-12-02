from santas_little_helpers.helpers import *
import re
from math import prod


input_data = read_input(2)

dice_data = [(n, re.compile(rf'(\d+) ({color})')) for n, color in enumerate(('red', 'green', 'blue'), start=12)]


party_1 = sum(n for n, line in enumerate(input_data, start=1)
                  if all(not any(int(c[0]) > max_dice for c in re.findall(pattern, line))
                         for max_dice, pattern in dice_data))

party_2 = sum(prod(max(int(c[0]) for c in re.findall(pattern, line))
                   for _, pattern in dice_data) 
                   for line in input_data)


print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 2156

def test_two():
    assert party_2 == 66909

