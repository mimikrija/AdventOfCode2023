from santas_little_helpers.helpers import *


input_data = read_input(4)


party_1 = 0
wins_per_card = list()
for line in input_data:
    winning, mine = ({w for w in winning.split()} for winning in line.split(": ")[1].split(" | "))
    wins_per_card.append((wins:=len(winning & mine)))
    party_1 += 2**(wins-1) if wins else 0


final_counts = [1 for _ in wins_per_card]
for pos,win_counts in enumerate(wins_per_card, start=1):
    for w in range(win_counts):
        final_counts[pos+w] += final_counts[pos-1]

party_2 = sum(final_counts)

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 24542

def test_two():
    assert party_2 == 8736438
