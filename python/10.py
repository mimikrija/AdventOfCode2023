from santas_little_helpers.helpers import *
from collections import deque
import re


input_data = read_input(10)


NORTH = 0-1j
SOUTH = 0+1j
EAST = 1+0j
WEST = -1+0j

DIRECTIONS = {
    '-': (EAST, WEST),
    '|': (NORTH, SOUTH),
    'L': (NORTH, EAST),
    'J': (NORTH, WEST),
    '7': (SOUTH, WEST),
    'F': (SOUTH, EAST),
}


MATCHES = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    EAST: WEST,
    WEST: EAST,
}


def get_neighbors(location, pipemap):
    return {candidate for delta in pipes[location]
            if (candidate:=location + delta) in pipemap}


def get_loop(pipemap, start=None):
    frontier = deque([start])
    visited = {start}
    while frontier:
        current = frontier.popleft()
        for neighbor in get_neighbors(current, pipemap):
            if neighbor not in visited:
                frontier.append(neighbor)
                visited.add(neighbor)
    return visited


pipes = {}

for y, line in enumerate(input_data):
    for x, c in enumerate(line):
        if c != '.' and c != 'S':
            pipes[complex(x, y)] = DIRECTIONS[c]
        elif c == 'S':
            START = complex(x, y)
            pipes[START] = (WEST, SOUTH) # this is manual depending on the example


loop = get_loop(pipes, start = START)
party_1 = len(loop)//2

# pt2:
party_2 = 0
for y, line in enumerate(input_data):
    cline = ''
    for x, c in enumerate(line):
        if complex(x, y) not in loop:
            cline += '.'
        elif c =='S':
        # this is manual depending on the example
            cline += '7'
        else:
            cline += c

    matches = re.finditer(r'L-*J|L-*7|F-*J|F-*7|\|', cline)
    is_in = False
    previous_right = -1
    for match in matches:
        pipe_conf = match.group()
        left, right = match.span()
        area_between_pipes = left - previous_right - 1

        if is_in:
            party_2 += area_between_pipes
        previous_right = right-1
        # LJ and F7 combos do not change the in/out status
        # so switch it only if we hit the other kind (hence not)
        is_in ^= not(any(all(c in pipe_conf for c in ins) for ins in ('LJ','F7')))



print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 6864

def test_two():
    assert party_2 == 349
