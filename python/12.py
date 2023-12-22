from santas_little_helpers.helpers import *
import re
from itertools import product

input_data = read_input(12)
party_1 = 0
for line in input_data:
    arr = 0
    test_line = [l for l in line]
    indices = [x.start() for x in re.finditer(r'\?', line)]
    groups = [int(num) for num in re.findall(r'\d+', line)]
    for permo in product('.#', repeat=len(indices)):
        for pos, symbol in zip(indices, permo):
            test_line[pos] = symbol
        test = ''.join(c for c in test_line)
        ranges = []
        for m in re.finditer(r'#+', test):
            l, r = m.span()
            ranges.append(r-l)
        if len(ranges) == len(groups):
            if all(r==g for r,g in zip(ranges, groups)):
                arr += 1
    party_1 += arr

print_solutions(party_1)

def test_one():
    assert party_1 == 7402
