from Cards import card, numberCard, actionCard, wildCard
from Player import player, AI
from Order import orderOfTurns
import random


numLimit = 10
intActDup, wildDup = 2, 4
startingHand = 7
maxPlayers = 4


''' Class that represents the entire game of UNO '''
class UNO:
    def __init__(self):
        self.deck = list()
        self.playedCards = list()
        self.players = set()
        self.order = orderOfTurns()
        self.user = None

    # Creates a shuffled deck of 108 cards
    def buildDeck(self) -> None:
        for c in card.colors:
            for n in range(numLimit):
                if n > 0:
                    self.deck += [numberCard(c,n)] * intActDup
                else:
                    self.deck.append(numberCard(c,n))
            for a in actionCard.types:
                self.deck += [actionCard(c,a)] * intActDup
        
        for w in wildCard.types:
            self.deck += [wildCard(w)] * wildDup

        random.shuffle(self.deck)
        print("deck built")

    # Adds shuffled deck of played cards to the bottom of the deck
    def recycleCards(self) -> None:
        random.shuffle(self.playedCards)

        allRecycled = False
        while not allRecycled:
            played = self.playedCards.pop(0)
            self.deck.insert(0,played) 
            
            if not self.playedCards:
                allRecycled = True

    # Distributes cards to each player 
    def distributeHands(self) -> None:
        totalCards = startingHand * self.order.count
        while totalCards > 0:
            for p in self.players:
                topCard = self.deck.pop()
                p.hand.append(topCard)
                totalCards -= 1
        print("hands distributed")

    # Establishes number of players and assigns user their turn in the game
    def startGame(self) -> None:
        valid = False
        group = 0

        while not valid:
            group = int(input("How many players?:   "))
            if group <= maxPlayers:
                valid = True
        
        userNum = random.randint(1, group)
        self.user = player(input("Enter a username:    "))
        for n in range(1, group+1):
            if n == userNum:
                self.order.addPlayer(self.user)
                self.players.add(self.user)
            else:
                newAI = AI(n)
                self.order.addPlayer(newAI)
                self.players.add(newAI)

        self.order.cycleOfTurns()

    # Continuously draws a card
    def drawCard(self, lastCard) -> list: 
        valid = list()
        while not valid:
            print("drawing from deck")
            draw = self.deck.pop()
            if draw.color == lastCard.color:
                valid.append(draw)

            if isinstance(lastCard, numberCard) and isinstance(draw, numberCard):
                if lastCard.num == draw.num:
                    valid.append(draw)

            if isinstance(lastCard, actionCard) and isinstance(draw, actionCard):
                if lastCard.action == draw.action:
                    valid = draw

            if isinstance(draw, wildCard):
                valid.append(draw)
        
        print(valid)
        return valid

    # Runs loop that allows for gameplay until someone wins the game or all players quit
    def gameplay(self) -> None:
        firstPlay = self.deck.pop()
        self.playedCards.append(firstPlay)
        lastCard = firstPlay

        gameOver = False
        while not gameOver:
            print(lastCard)
            if self.order.turn.cur == self.user:
                self.user.sortHand()
                print(self.user.hand)

                played = None
                while played is None:
                    selected = int(input("Enter index of card: "))
                    if selected == -1:
                        drawn = self.drawCard(lastCard)
                        played = self.user.selectCard(lastCard, drawn.pop())
                        self.user.hand += drawn
                    else:
                        played = self.user.selectCard(lastCard, selected)

                self.playedCards.append(played)
                lastCard = played
                if len(self.user.hand) == 0:
                    gameOver = True
                
            self.order.nextPlayer()

    # Runs the entire game
    def main(self) -> None:
        self.startGame()
        self.buildDeck()
        self.distributeHands()
        self.gameplay()
        print("gameOver")




if __name__ == "__main__":
    u = UNO()
    u.main()
