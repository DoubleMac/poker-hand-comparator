from abc import ABC
from functools import total_ordering

from poker.card import Card


@total_ordering
class Hand(ABC):
    value: int

    def __init__(self, hand: list[Card]):
        self.hand = hand
        
    # New
    def stripSuits(self):
        return [card.rank for card in self.hand]

    def __lt__(self, other):
        if not isinstance(other, Hand):
            raise ValueError()

        if self.value == other.value:
            # Old
            # return self.hand < other.hand
        
            # New
            return self.stripSuits() < other.stripSuits()
        else:
            return self.value < other.value

    def __eq__(self, other):
        if not isinstance(other, Hand) or self.value != other.value:
            return False

        # Old
        # return self.hand < other.hand
    
        # New
        return self.stripSuits() == other.stripSuits()


class StraightFlush(Hand):
    value = 100


class FourOfAKind(Hand):
    value = 90


class FullHouse(Hand):
    value = 80


class Flush(Hand):
    value = 70


class Straight(Hand):
    value = 60


class ThreeOfAKind(Hand):
    value = 50


class TwoPair(Hand):
    value = 40


class OnePair(Hand):
    value = 30


class HighCard(Hand):
    value = 20
