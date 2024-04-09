DEBUG CHANGES:

1. fixed card rank parser to accomodate 2-character ranks (ie 10)
    - card.py:48

2. fixed out of order hand rankings (2 pair over 1 pair)
    - extractor.py:169

3. fixed extracting list of all pair cards from 2-pair hands
    - extractor.py:140

4. fixed the comparison method for when hands have the same rank
    - sorted the list of cards returned by the hand extractor so that 
      a list comparision of the card ranks will act as a tie breaker
    - card list comparision only looks at card ranks, not suits
    - added extra tests to test tie breaker logic
    - extractor.py, hand.py, test_evaluate.py:95

5. implemented StraightFlush extractor using Straight and Flush extractors
    - extractor.py:64

6. no changes for evaluate.py

END OF DEBUG CHANGES

Poker is a family of card games played with a standard 52-card deck.
Each card has a unique rank and suit combination, where the ranks are
(from lowest to highest):
```
2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
```
and the suits are:
```
Spades, Hearts, Clubs, Diamonds
```

Players have access to five cards (hand), which may be classified into one
of nine categories (from low to high):

```
High card: no particular pattern; catch-all
One Pair: two cards with the same rank
Two pair: two pairs of two cards of the same rank
Three of a kind (triple): three cards of the same rank
Straight: five cards with consecutive ranks (e.g. 2 3 4 5 6, or 10 J Q K A)
Flush: five cards with the same suit
Full house: a triple and a pair
Four of a kind (quad): four cards of the same rank
Straight flush: straight that is also a flush
```

If two hands are of different categories, then
they are ranked according to their category. If they are of the same
category, then compare them as follows:

```
High card: compare highest card, then next highest, etc.
One Pair: compare pair, then the rest of the cards (kickers) like high card
Two pair: compare highest pair, then second pair, then the kicker
Three of a kind: compare triple, then kickers
Straight: compare by rank
Flush: compare like high card
Full house: compare triple, then double
Four of a kind: compare quad, then kicker
Straight flush: compare by rank
```

Two cards with the same rank but different suits are considered equal.

Your task is to create an evaluator that takes in two hands in string
format, and determines which hand is ranked higher. Your code should be
as **production** ready as possible.

Cards are input as strings, with their rank followed by the first letter
of their suit.

Examples:
- \#1
  - Hand 1: "2S 3S 4S 5S 6S"
  - Hand 2: "2D 3C 9C JH QH"
  - Hand 1 is a straight flush, while hand 2 is high card. Since hand 1 has a
  higher-ranking category, it is higher-ranked.
- \#2
  - Hand 1: "2S 2D JC 4D 4C"
  - Hand 2: "3D 3C 2H 4H 4S"
  - Both hands are two pair. Since hand 2's pairs (4s and 3s) are higher than
  hand 1's pairs (4s and 2s), it is higher. This is determined by first comparing
  the highest pair (4 vs 4) and then the second pair (3 vs 2).


Prerequisites:
- Python 3.9+

How to run:
- script:  
```
PYTHONPATH='.' python3 poker/evaluate.py "2S 3S 4S 5S 6S" "2D 3C 9C JH QH"
```
- tests:
```
PYTHONPATH='.' pytest
```