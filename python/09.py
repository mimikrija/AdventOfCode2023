from santas_little_helpers.helpers import *


input_data = read_input(9)


def solve(sequence, part_2=False):
    if part_2:
        sequence.reverse()
    last = sequence[-1]
    while True:
        sequence = [right-left for left, right in zip(sequence[:-1], sequence[1:])]
        if all(c == 0 for c in sequence):
            return last
        last += sequence[-1]


sequences = [list(map(int, line.split())) for line in input_data]

party_1, party_2 = (sum(solve(sequence, pt2) for sequence in sequences) for pt2 in (False, True))

print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 1479011877

def test_two():
    assert party_2 == 973
