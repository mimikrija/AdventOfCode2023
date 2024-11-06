from santas_little_helpers.helpers import *


input_data = read_input(13, separator='\n\n')

images = [{(x, y) for y, row in enumerate(image.split('\n'), start=1) for x, symbol in enumerate(row, start=1) if symbol == '#'} for image in input_data]


def horizontal_mirror(image):
    MAX_X = max(x for x, y in image)
    for horizontal_axis in range(1, MAX_X):
        mirror = set()
        for x, y in image:
            if x > horizontal_axis:
                distance = x - horizontal_axis - 1
                new_x = horizontal_axis - distance
                if new_x in range(1, horizontal_axis + 1):
                    mirror.add((new_x, y))
        axis_distance = min(MAX_X-horizontal_axis, horizontal_axis)
        cropped = {(x, y) for x, y in image if x in range(horizontal_axis-axis_distance + 1, horizontal_axis + 1)}
        if all( c in image for c in mirror) and all(c in mirror for c in cropped):
            return horizontal_axis
    return 0

def vertical_mirror(image):
    MAX_Y = max(y for x, y in image)
    for horizontal_axis in range(1, MAX_Y):
        mirror = set()
        for x, y in image:
            if y > horizontal_axis:
                distance = y - horizontal_axis - 1
                new_y = horizontal_axis - distance
                if new_y in range(1, horizontal_axis + 1):
                    mirror.add((x, new_y))
        axis_distance = min(MAX_Y-horizontal_axis, horizontal_axis)
        cropped = {(x, y) for x, y in image if y in range(horizontal_axis-axis_distance + 1, horizontal_axis + 1)}
        if all( c in image for c in mirror) and all(c in mirror for c in cropped):
            return horizontal_axis
    return 0



party_1 = sum(horizontal_mirror(image) + 100*vertical_mirror(image) for image in images)
print_solutions(party_1)


def test_one():
    assert party_1 == 40006
