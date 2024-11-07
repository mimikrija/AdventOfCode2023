from santas_little_helpers.helpers import *


input_data = read_input(13, separator='\n\n')

images = [{(x, y) for y, row in enumerate(image.split('\n'), start=1) for x, symbol in enumerate(row, start=1) if symbol == '#'} for image in input_data]
flipped_images = [{(y, x) for x, y in image} for image in images]

def is_full_mirror(full_image, cropped_image, mirrored_image):
    return all( c in full_image for c in mirrored_image) and all(c in mirrored_image for c in cropped_image)

def is_smudged_mirror(full_image, cropped_image, mirrored_image):
    return {len(mirrored_image-cropped_image), len(cropped_image-mirrored_image)} == {0,1}


def find_mirror_axis(image, criterion):
    max_row_or_column = max(x for x, _ in image)
    for axis in range(1, max_row_or_column):
        mirror = set()
        for x, y in image:
            if x > axis:
                distance = x - axis - 1
                new_x = axis - distance
                if new_x in range(1, axis + 1):
                    mirror.add((new_x, y))
        axis_distance = min(max_row_or_column-axis, axis)
        limit_range = range(axis-axis_distance + 1, axis + 1)
        cropped = {(x, y) for x, y in image if x in limit_range}
        if criterion(image, cropped, mirror):
            return axis
    return 0


party_1, party_2 = (sum(find_mirror_axis(image, criterion) + 100*find_mirror_axis(flipped_image, criterion)
                        for image, flipped_image in zip(images, flipped_images))
                            for criterion in (is_full_mirror, is_smudged_mirror))

print_solutions(party_1,party_2)



def test_one():
    assert party_1 == 40006

def test_two():
    assert party_2 == 28627
