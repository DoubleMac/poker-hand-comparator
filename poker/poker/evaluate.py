import sys

from poker.card import Card
from poker.extractor import HandExtractor
from poker.hand import Hand


def hand_from_str(hand_str: str) -> Hand:
    cards = list(map(Card.from_str, hand_str.split()))
    return HandExtractor().extract(cards)


def compare(hand_str1: str, hand_str2: str):
    hand1 = hand_from_str(hand_str1)
    hand2 = hand_from_str(hand_str2)

    if hand1 < hand2:
        return "hand 2"
    elif hand1 > hand2:
        return "hand 1"
    else:
        return "equal"


if __name__ == "__main__":
    print(compare(sys.argv[1], sys.argv[2]))
