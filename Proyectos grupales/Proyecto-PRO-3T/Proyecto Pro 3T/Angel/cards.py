from __future__ import annotations
from helpers import *

class Card:
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    SUITS = ('❤', '◆', '♣', '♠')
    ALL_CARDS = {}

    def __init__(self, value: str) -> None:
        self.value = value
        self.rank = value[:-1]
        self.suit = value[-1]

    def __gt__(self: Card, other: Card) -> bool:
        return Card.RANKS.index(self.rank) > Card.RANKS.index(other.rank)
    
    # Comprueba si una carta es mayo que otra a traves de índices

    def __str__(self) -> str:
        return self.value

class Deck:
    def __init__(self) -> None:
        self.cards = [f'{rank}{suit}' for suit in Card.SUITS for rank in Card.RANKS]
        shuffle(self.cards)

    # Genera el mazo y lo baraja

class Hand:
    HAND_LENGTH = 5
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

    def __init__(self, cards: list[Card]) -> None:
        self.cards = sorted(cards)
        self.cat = Hand.HIGH_CARD
        self.cat_rank = self.cards[-1].rank

        # ordena el mazo y mira la carta más alta

    def is_straight_flush(self) -> bool:
        target_suit = self[0].suit
        valid_cards = tuple(card.rank for card in self if card.suit == target_suit)
        cmp_start = Card.RANKS.index(valid_cards[0])
        return valid_cards == Card.RANKS[cmp_start : cmp_start + Hand.HAND_LENGTH]

        #comprueba si hay escalera de color

    def is_four_of_a_kind(self) -> bool:
        pass

    def is_full_house(self) -> bool:
        pass

    def is_flush(self) -> bool:
        target_suit = self[0].suit
        valid_cards = [card for card in self if card.suit == target_suit]
        return valid_cards == Hand.HAND_LENGTH

    def is_straight(self) -> bool:
        pass

    def is_three_of_a_kind(self) -> bool:
        pass

    def is_two_pair(self) -> bool:
        pass

    def is_one_pair(self) -> bool:
        pass

    def get_cat(self) -> int:
        if self.is_straight_flush():
            return Hand.STRAIGHT_FLUSH
        elif self.is_four_of_a_kind():
            return Hand.FOUR_OF_A_KIND
        elif self.is_full_house():
            return Hand.FULL_HOUSE
        elif self.is_flush():
            return Hand.FLUSH
        elif self.is_straight():
            return Hand.STRAIGHT
        elif self.is_three_of_a_kind():
            return Hand.THREE_OF_A_KIND
        elif self.is_two_pair():
            return Hand.THREE_OF_A_KIND
        elif self.is_one_pair():
            return Hand.ONE_PAIR
        else:
            return Hand.HIGH_CARD
    

    def __contains__(self: Hand, card: Card) -> bool:
        return card in self.cards
    
    def __gt__(self: Hand, other: Hand) -> bool | None:
        if self.cat == other.cat:
            if self.cat_rank == other.cat_rank:
                return None
            return self.cat_rank > other.cat_rank
        return self.cat > other.cat
    
    def __getitem__(self, index: int):
        return self.cards[index]
    
    def __iter__(self):
        return HandIterator(self)


class HandIterator:
    def __init__(self, hand: Hand) -> None:
        self.hand = hand
        self.pointer = 0
    
    def __next__(self):
        if self.pointer >= len(self.hand.cards):
            raise StopIteration
        else:
            item = self.hand[self.pointer]
            self.pointer += 1
            return item

if __name__ == '__main__':
    hand1 = Hand([Card('10♣'), Card('9♣'), Card('8♣'), Card('7♣'), Card('6♣')])
    print(hand1.is_straight_flush())