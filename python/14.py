from santas_little_helpers.helpers import *
from collections import defaultdict

input_data = read_input(14)

rocks = {complex(x,y) for y, row in enumerate(input_data, start=1) for x, symbol in enumerate(row, start=1) if symbol == '#'}
round_rocks = {complex(x,y) for y, row in enumerate(input_data, start=1) for x, symbol in enumerate(row, start=1) if symbol == 'O'}
available = {complex(x,y) for y, row in enumerate(input_data, start=1) for x, symbol in enumerate(row, start=1) if symbol != '#'}

SOUTH_BORDER = max(point.imag for point in available) + 1
EAST_BORDER = max(point.real for point in available) + 1


def is_north_border(point):
    return point.imag == 0

def is_south_border(point):
    return point.imag == SOUTH_BORDER

def is_west_border(point):
    return point.real == 0

def is_east_border(point):
    return point.real == EAST_BORDER

def distance_from_south_border(point):
    return SOUTH_BORDER - point.imag

DIRECTIONS = {
    'north': 0-1j,
    'south': 0+1j,
    'west': -1+0j,
    'east:': 1+0j,
}

border_condition = {
    'north': is_north_border,
    'south': is_south_border,
    'west':  is_west_border,
    'east:': is_east_border,
}

def roll_the_rock(rock, direction='north'):
    while True:
        if border_condition[direction]((next_position := rock + DIRECTIONS[direction])) or next_position in rocks:
            return rock
        rock = next_position

def calculate_force(rocks):
    total_force = 0
    rock_position_counter = defaultdict(int)
    for rock in round_rocks:
        rock_position_counter[roll_the_rock(rock)] += 1
    for position, amount in rock_position_counter.items():
        exact_positions = (complex(position.real, (position.imag+d)) for d in range(amount))
        total_force += sum(distance_from_south_border(position) for position in exact_positions)
    return int(total_force)


party_1 = calculate_force(round_rocks)
print_solutions(party_1)

def test_one():
    assert party_1 == 108792
