from santas_little_helpers.helpers import *


input_data = read_input(13, separator='\n\n')

images = [{(x, y) for y, row in enumerate(image.split('\n'), start=1) for x, symbol in enumerate(row, start=1) if symbol == '#'} for image in input_data]

def is_full_mirror(full_image, cropped_image, mirrored_image):
    return all( c in full_image for c in mirrored_image) and all(c in mirrored_image for c in cropped_image)

def is_smudged_mirror(full_image, cropped_image, mirrored_image):
    return {len(mirrored_image-cropped_image), len(cropped_image-mirrored_image)} == {0,1}

def horizontal_mirror(image, criterion):
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
        if criterion(image, cropped, mirror):
            return horizontal_axis
    return 0

def vertical_mirror(image, criterion):
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
        if criterion(image, cropped, mirror):
            return horizontal_axis
    return 0



party_1, party_2 = (sum(horizontal_mirror(image, criterion) + 100*vertical_mirror(image, criterion) for image in images) for criterion in (is_full_mirror, is_smudged_mirror))

print_solutions(party_1,party_2)



def test_one():
    assert party_1 == 40006

def test_two():
    assert party_2 == 28627
