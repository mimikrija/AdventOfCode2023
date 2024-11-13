from santas_little_helpers.helpers import *
from collections import defaultdict


input_data = read_input(18)

# parse instructions
instructions_part_1 = [((spl:=line.split())[0], int(spl[1])) for line in input_data]
instructions_part_2 = list()
for line in input_data:
    color = line.split()[2]
    dir = int(color[-2])
    count = int(color[2:7], 16)
    instructions_part_2.append((dir, count))


DIRECTIONS = {
    'R': 1+0j,
    0:   1+0j,

    'D': 0+1j,
    1:   0+1j,

    'L':-1+0j,
    2:  -1+0j,

    'U': 0-1j,
    3:   0-1j,
}

def calculate_vertices(instructions):
    current = 0+0j
    vertices = [current]
    for dir, count in instructions:
        current += DIRECTIONS[dir] * count
        vertices.append(current)
    return vertices


def shoelace_formula(vertices):
    list_vertices = vertices + [vertices[0]]
    left_shoelace = sum(a.real * b.imag for a, b in zip(list_vertices, list_vertices[1:]))
    right_shoelace = sum(a.imag * b.real for a, b in zip(list_vertices, list_vertices[1:]))
    area = abs(left_shoelace - right_shoelace) //2
    return int(area)


def perimeter(instructions):
    return sum(ins[1] for ins in instructions)

def calculate_area(instructions):
    vertices = calculate_vertices(instructions)
    return perimeter(instructions) // 2 + 1 + shoelace_formula(vertices)

party_1 = calculate_area(instructions_part_1)
party_2 = calculate_area(instructions_part_2)

print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 53300

def test_two():
    assert party_2 == 64294334780659
