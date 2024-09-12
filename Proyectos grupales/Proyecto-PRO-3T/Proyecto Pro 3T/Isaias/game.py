from cards import *
from roles import *

def get_winner(
    players: list[Player],
    common_cards: list[Card],
    private_cards: list[list[Card]],
    ) -> tuple[Player | None, Hand]:
    dealer = Dealer(players)
    dealer.unveil_common_cards(common_cards)
    dealer.give_private_cards(private_cards)
    winner, winner_hand = dealer.find_winner()
    return (winner, winner_hand)

if __name__ == '__main__':
    dealer = Dealer([Player('Player 1'), Player('Player 2')])
    dealer.unveil_common_cards([Card('A♠'), Card('Q❤'), Card('9♠'), Card('5♣'), Card('4◆')])
    dealer.give_private_cards([[Card('J◆'), Card('10❤')], [Card('K❤'), Card('2❤')]])
    winner, winner_hand = dealer.find_winner()
    print(winner, winner_hand)
    print(Card.RANKS.index('A'))
    print(Card.RANKS.index('Q'))

