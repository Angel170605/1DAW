from __future__ import annotations
from cards import *
from helpers import *


class Dealer:
    def __init__(self, players: list[Player]) -> None:
        self.players = players

    @classmethod
    def give_common_cards(cls, common_cards: list[cards]) -> None:
        cls.common_cards = common_cards
        
    
    def give_private_cards(self, private_cards: list[list[Card]]) -> None:
        for i, player in enumerate(self.players):
            player.get_private_cards(private_cards[i])
            
    def get_winner(self):      
        hands = [player.best_hand() for player in self.players]
        winner_hand = max(hands)
        hand_idx = hands.index(winner_hand)
        winner = self.players[hand_idx] if self.players[0].best_hand().hand_ranks == self.players[1].best_hand().hand_ranks else None
        return (winner, winner_hand)

class Player:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_private_cards(self, private_cards: list[Cards]) -> list:
        self.private_cards = private_cards

    def best_hand(self) -> Hand:
        all_cards = Dealer.common_cards + self.private_cards
        all_hands = combinations(all_cards, n=5)
        return max(all_hands)
        
       
        
       

        
