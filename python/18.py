from santas_little_helpers.helpers import *
from collections import defaultdict


input_data = read_input(18)

# parse instructions
instructions = [((spl:=line.split())[0], int(spl[1]), spl[2]) for line in input_data]

DIRECTIONS = {
    'U': 0-1j,
    'D': 0+1j,
    'L':-1+0j,
    'R': 1+0j,
    'UL': -1-1j,
    'UR': 1-1j,
    'DL': -1+1j,
    'DR': 1+1j,
}

def expand_inwards(edge, start):
    frontier = {start}
    inside = {start}
    while frontier:
        current = frontier.pop()
        if current in outer_edge:
            continue
        for neighbor in (current + dir for dir in DIRECTIONS.values()):
            if neighbor not in edge and neighbor not in inside:
                inside.add(neighbor)
                frontier.add(neighbor)
    return len(inside) + len(outer_edge)


# draw outer edge
outer_edge = set()
pos = 0+0j
for dir, count, color in instructions:
    outer_edge |= {pos+n*DIRECTIONS[dir] for n in range(1, count+1)}
    pos += count*DIRECTIONS[dir]


rows = defaultdict(list)
for c in outer_edge:
    rows[int(c.imag)].append(int(c.real))

rows = {row: sorted(columns) for row, columns in rows.items()}

print(sorted(rows.items(), key=lambda x: x[0])[:2])

party_1 = expand_inwards(outer_edge, start=-2-208j)

print_solutions(party_1)

def test_one():
    assert party_1 == 53300

