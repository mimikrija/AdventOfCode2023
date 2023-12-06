from santas_little_helpers.helpers import *
import re
from math import prod


def number_of_ways(total_time, record):
    return sum(speed*total_time - speed**2 > record for speed in range(1, total_time))


input_data = read_input(6)

total_times, records = ([int(n) for n in re.findall(r'\d+', line)] for line in input_data)
party_1 = prod(number_of_ways(total_time, record) for total_time, record in zip(total_times, records))


total_time, record = (int(''.join(c for c in line if c.isdigit())) for line in input_data)
party_2 = number_of_ways(total_time, record)

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 114400

def test_two():
    assert party_2 == 21039729
