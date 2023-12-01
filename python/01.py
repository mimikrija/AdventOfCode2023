from santas_little_helpers.helpers import *
from re import findall

input_data = read_input(1)
party_1 = 0
for line in input_data:
    numbers = findall(r'\d', line)
    party_1 += int(numbers[0]+numbers[-1])




party_2 = 0

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words_reversed = [word[::-1] for word in words]

bla = '|'.join(c for c in words)
truc = '|'.join(c for c in words_reversed)

def convert(s):
    if len(s) == 1:
        return int(s)
    return words.index(s)+1

def converts(s):
    if len(s) == 1:
        return int(s)
    return words_reversed.index(s)+1


for line in input_data:
    numbers = findall(f'\d|{bla}', line)
    fun = findall(f'\d|{truc}', line[::-1])
    print(line, numbers[0], numbers[-1], convert(numbers[0]), convert(numbers[-1]), int(str(convert(numbers[0]))+str(convert(numbers[-1]))))
    party_2 += int(str(convert(numbers[0]))+str(converts(fun[0])))

print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 53386

def test_two():
    assert party_2 == 53312
