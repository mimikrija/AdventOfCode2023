from santas_little_helpers.helpers import *
import re


input_data = read_input(2)

print(input_data[:4])

cubes_in_bag = {"red": 12, "green": 13, "blue": 14}

find_red = re.compile(r'(\d+) (red)')
find_green = re.compile(r'(\d+) (green)')
find_blue = re.compile(r'(\d+) (blue)')

party_1 = 0
party_2 = 0
for ID, line in enumerate(input_data, start=1):
    c = re.findall(find_red, line)
    possible_red = not any(int(rc[0]) > cubes_in_bag["red"] for rc in c)
    min_red = max(int(rc[0]) for rc in c)

    c = re.findall(find_green, line)
    possible_green = not any(int(rc[0]) > cubes_in_bag["green"] for rc in c)
    min_green = max(int(rc[0]) for rc in c)
    
    c = re.findall(find_blue, line)
    possible_blue = not any(int(rc[0]) > cubes_in_bag["blue"] for rc in c)
    min_blue= max(int(rc[0]) for rc in c)

    party_2 += min_blue * min_red * min_green

    if possible_red and possible_green and possible_blue:
        party_1 += ID

print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 2156

def test_two():
    assert party_2 == 66909

