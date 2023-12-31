from santas_little_helpers.helpers import *
from collections import Counter
from functools import cmp_to_key



def card_rank(card, part_2=False):
    groups = Counter(card)

    if part_2 and groups['J'] > 0:
        if len(groups) <= 2:
            return 'five'
        if len(groups) == 4:
            return 'three'
        if groups['J'] >= 3:
            return 'four'
        elif len(groups) == 3:
            if all(c == 2 for m, c in groups.items() if m!= 'J'):
                return 'full house'
            return 'four'
        return 'pair'

    # pt1 or if no J in the cards return standard ranking
    if len(groups) == 1:
        return 'five'
    if 4 in groups.values():
        return 'four'
    if 3 in groups.values() and 2 in groups.values():
        return 'full house'
    if sum(c == 2 for c in groups.values()) == 2:
        return 'two pairs'
    if 3 in groups.values():
        return 'three'
    if max(groups.values()) == 2:
        return 'pair'
    return 'high card'

def compare_helper(part_2=False):
    def compare(card1, card2):
        rank_1 = card_rank(card1, part_2)
        rank_2 = card_rank(card2, part_2)
        RANKINGS = ['high card', 'pair', 'two pairs', 'three', 'full house', 'four', 'five']
        card_labels='J23456789TQKA' if part_2 else '23456789TJQKA'
        if RANKINGS.index(rank_1) > RANKINGS.index(rank_2):
            return 1
        elif RANKINGS.index(rank_1) < RANKINGS.index(rank_2):
            return -1
        else: # same ranking, compare by first card
            for l, r in zip(card1, card2):
                if l != r:
                    return 1 if card_labels.index(l) > card_labels.index(r) else -1
    return compare


input_data = read_input(7)
cards = {(sp:=line.split())[0]: int(sp[1]) for line in input_data}

def total_winnings(cards, part_2=False):
    rankings = sorted(cards, key=cmp_to_key(compare_helper(part_2)))
    return sum(rank*cards[card] for rank, card in enumerate(rankings, start=1))


party_1, party_2 = (total_winnings(cards, part_2) for part_2 in (False, True))


print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 249726565

def test_two():
    assert party_2 == 251135960
