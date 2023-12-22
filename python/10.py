from santas_little_helpers.helpers import *
from collections import deque
import re


input_data = read_input(10)


NORTH = 0-1j
SOUTH = 0+1j
EAST = 1+0j
WEST = -1+0j

DIRECTIONS = {
    '-': (EAST, WEST), # east- west
    '|': (NORTH, SOUTH),  # north-south
    'L': (NORTH, EAST),
    'J': (NORTH, WEST),
    '7': (SOUTH, WEST),
    'F': (SOUTH, EAST),

}

pipes = {}

for y, line in enumerate(input_data):
    for x, c in enumerate(line):
        if c != '.' and c != 'S':
            pipes[complex(x, y)] = DIRECTIONS[c]
        elif c == 'S':
            START = complex(x, y)
            pipes[START] = (WEST, SOUTH)


MATCHES = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    EAST: WEST,
    WEST: EAST,
}



def get_neighbors(location, heightmap):
    return {candidate for delta in pipes[location]
            if (candidate:=location + delta) in heightmap}


def get_path_length(came_from, start, end):
    current = end
    path = []
    while current != start:
        if current not in came_from:
            return
        path.append(current)
        current = came_from[current]
    return len(path)

def is_angle(coord):
    angles = 'LJF7'
    return any(pipes[coord] == DIRECTIONS[angle] for angle in angles)

def shortest_path(heightmap, start=None):
    frontier = deque([start])
    came_from = {start: None}
    while frontier:
        current = frontier.popleft()

        if current == start and len(came_from) >1 : # full loop
                return get_path_length(came_from, start, start)

        for neighbor in get_neighbors(current, heightmap):
            if neighbor not in came_from:
                frontier.append(neighbor)
                came_from[neighbor] = current
            # if neighbor == START:
            #     frontier.append(neighbor)
            #     came_from[neighbor] = current
    print(len(came_from)//2) #party_1
    return set(came_from)


#print(shortest_path(pipes, start = START))

loop = shortest_path(pipes, start = START)

clean_map = [[c for c in line] for line in input_data]
for y, line in enumerate(input_data):
    for x, c in enumerate(line):
        if complex(x, y) not in loop:
            clean_map[y][x] = '.'
        if c =='S':
            clean_map[y][x] = '7' # this is manual depending on the example
party_2 = 0
for n, line in enumerate(clean_map):
    
    cline = ''.join(c for c in line)
    matches = re.finditer(r'L-*J|L-*7|F-*J|F-*7|\|', cline)
    areas = re.finditer(r'\.+', cline)
    spans_to_check = []
    for a in areas:
        spans_to_check.append(a.span())


    out = True
    last_right = -1
    for match in matches:
        conf = match.group()
        left, right = match.span()
        diff = left - last_right - 1
        

        if not out:
            #print(f'line number {n}, {left}, {last_right}')
            party_2 += diff
        last_right = right-1
        if not(('L' in conf and 'J' in conf) or ('F' in conf and '7' in conf)):
            out = not out


print(party_2)