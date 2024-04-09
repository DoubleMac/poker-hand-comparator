from enum import IntEnum
from typing import NamedTuple


class Suit(IntEnum):
    SPADES = 4
    HEARTS = 3
    CLUBS = 2
    DIAMONDS = 1

    @staticmethod
    def from_str(suit_str: str) -> "Suit":
        for name, member in Suit.__members__.items():
            if suit_str.upper() == name[0]:
                return member
        raise ValueError


class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    @staticmethod
    def from_str(rank_str) -> "Rank":
        for name, member in Rank.__members__.items():
            if rank_str.upper() == name[0] or rank_str == str(member.value):
                return member
        raise ValueError


class Card(NamedTuple):
    rank: Rank
    suit: Suit

    @staticmethod
    def from_str(card_str: str) -> "Card":
        # Old
        # rank_str = card_str[0]
        # suit_str = card_str[1]
        
        # New
        if len(card_str) > 2:
            rank_str = card_str[:2]
            suit_str = card_str[2]
        else:
            rank_str = card_str[0]
            suit_str = card_str[1]
            
        return Card(
            rank=Rank.from_str(rank_str),
            suit=Suit.from_str(suit_str)
        )
