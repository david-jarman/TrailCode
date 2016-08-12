from random import random

class Card(object):
    def __init__(self, _value, _suit):
        self.value = _value
        self.suit = _suit

    def __str__(self):
        return "%s %s" % (self.value, self.suit)

def shuffleDeck(cards):
    num_cards = len(cards)

    for i in range(0, num_cards):
        index = int(random() * (num_cards - i)) + i
        any_card = cards[index]
        swap_card = cards[i]
        cards[i] = any_card
        cards[index] = swap_card

    return cards

suits = ["hearts", "diamonds", "spades", "clubs"]
cards = []

for suit in suits:
    for num in range(1,14):
        new_card = Card(num, suit)
        cards.append(new_card)

for card in cards:
    print card

shuffleDeck(cards)

print "shuffled cards:"

for card in cards:
    print card
