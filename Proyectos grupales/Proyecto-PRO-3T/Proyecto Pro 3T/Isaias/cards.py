from __future__ import annotations
from helpers import *

class Card:
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    SUITS = ('❤', '◆', '♣', '♠')

    def __init__(self, value: str) -> None:
        self.value = value
        self.rank = value[:-1]
        self.suit = value[-1]

    def __gt__(self: Card, other: Card) -> bool:
        return Card.RANKS.index(self.rank) > Card.RANKS.index(other.rank)
    
    def __eq__(self, other: Card) -> bool:
        return self.rank == other.rank

    def __str__(self) -> str:
        return self.value

class Deck:
    def __init__(self) -> None:
        self.cards = [f'{rank}{suit}' for suit in Card.SUITS for rank in Card.RANKS]
        shuffle(self.cards)

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
        self.hand_ranks = tuple(card.rank for card in self)
        self.hand_suits = tuple(card.suit for card in self)
        self.cat = self.get_cat()

    def is_straight_flush(self) -> bool:
        if len(set(self.hand_suits)) == 1:
            cmp_start = Card.RANKS.index(self[0].rank)
            return self.hand_ranks == Card.RANKS[cmp_start : cmp_start + Hand.HAND_LENGTH]
        return False

    def is_four_of_a_kind(self) -> bool:
        target_rank = self[0].rank
        same_cards = 0
        for card in self:
            if card.rank == target_rank:
                same_cards += 1
                if same_cards == 4:
                    self.cat_rank = target_rank
                    break
            else:
                same_cards = 1
                target_rank = card.rank
        return same_cards >= 4

    def is_full_house(self) -> bool:
        unique_ranks = set(self.hand_ranks)
        if len(unique_ranks) == 2:
            self.cat_rank = []
            for rank in unique_ranks:
                if self.hand_ranks.count(rank) == 3:
                    self.cat_rank.insert(0, rank)
                else:
                    self.cat_rank.append(rank)
            self.cat_rank = tuple(self.cat_rank)
            return True
        return False

    def is_flush(self) -> bool:
        target_suit = self[0].suit
        valid_cards = tuple(card for card in self if card.suit == target_suit)
        return len(valid_cards) == Hand.HAND_LENGTH

    def is_straight(self) -> bool:
        cmp_start = Card.RANKS.index(self[0].rank)
        hand_cards_ranks = tuple(card.rank for card in self)
        return hand_cards_ranks == Card.RANKS[cmp_start : cmp_start + Hand.HAND_LENGTH]

    def is_three_of_a_kind(self) -> bool:
        target_rank = self[0].rank
        same_cards = 0
        for card in self:
            if card.rank == target_rank:
                same_cards += 1
                if same_cards == 3:
                    self.cat_rank = target_rank
                    break
            else:
                same_cards = 1
                target_rank = card.rank
        return same_cards == 3

    def is_two_pair(self) -> bool:
        target_rank = self[0].rank
        same_cards = 0
        pairs = 0
        ranks_idxs = []
        for card in self:
            if card.rank == target_rank:
                same_cards += 1
                if same_cards == 2:
                    pairs += 1
                    same_cards = 0
                    ranks_idxs.append(Card.RANKS.index(target_rank))
                    if pairs == 2:
                        ranks_idxs = sorted(ranks_idxs, reverse=True)
                        self.cat_rank = tuple(Card.RANKS[i] for i in ranks_idxs)
                        break
            else:
                same_cards = 1
                target_rank = card.rank
        return pairs == 2

    def is_one_pair(self) -> bool:
        target_rank = self[0].rank
        same_cards = 0
        for card in self:
            if card.rank == target_rank:
                same_cards += 1
                if same_cards == 2:
                    self.cat_rank = target_rank
                    break
            else:
                same_cards = 1
                target_rank = card.rank
        return same_cards == 2

    def get_cat(self) -> int:
        if self.is_straight_flush():
            cat = Hand.STRAIGHT_FLUSH
            self.cat_rank = self[-1].rank
        elif self.is_four_of_a_kind():
            cat = Hand.FOUR_OF_A_KIND
        elif self.is_full_house():
            cat = Hand.FULL_HOUSE
        elif self.is_flush():
            cat = Hand.FLUSH
            self.cat_rank = self[-1].rank
        elif self.is_straight():
            cat = Hand.STRAIGHT
            self.cat_rank = self[-1].rank
        elif self.is_three_of_a_kind():
            cat = Hand.THREE_OF_A_KIND
        elif self.is_two_pair():
            cat = Hand.TWO_PAIR
        elif self.is_one_pair():
            cat = Hand.ONE_PAIR
        else:
            cat = Hand.HIGH_CARD
            self.cat_rank = self[-1].rank
        return cat
    
    def __str__(self):
        return '-'.join(str(card) for card in self)

    def __contains__(self: Hand, card: Card) -> bool:
        return str(card) in tuple(str(card) for card in self)
    
    def __gt__(self: Hand, other: Hand) -> bool | None:
        if self.cat == other.cat:
            if self.cat_rank == other.cat_rank:
                for card1, card2 in zip(reversed(self.cards), reversed(other.cards)):
                    if card1 > card2:
                        return True
                    elif card1 == card2:
                        continue
                    else:
                        return False
                return False
            if isinstance(self.cat_rank, tuple):
                hand1_ranks = tuple(Card.RANKS.index(rank) for rank in self.cat_rank)
                hand2_ranks = tuple(Card.RANKS.index(rank) for rank in other.cat_rank)
                if self.cat == Hand.FULL_HOUSE:
                    return hand1_ranks[0] * 3 + hand1_ranks[1] * 2 > hand2_ranks[0] * 3 + hand2_ranks[1] * 2
                else:
                    return hand1_ranks[0] * 2 + hand1_ranks[1] * 2 > hand2_ranks[0] * 2 + hand2_ranks[1] * 2
            else:
                return Card.RANKS.index(self.cat_rank) > Card.RANKS.index(other.cat_rank)
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
    carta = Card('Q❤')
    hand1 = Hand([Card('10♣'), Card('9♣'), Card('8♣'), Card('7♣'), Card('6♣')])
    print(hand1.get_cat())
    hand2 = Hand([Card('6◆'), Card('6♣'), Card('6❤'), Card('6♠'), Card('Q♠')])
    print(hand2.get_cat())
    hand3 = Hand([Card('Q❤'), Card('Q♠'), Card('Q◆'), Card('4♣'), Card('4◆')])
    print(hand3.get_cat())
    hand4 = Hand([Card('J❤'), Card('8❤'), Card('5❤'), Card('4❤'), Card('3❤')])
    print(hand4.get_cat())
    hand5 = Hand([Card('J♠'), Card('10♣'), Card('9❤'), Card('8◆'), Card('7❤')])
    print(hand5.get_cat())
    hand6 = Hand([Card('9❤'), Card('9♣'), Card('9♠'), Card('Q◆'), Card('J❤')])
    print(hand6.get_cat())
    hand7 = Hand([Card('K❤'), Card('K◆'), Card('3❤'), Card('3◆'), Card('A◆')])
    print(hand7.get_cat())
    hand8 = Hand([Card('3◆'), Card('3♣'), Card('A❤'), Card('K◆'), Card('Q♣')])
    print(hand8.get_cat())
    hand9 = Hand([Card('A♠'), Card('K❤'), Card('Q❤'), Card('9♠'), Card('5♣')])
    print(hand9.get_cat())
    print(max([hand1, hand2, hand3]))
    print(hand1)
    print(max(hand1.cards))
    print(Card('Q❤') in hand3)

    hand10 = Hand([Card('A♠'), Card('Q❤'), Card('J❤'), Card('10❤'), Card('9♠')])
    print(hand9.cat_rank)
    print(hand10.cat_rank)
    print(max([hand10, hand9]))