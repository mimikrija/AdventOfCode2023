from santas_little_helpers.helpers import *
from math import inf
from queue import PriorityQueue

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


input_data = read_input(17)
heat_map = {complex(x,y): int(symbol) 
              for y, row in enumerate(input_data, start=1)
              for x, symbol in enumerate(row, start=1)}

MAX_COLUMN = max(c.real for c in heat_map.keys())
MAX_ROW = max(c.imag for c in heat_map.keys())

DIRECTIONS = {
    'up': 0-1j,
    'down': 0+1j,
    'left': -1+0j,
    'right': 1+0j,
}

more_than_three = lambda path: len(set(c.real for c in path)) == 1 or len(set(c.imag for c in path)) == 1
calculate_heat = lambda path: sum(heat_map[pos] for pos in path) if len(path) > 2 else inf

#get_direction = lambda c: complex(c.real/abs(c.real), 0) if c.imag == 0 else complex(0, c.imag/abs(c.imag), 0)

def more_than_three_in_line(came_from, current):
    path = [current]
    for _ in range(4):
        if current not in came_from:
            print(current)
            return False
        current = came_from[current]
        path.append(current)
    # if len(path) != len(set(path)):
    #     return True
    # if path[-1] == path[-3]:
    #  return True
    return more_than_three(path)

nice_directions = {
    0-1j: '^',
    0+1j: 'v',
    -1+0j: '<',
    1+0j: '>',
}



def least_heat(start=1+1j, end=complex(MAX_COLUMN, MAX_ROW)):
    frontier = PriorityQueue()
    
    frontier.put(PrioritizedItem(0, [DIRECTIONS['down']]))
    frontier.put(PrioritizedItem(0, [DIRECTIONS['right']]))
    heat_so_far = dict()
    heat_so_far[start] = 0
    result = inf

    while not frontier.empty():
        item = frontier.get()
        current_heat = item.priority
        directions_so_far = item.item
        current_position = start + sum(directions_so_far)
        if len(directions_so_far)>=4 and len(set(directions_so_far[-4:])) == 1:
            continue
        if current_position not in heat_map:
            continue
        new_heat = current_heat + heat_map[current_position]
        if current_position not in heat_so_far or heat_so_far[current_position] > new_heat:
            heat_so_far[current_position] = new_heat
        if current_position == end:
            result = min(new_heat, result)
            print(result, ''.join(nice_directions[c] for c in directions_so_far))
            return

        for d in DIRECTIONS.values():
            frontier.put(PrioritizedItem(new_heat, directions_so_far + [d]))



# 913 too high

party_1 = least_heat()
print_solutions(party_1)