from santas_little_helpers.helpers import *


input_data = read_input(15, numbers=False, separator=',')

def hash(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

party_1 = sum(hash(string) for string in input_data)
print_solutions(party_1)

def test_one():
    assert party_1 == 509784
