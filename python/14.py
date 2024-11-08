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
    'east': 1+0j,
}

border_condition = {
    'north': is_north_border,
    'south': is_south_border,
    'west':  is_west_border,
    'east': is_east_border,
}

def roll_the_rock(rock, direction='north'):
    while True:
        if border_condition[direction]((next_position := rock + DIRECTIONS[direction])) or next_position in rocks:
            return rock
        rock = next_position

def position_the_rocks_correctly(round_rocks, direction='north'):
    exact_positions = []
    rock_position_counter = defaultdict(int)
    for rock in round_rocks:
        rock_position_counter[roll_the_rock(rock, direction)] += 1
    for position, amount in rock_position_counter.items():
        exact_positions += [position - d*DIRECTIONS[direction] for d in range(amount)]
    return exact_positions

def calculate_force(exact_positions):
    total_force = sum(distance_from_south_border(position) for position in exact_positions)
    return int(total_force)

def one_cycle(rounded_rock_positions):
    for direction in ['north', 'west', 'south', 'east']:
        rounded_rock_positions = position_the_rocks_correctly(rounded_rock_positions, direction)
    return rounded_rock_positions


def a_lot_of_cycles(round_rocks, a_lot=1000000000):
    pattern = defaultdict(list)
    rounded_rocks_after_centrifuge = frozenset(round_rocks)
    cycle = 1
    while True:
        if pattern and any(len(cycles) > 1 for cycles in pattern.values()):
            more_than_one = [cycle for cycles in pattern.values() for cycle in cycles if len(cycles) == 2]
            first_repeating, next_repeating = more_than_one
            period = next_repeating - first_repeating
            solution_cycle = first_repeating + (a_lot - first_repeating)%period
            break

        rounded_rocks_after_centrifuge = frozenset(one_cycle(rounded_rocks_after_centrifuge))
        pattern[rounded_rocks_after_centrifuge].append(cycle)
        cycle += 1
        
    for rocks, cycles in pattern.items():
        if solution_cycle in cycles:
            return calculate_force(rocks)


round_rocks_north = position_the_rocks_correctly(round_rocks, 'north')
party_1 = calculate_force(round_rocks_north)
party_2 = a_lot_of_cycles(round_rocks)


print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 108792

def test_two():
    assert party_2 == 99118
