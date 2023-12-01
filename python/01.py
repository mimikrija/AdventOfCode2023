from santas_little_helpers.helpers import *
import re

input_data = read_input(1)


party_1 = sum(int((digits:=re.findall(r'\d', line))[0]+digits[-1]) for line in input_data)


words = ['\\d', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words_reversed = ['\\d']+[word[::-1] for word in words[1:]]

forward, backward = (re.compile('|'.join(c for c in w)) for w in (words, words_reversed))

first_digit = lambda x: re.search(forward, x)[0]
last_digit = lambda x: re.search(backward, x[::-1])[0]

def convert_to_numbers(text, search_words):
    if len(text) == 1:
        return text
    return str(search_words.index(text))

def digits_to_number(d1, d2):
    d1 = convert_to_numbers(d1, words)
    d2 = convert_to_numbers(d2, words_reversed)
    return int(d1+d2)

party_2 = sum(digits_to_number(first_digit(line), last_digit(line)) for line in input_data)

print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 53386

def test_two():
    assert party_2 == 53312

