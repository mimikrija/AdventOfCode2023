from santas_little_helpers.helpers import *


input_data = read_input(15, numbers=False, separator=',')

def hash(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

def focusing_power(box_no, slot, focal_length):
    return (box_no+1) * slot * focal_length

def part_two(string, boxes):

    if '-' in string:
        label = string[:-1]
        operator = '-'
    if '=' in string:
        operator = '='
        label, focal_length = string.split('=')

    box = hash(label)
    if operator == '=':
        if all(lens[0] != label for lens in boxes[box]):
            boxes[box].append([label, focal_length])
        else:
            boxes[box] = [lens if lens[0] != label else [label, focal_length] for lens in boxes[box]]
    if operator == '-':
        new_box = []
        for c in boxes[box]:
            if c[0] != label:
                new_box.append(c)
        boxes[box] = new_box

party_1 = sum(hash(string) for string in input_data)


boxes = {n: [] for n in range(256)}

for c in input_data:
    part_two(c, boxes)

lenses_result = {}
for box, lenses in boxes.items():
    for pos, (lens, focal_length) in enumerate(lenses, start=1):
        lenses_result[lens] = [box, pos, int(focal_length)]



party_2 = sum(focusing_power(*bla) for bla in lenses_result.values())
print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 509784

def test_two():
    assert party_2 == 230197
