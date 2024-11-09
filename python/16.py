from santas_little_helpers.helpers import *
from collections import deque


input_data = read_input(16)


mirror_map = {complex(x,y): symbol 
              for y, row in enumerate(input_data, start=1)
              for x, symbol in enumerate(row, start=1)}

is_horizontal = lambda x:  DIRECTIONS['left'] == x or DIRECTIONS['right'] == x
is_vertical = lambda x:  DIRECTIONS['up'] == x or DIRECTIONS['down'] == x

def reflected(direction, mirror_type):
    if mirror_type == '.':
        return [direction]

    if mirror_type == '-':
        if is_horizontal(direction):
            return [direction]
        else:
            return [DIRECTIONS['left'], DIRECTIONS['right']]
    
    if mirror_type == '|':
        if is_vertical(direction):
            return [direction]
        else:
            return [DIRECTIONS['up'], DIRECTIONS['down']]
    
    if mirror_type == '/':
            if is_horizontal(direction):
                return [direction * (0-1j)]
            else:
                return [direction * (0+1j)]
    
    if mirror_type == '\\':
            if is_horizontal(direction):
                return [direction * (0+1j)]
            else:
                return [direction * (0-1j)]

DIRECTIONS = {
    'up': 0-1j,
    'down': 0+1j,
    'left': -1+0j,
    'right': 1+0j,
}


def draw_laser_beams(mirror_map, start, start_direction):
    energized_fields = set()
    to_solve = deque([(start, DIRECTIONS[start_direction])])
    while to_solve:
        current, direction = to_solve.popleft()
        current += direction
        if current not in mirror_map or (current, direction) in energized_fields:
            continue
        else:
            energized_fields.add((current, direction))
            type = mirror_map[current]
            directions = reflected(direction, type)
            for d in directions:
                to_solve.append((current, d))

    return len(set(c[0] for c in energized_fields))

def find_best(mirror_map):
    best_result = 0
    max_column = max(mirror_map.keys(), key=lambda x: x.real)
    max_row = max(mirror_map.keys(), key=lambda x: x.imag)
    left_columns = (c - 1 for c in mirror_map.keys() if c.real == 1)
    right_columns = (c + 1 for c in mirror_map.keys() if c.real == max_column)
    top_rows = (c - 1j for c in mirror_map.keys() if c.imag == 1)
    bottom_rows = (c + 1j for c in mirror_map.keys() if c.imag == max_row)

    for start_position in left_columns:
        best_result = max(best_result, draw_laser_beams(mirror_map, start_position, 'right'))

    for start_position in right_columns:
        best_result = max(best_result, draw_laser_beams(mirror_map, start_position, 'left'))

    for start_position in top_rows:
        best_result = max(best_result, draw_laser_beams(mirror_map, start_position, 'down'))

    for start_position in bottom_rows:
        best_result = max(best_result, draw_laser_beams(mirror_map, start_position, 'up'))

    return best_result

party_1 = draw_laser_beams(mirror_map, 0+1j, 'right')

party_2 = find_best(mirror_map)

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 7860

def test_two():
    assert party_1 == 8331
