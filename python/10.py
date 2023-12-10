from santas_little_helpers.helpers import *
from collections import deque


input_data = read_input(10)
input_data = get_input('inputs/09e.txt')

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
                print(came_from)
                print('hello')
                return get_path_length(came_from, start, start)

        for neighbor in get_neighbors(current, heightmap):
            if neighbor not in came_from:
                frontier.append(neighbor)
                came_from[neighbor] = current
            # if neighbor == START:
            #     frontier.append(neighbor)
            #     came_from[neighbor] = current
    print(len(came_from)//2)
    return set(came_from)


#print(shortest_path(pipes, start = START))

loop = shortest_path(pipes, start = START)
print (START in loop)
party_2 = 0
visited = set()
for y, line in enumerate(input_data):
    leftright = list()
    for tile in loop:
        if tile.imag == y and tile not in visited:
            leftright.append(tile.real)
            visited.add(tile)

    leftright = deque(sorted(leftright))
    #print(f'{y}: {leftright}')
    last = leftright.popleft()
    groups = [[last]]
    while leftright:
        current = leftright.popleft()
        if last+1 == current:
            groups[-1].append(current)
        else:
            groups.append([current])
        last = current
    area = 0
    l = 0
    for g1, g2 in zip(groups, groups[1:]):
        l += len(g1)
        l -= sum(is_angle(complex(x, y)) for x in g1)
        print(l)
        if l%2== 1:
            area += g2[0] - g1[-1] -1
    if area:
        print(y, area)
    party_2 += area
 



    #party_2 += sum(right-left-1 for left, right in zip(leftright[::2], leftright[1::2]))

print(party_2)