from santas_little_helpers.helpers import *
from collections import deque


input_data = read_input(16)


mirror_map = {complex(x,y): symbol for y, row in enumerate(input_data, start=1) for x, symbol in enumerate(row, start=1)}

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

GETDIRECTION = {v: k for k, v in DIRECTIONS.items()}

def draw_laser_beams(mirror_map, start, start_direction):
    energized_fields = [(start, start_direction)]
    to_solve = deque([(start, DIRECTIONS[start_direction])])
    count = 0
    while to_solve:
        count += 1
        current, direction = to_solve.popleft()
        current += direction
        if current not in mirror_map or (current, direction) in energized_fields:
            continue
        else:
            energized_fields.append((current, direction))
            type = mirror_map[current]
            direction = reflected(direction, type)
            for d in direction:
                to_solve.append((current, d))

    return energized_fields


party_1 = len(set((c[0] for c in draw_laser_beams(mirror_map, 1+1j, 'down'))))

print_solutions(party_1)

def test_one():
    assert party_1 == 7860
