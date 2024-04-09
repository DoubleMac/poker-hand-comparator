import pytest

from poker.evaluate import compare

"""
changes made:

fixed card rank parser to accomodate 2-character ranks (ie 10)
    - card.py:48

fixed out of order hand rankings (2 pair over 1 pair)
    - extractor.py:169

fixed extracting list of all pair cards from 2-pair hands
    - extractor.py:140

fixed the comparison method for when hands have the same rank
    - sorted the list of cards returned by the hand extractor so that 
      a list comparision of the card ranks will act as a tie breaker
    - card list comparision only looks at card ranks, not suits
    - added extra tests to test tie breaker logic
    - extractor.py, hand.py, test_evaluate.py:95

implemented StraightFlush extractor using Straight and Flush extractors
    - extractor.py:64

no changes for evaluate.py
"""


@pytest.mark.parametrize(
    "hand1, hand2, expected_output",
    [
        # straight flush vs high card
        (
            "2S 3S 4S 5S 6S",
            "2D 3C 9C JH QH",
            "hand 1",
        ),
        # straight vs high card
        (
            "7S 8D 9D 10H JC",
            "QH 2D 3C 9C JH",
            "hand 1",
        ),
        # one pair vs two pair
        (
            "2S 2H JH QC AS",
            "2D 2C 9C 9H QH",
            "hand 2",
        ),
        # straight flush high 6 vs straight flush high 6
        (
            "2S 3S 4S 5S 6S",
            "6D 5D 4D 3D 2D",
            "equal",
        ),
        # straight flush vs full house
        (
            "2S 3S 4S 5S 6S",
            "4D 3C 7C 5H 6H",
            "hand 1",
        ),
        # pair 3s high 9 vs pair 3s high jack
        (
            "3D 3S 4C 5S 9S",
            "3H 3C 2C 6H JH",
            "hand 2",
        ),
        # high queen vs high ace
        (
            "3D 10S JC 2S QS",
            "3H 4C 2C AH KH",
            "hand 2",
        ),
        # straight flush vs four of a kind
        (
            "3D 4D 7D 6D 5D",
            "9C 9D 10C 9H 9S",
            "hand 1",
        ),
        # two pair high 6s vs two pair high 5s
        (
            "3D 3S 7D 6D 6H",
            "4C 4D 10C 5H 5S",
            "hand 1",
        ),
        # pair 3s high queen vs pair 3s high ace
        (
            "3D 4D JH QS 3H",
            "3S 2S KH 3C AD",
            "hand 2",
        ),
        
        # additional tests for testing tie breaker (cardSort) logic
        # one pair vs two pair
        (
            "2S 2H QC JH AS",
            "9C 9H QH 2D 2C",
            "hand 2",
        ),
        # flush high 9 vs flush high jack
        (
            "2S 3S 9S 5S 6S",
            "6D JD 4D 3D 2D",
            "hand 2",
        ),
        # pair 5s pair 3s vs pair 5s pair 4s
        (
            "3D 3S 7D 5D 5H",
            "4C 4D 10C 5H 5S",
            "hand 2",
        )
    ]
)

def test_evaluate(hand1, hand2, expected_output):
    result = compare(hand1, hand2)
    assert expected_output == result
