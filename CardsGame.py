import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spade diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def choice(self):
        return choice(self)

    def __call__(self, *args, **kwargs):
        return self.choice()


def factorial(n):
    '''returns n'''
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    deck = FrenchDeck()
    print(deck.choice())
    print(deck())
