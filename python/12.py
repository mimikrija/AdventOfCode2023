from santas_little_helpers.helpers import *
from functools import cache


@cache
def find_all_combinations(rest, groups):

    # if no groups left, valid combinations are only if there is
    # no # in the rest of the string
    if not groups:
        return '#' not in rest

    # if the string is empty (and groups aren't)
    # means we reached the end of it without solving
    # for all groups
    if not rest:
        return 0

    # there is no point in trying to solve if sum of group lengths
    # is greater than the rest of the string - we can't fit them
    # although I am curious to know why the logic below doesn't cover
    # this case
    if sum(groups) > len(rest):
        return 0
    
    # start here, we examine first character in the rest of the string
    # and take the current group size
    character = rest[0]
    group_size = groups[0]

    # no combinations possible here, continue solving from next char
    if character == '.':
        return find_all_combinations(rest[1:], groups)

    # we found a spring
    if character == '#':
        # enough space to fit the group and more
        if len(rest) > group_size:
            # we check if all chars in the range of group size are # or ?
            # but we also check that the first char after the group is a limiter ? or .
            if all(c in '#?' for c in rest[:group_size]) and rest[group_size] in '?.':
                # this is a valid combination; continue solving from the next char
                # after the group and for the rest of the groups
                return find_all_combinations(rest[group_size + 1:], groups[1:])
            # if those conditions are not met - this is not a valid combination
            else:
                return 0
        # group size fits the end of the string exactly:
        if len(rest) == group_size:
            # if all chars in the range of group size are # or ?
            # it is a valid combination
            return all(c in '#?' for c in rest)
        # this means rest is smaller than group size, so not enough room
        else:
            return 0
    
    # the forking logic! if ?, we can go both ways
    if character == '?':
        # sum the combinations obtained if ? was a # and if ? was a .
        # in the first one we replace ? with # and continue,
        # in the second one we continue with trimmed rest (same as . condition)
        return find_all_combinations('#' + rest[1:], groups) + find_all_combinations(rest[1:], groups)



def combos_per_line(line):
    rest, groups = line.split(' ')
    groups = tuple([int(num) for num in groups.split(',')])
    return find_all_combinations(rest, groups)


input_data = read_input(12)
party_1 = sum(combos_per_line(line) for line in input_data)

big_data = ['?'.join((s:=line.split())[0] for _ in range(5)) + ' ' + ','.join(s[1] for _ in range(5)) for line in input_data  ]
party_2 = sum(combos_per_line(line) for line in big_data) # 

print_solutions(party_1, party_2)




def test_one():
    assert party_1 == 7402

def test_two():
    assert party_2 == 3384337640277
