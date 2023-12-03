from santas_little_helpers.helpers import *
import re
from math import prod


def get_neighbors(x, y):
    return {(xn, yn) for xn, yn in ((x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1))}


input_data = read_input(3)


motor_data = []
symbols = set()
gears = set()
for y, row in enumerate(input_data):
    for x, symbol in enumerate(row):
        if symbol != '.' and not symbol.isdigit():
            symbols.add((x,y))
        if symbol == '*':
            gears.add((x, y))
    for match in re.finditer(r'\d+', row):
        num = match.group()
        positions = range(*match.span())
        motor_data.append((int(num), {(p, y) for p in positions}))


party_1 = sum(num for num, coords in motor_data 
              if any(neighbor in symbols 
                     for neighbor in {n for (x, y) in coords for n in get_neighbors(x, y)}))


party_2 = 0
for gx, gy in gears:
    gear_neighbours = get_neighbors(gx, gy)
    adj = [num for num, coords in motor_data if any(c in gear_neighbours for c in coords)]
    if len(adj) == 2:
        party_2 += prod(adj)


print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 532331

def test_two():
    assert party_2 == 82301120
