from Cards import card, numberCard, actionCard, wildCard
import random


''' Base Class that represents players '''
class player:
    def __init__(self, username: str):
        self.name = username
        self.hand = []
        self.gamesWon = 0
        self.gamesLost = 0
        self.score = 0

    def __repr__(self) -> str:
        return f'Player({self.name})'

    def __str__(self) -> str:
        return self.name

    # Sorts a player's hand to make it easier to see their cards
    def sortHand(self) -> None:
        self.hand.sort(key = lambda c: (c.color, c.value, c.func))

    # Allows player to select a card from their hand by entering the index of the card
    def selectCard(self, lastCard: card, ndx: int) -> (card | None):
        if ndx in range(len(self.hand)):
            selected = self.hand[ndx]
            
            if lastCard.color == selected.color:
                return self.hand.pop(ndx)

            if isinstance(lastCard, numberCard) and isinstance(selected, numberCard):
                if lastCard.num == selected.num:
                    return self.hand.pop(ndx)

            if isinstance(lastCard, actionCard) and isinstance(selected, actionCard):
                if lastCard.action == selected.action:
                    return self.hand.pop(ndx)

            if isinstance(selected, wildCard):
                return self.hand.pop(ndx)
                
        return None


''' AI that inherits methods of the Player class '''
class AI(player):
    def __init__(self, ID):
        player.__init__(self, f'AI-{ID}')

