from santas_little_helpers.helpers import *
from collections import Counter
from functools import cmp_to_key

input_data = read_input(7)
#input_data = get_input('inputs/07e.txt')


rankings = ['high card', 'pair', 'two pairs', 'three of a kind', 'full house', 'four', 'five']

def card_rank(card):
    count = Counter(card)
    groups = sorted(((count[r], r) for r in count), key=lambda x: x[0], reverse=True)

    if len(groups) == 1:
        return 'five'
    if groups[0][0] == 4:
        return 'four'
    if groups[0][0] == 3 and groups[1][0] == 2:
        return 'full house'
    if groups[0][0] == 2 and groups[1][0] == 2:
        return 'two pairs'
    if len(groups) == 3 and groups[0][0] == 3:
        return 'three of a kind'
    if groups[0][0] == 2:
        return 'pair'
    return 'high card'

card_labels = '23456789TJQKA'


def compare_cards(card1, card2):
    rank_1 = card_rank(card1)
    rank_2 = card_rank(card2)

    if rankings.index(rank_1) > rankings.index(rank_2):
        return 1
    elif rankings.index(rank_1) < rankings.index(rank_2):
        return -1
    else: # same ranking
        for l, r in zip(card1, card2):
            if l != r:
                return 1 if card_labels.index(l) > card_labels.index(r) else -1



cards = dict()

for line in input_data:
    card, bid = line.split()
    cards[card] = int(bid)



rankings = sorted(cards, key=cmp_to_key(compare_cards))
print(rankings)

party_1 = sum(rank*cards[sorted_card] for rank, sorted_card in enumerate(rankings, start=1))
print(party_1)

def test_one():
    assert party_1 == 249726565