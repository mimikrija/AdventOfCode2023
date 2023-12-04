from santas_little_helpers.helpers import *


input_data = read_input(4)


party_1 = 0
scratch_cards = list()
for line in input_data:
    numbers = line.split(": ")[1]
    winning, mine = numbers.split(" | ")
    winning = set(int(w) for w in winning.split())
    mine = set(int(m) for m in mine.split())
    winning_count = len(winning & mine)
    card_score = 0
    if winning_count:
        card_score = 2**(winning_count-1)
        party_1 += card_score
    scratch_cards.append(winning_count)


counts = [1 for _ in scratch_cards]

for pos,win_counts in enumerate(scratch_cards, start=1):
    for w in range(win_counts):
        counts[pos+w] += counts[pos-1]

party_2 = sum(counts)
        
print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 24542

def test_two():
    assert party_2 == 8736438
