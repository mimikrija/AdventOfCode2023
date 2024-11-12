from santas_little_helpers.helpers import *
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

def least_heat(min_steps = 1, max_steps = 3, start=1+1j, end=complex(MAX_COLUMN, MAX_ROW)):
    frontier = PriorityQueue()
    # there are two possible ways to go
    frontier.put(PrioritizedItem(0, (start, DIRECTIONS['down'])))
    frontier.put(PrioritizedItem(0, (start, DIRECTIONS['right'])))
    heat_so_far = {(start, DIRECTIONS['right']): 0, (start, DIRECTIONS['down']): 0}


    while not frontier.empty():
        item = frontier.get()
        last_heat_score = item.priority
        last_position, last_direction = item.item
        
        if last_position == end:
            return last_heat_score
        
        for dir in set(DIRECTIONS.values()) - {last_direction, -last_direction}:
            current_positions = {steps: current_position for steps in range(max_steps, 0, -1)
                                 if (current_position:=last_position + steps*dir) in heat_map}
            for count, current_position in current_positions.items():
                if count >= min_steps:
                    new_heat_score = last_heat_score + sum(heat_map[current_positions[m]] for m in range(1, count + 1))
                    bla = (current_position, dir)
                    if bla not in heat_so_far or heat_so_far[bla] > new_heat_score:
                        heat_so_far[bla] = new_heat_score
                        frontier.put(PrioritizedItem(new_heat_score, bla))



party_1 = least_heat()
party_2 = least_heat(min_steps=4, max_steps=10)
print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 866

def test_two():
    assert party_2 == 1010
