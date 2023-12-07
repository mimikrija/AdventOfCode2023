from santas_little_helpers.helpers import *
from collections import Counter
from functools import cmp_to_key

input_data = read_input(7)
#input_data = get_input('inputs/07e.txt')


RANKINGS = ['high card', 'pair', 'two pairs', 'three of a kind', 'full house', 'four', 'five']

def card_rank(card, is_part_2=True):
    count = Counter(card)
    groups = sorted(((count[r], r) for r in count), key=lambda x: x[0], reverse=True)
    if is_part_2 and count['J'] > 0:
        if count['J'] >= 4:
            return 'five'
        if count['J'] == 3:
            if len(groups) == 2:
                return 'five'
            else:
                return 'four'
        if count['J'] == 2:
            if len(groups) == 2:
                return 'five'
            if len(groups) == 3:
                return 'four'
            if len(groups) == 4:
                return 'three of a kind'
        else:
            if len(groups) == 2:
                return 'five'
            if len(groups) == 3:
                if all(c == 2 for m, c in count.items() if m!= 'J'):
                    return 'full house'
                return 'four'
            if len(groups) == 4:
                return 'three of a kind'
            if len(groups) == 5:
                return 'pair'
    

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

#card_labels = '23456789TJQKA'






def compare_cards(card1, card2):
    card_labels = 'J23456789TQKA' #part 2
    #card_labels = '23456789TJQKA'
    rank_1 = card_rank(card1)
    rank_2 = card_rank(card2)

    if RANKINGS.index(rank_1) > RANKINGS.index(rank_2):
        return 1
    elif RANKINGS.index(rank_1) < RANKINGS.index(rank_2):
        return -1
    else: # same ranking
        for l, r in zip(card1, card2):
            if l != r:
                return 1 if card_labels.index(l) > card_labels.index(r) else -1



cards = dict()

for line in input_data:
    card, bid = line.split()
    cards[card] = int(bid)

# for card in cards:
#     print(card, card_rank(card))


rankings = sorted(cards, key=cmp_to_key(compare_cards))


party_1 = sum(rank*cards[sorted_card] for rank, sorted_card in enumerate(rankings, start=1))
print(party_1)

def test_one():
    assert party_1 == 249726565

def test_one():
    assert party_2 == 251135960

# pt 2
card_labels = 'J23456789TQKA'




rankings = sorted(cards, key=cmp_to_key(compare_cards))


party_2 = sum(rank*cards[sorted_card] for rank, sorted_card in enumerate(rankings, start=1))
print(party_2) 
# 251548631 too high
# 251442624 too high
# 250759257 too low
# 250800628 not the right answer 
# 251483995 NOT!!!
# 249897972
# 251256747 NOT!!!
# 251175847
# 251069366
# 251257628
# 251257628 # NOT!!! hahahaha

# 251135960 YESSSS