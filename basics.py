# basics.py

"""
A module with card resources, mainly a class implementing a 52 (or 104, etc.) card
deck using numpy for shuffling.
"""

import numpy as np

class Card():
    """
    Supporter class for Deck.

    --DETAILS--
    - Suits are valued by integers: Clubs=1, Diamonds=2, Hearts=3, Spades=4
    - Card values are standard, but face cards are represented by continuing
    integers: Jack=11, Queen=12, King=13, Ace=14 (NOTE: Aces are unique,
    and may need to be switched to 1.)
    """
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def __repr__(self):
        val_repr = -1
        if self.get_val() <= 10:
            val_repr = self.val
        elif self.get_val() == 11:
            val_repr = 'JACK'
        elif self.get_val() == 12:
            val_repr = 'QUEEN'
        elif self.get_val() == 13:
            val_repr = 'KING'
        elif self.get_val() == 14:
            val_repr = 'ACE'

        suit_repr = None
        if self.get_suit() == 1:
            suit_repr = 'CLUBS'
        elif self.get_suit() == 2:
            suit_repr = 'DIAMONDS'
        elif self.get_suit() == 3:
            suit_repr = 'HEARTS'
        elif self.get_suit() == 4:
            suit_repr = 'SPADES'

        return '{}--{}'.format(val_repr, suit_repr)

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

    def get_suit(self):
        return self.suit

    def set_suit(self, suit):
        self.suit = suit

class Deck():
    """
    Class simulating a deck of cards, supporting shuffling.
    """
    def __init__(self, num_decks=1):
        self.num_decks = num_decks # 52*num_decks = len(cards)
        self.aces = aces # aces high or low
        self.cards = []
        for deck in range(self.num_decks):
            for suit in range(1,5): # actually only looks for 1, 2, 3, 4
                for val in range(2,15): # ^ for 2, ..., 14
                    card = Card(val, suit)
                    self.cards.append(card)

    def __len__(self): # supports len(deck)
        return len(self.cards)

    def __repr__(self):
        return self.cards

    def __str__(self): # supports print(deck)
        str = ''
        for card in self.cards: # prints line by line
            str += '{}\n'.format(card)
        return str

    def stats(self):
        """
        Return number of cards in each suit, bookkeeping method to make sure deck
        is maintained.
        """
        CLUBS, DIAMONDS, HEARTS, SPADES = 0, 0, 0, 0
        for card in self.cards:
            if card.get_suit() == 1:
                CLUBS += 1
            if card.get_suit() == 2:
                DIAMONDS += 1
            if card.get_suit() == 3:
                HEARTS += 1
            if card.get_suit() == 4:
                SPADES += 1
        return "CLUBS: {}--DIAMONDS: {}--HEARTS: {}--SPADES: {}".format(CLUBS, DIAMONDS, HEARTS, SPADES)

    def shuffle(self):
        """
        Method to shuffle deck in-place. Relies on numpy.random.
        """
        shuffled = np.random.choice(self.cards, 52, replace=False)
        self.cards = shuffled

    def deal(self, num=1):
        """
        Deal some number of cards, default one. If returning one card, returns
        an instance of class Card. If returning multiple, returns as a list.
        """
        to_deal = []
        for idx in range(num):
            to_deal.append(self.cards[0])
            self.cards = self.cards[1:]
        if len(to_deal) > 1:
            return to_deal
        else:
            return to_deal[0]
