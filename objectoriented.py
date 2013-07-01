"""
Chapter 8 | Object-Oriented Design
"""

# 81. Design the data structure for a generic deck of cards. Explain how you would subclass the data structures to implement blackjack.

import collections
import itertools
import random

Card = collections.namedtuple('Card', ['suit', 'rank'])

class Deck(object):

    suits = None
    ranks = None

    def __init__(self):
        self.cards = [Card(s, r) for (s, r) in itertools.product(self.suits, self.ranks)]


    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class StandardDeck(Deck)

    suits = 'ACHS'
    cards = [2,3,4,5,6,7,8,9,10,11,12,13,14]


    def repr(card):
        faces = {
            11: 'J',
            12: 'Q',
            13: 'K',
            14: 'A'
            }

        if card.value in faces:
            return faces[card.value]
        else:
            return str(card.value)


    def deal(self):

    
# Make a blackjack hand...super generic blah blah.
class Hand(object):

    def __init__(self, cards):
        self.cards = cards
        
        
