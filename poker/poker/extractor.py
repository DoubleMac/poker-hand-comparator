from abc import ABC, abstractmethod
from itertools import groupby
from typing import Optional

from poker.card import Card, Rank
from poker.hand import (
    Hand,
    Straight,
    Flush,
    FourOfAKind,
    FullHouse,
    
    # New
    StraightFlush,
    
    ThreeOfAKind,
    TwoPair,
    OnePair,
    HighCard,
)


class BaseHandExtractor(ABC):
    @abstractmethod
    def extract(self, cards: list[Card]) -> Optional[Hand]:
        pass
    
    #New
    @staticmethod
    def sortCards(cards: list[Card]) -> list[Card]:
        """
        :return: list[Card] sorted by descending card rank
        """
        cards.sort(reverse=True)
        return cards

    @staticmethod
    def group_by_rank(cards: list[Card]) -> dict[Rank, list[Card]]:
        """
        :return: a dict with rank as key, and a list of cards with that rank as value.
        """
        sorted_hand = sorted(cards)
        return {
            key: list(group)
            for key, group in groupby(sorted_hand, lambda card: card.rank)
        }

    def group_by_multiples(self, cards: list[Card]) -> dict[int, list[list[Card]]]:
        """
        :return: a dict with number of copies as key, and groups of multiples as value
                 e.g. {2: [[2D, 2C], [3H, 3S]]}
        """
        rank_lookup = self.group_by_rank(cards)
        rank_groups = list(rank_lookup.values())
        sorted_ranks = sorted(rank_groups, key=len)
        return {
            key: list(group)
            for key, group in groupby(sorted_ranks, len)
        }


class StraightFlushExtractor(BaseHandExtractor):
    def extract(self, cards: list[Card]) -> Optional[Hand]:
        # Old
        # pass
        
        # New
        if StraightExtractor().extract(cards) and FlushExtractor().extract(cards):
            return StraightFlush(self.sortCards(cards))


class FourOfAKindExtractor(BaseHandExtractor):
    def extract(self, cards: list[Card]) -> Optional[Hand]:
        multiples = self.group_by_multiples(cards)
        if multiples.get(4):
            quad = multiples[4][0]
            kicker = list(set(cards) - set(quad))
            return FourOfAKind(quad + kicker)


class FullHouseExtractor(BaseHandExtractor):
    def extract(self, cards: list[Card]) -> Optional[Hand]:
        multiples = self.group_by_multiples(cards)
        if multiples.get(3) and multiples.get(2):
            triple = multiples[3][0]
            pair = multiples[2][0]
            return FullHouse(triple + pair)


class FlushExtractor(BaseHandExtractor):
    def extract(self, cards: list[Card]) -> Optional[Hand]:
        suits = set(card.suit for card in cards)
        if len(suits) == 1:
            # Old
            # return Flush(cards)
            
            # New
            return Flush(self.sortCards(cards))


class StraightExtractor(BaseHandExtractor):
    def extract(self, cards: list[Card]) -> Optional[Hand]:
        ranks = set(card.rank for card in cards)
        if len(ranks) == 5 and max(ranks).value - min(ranks).value == 4:
            # Old
            # return Straight(cards)
            
            # New
            return Straight(self.sortCards(cards))


class ThreeOfAKindExtractor(BaseHandExtractor):
    def extract(self, cards: list[Card]) -> Optional[Hand]:
        multiples = self.group_by_multiples(cards)
        if multiples.get(3):
            triple = multiples[3][0]
            kickers = list(set(cards) - set(triple))
            return ThreeOfAKind(triple + kickers)


class OnePairExtractor(BaseHandExtractor):
    def extract(self, cards: list[Card]) -> Optional[Hand]:
        multiples = self.group_by_multiples(cards)
        if multiples.get(2):
            pair = multiples[2][0]
            
            # Old
            # kickers = list(set(cards) - set(pair))
            
            # New
            kickers = self.sortCards(list(set(cards) - set(pair)))
            
            return OnePair(pair + kickers)


class TwoPairExtractor(BaseHandExtractor):
    def extract(self, cards: list[Card]) -> Optional[Hand]:
        multiples = self.group_by_multiples(cards)
        if len(multiples.get(2, [])) == 2:
            # Old
            # all_pairs = multiples[2]
            # pair_cards = sum(all_pairs)
            
            # New
            pair_cards = multiples[2][1] + multiples[2][0]
            
            kickers = list(set(cards) - set(pair_cards))
            return TwoPair(pair_cards + kickers)


class HighCardExtractor(BaseHandExtractor):
    def extract(self, cards: list[Card]) -> Optional[Hand]:
        # Old
        # return HighCard(cards)
    
        # New
        return HighCard(self.sortCards(cards))


class HandExtractor(BaseHandExtractor):
    def extract(self, cards: list[Card]) -> Optional[Hand]:
        extractors = [
            StraightFlushExtractor(),
            FourOfAKindExtractor(),
            FullHouseExtractor(),
            FlushExtractor(),
            StraightExtractor(),
            ThreeOfAKindExtractor(),
            
            # Old
            # OnePairExtractor(),
            # TwoPairExtractor(),
            
            # New
            TwoPairExtractor(),
            OnePairExtractor(),
            
            HighCardExtractor(),
        ]
        for extractor in extractors:
            hand = extractor.extract(cards)
            if hand:
                return hand
