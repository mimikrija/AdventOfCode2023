from santas_little_helpers.helpers import *
import re
from math import lcm
from itertools import cycle

input_data = read_input(8)
instructions = [c for c in input_data[0]]
nodes = {(c:=re.findall(r'[A-Z]+', line))[0]: (c[1], c[2]) for line in input_data[2:]}


def find_all_paths(instructions, nodes, pos='AAA', part_2 = True):
    instr = cycle(instructions)
    count = 0
    while True:
        pos = nodes[pos][next(instr) == 'R']
        count += 1
        if part_2:
            if pos[-1] == 'Z':
                return count
        elif pos == 'ZZZ':
            return count


party_1 = find_all_paths(instructions, nodes)

starts = (pos for pos in nodes if pos[-1] == 'A')
party_2 = lcm(*[find_all_paths(instructions, nodes, start, True) for start in starts])

print_solutions(party_1, party_2)


def test_1():
    assert party_1 == 19631

def test_two():
    assert party_2 == 21003205388413
