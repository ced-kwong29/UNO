from Player import player


''' Contains a player as well as who plays before and after them in a game '''
class Turn:
    def __init__(self, cur, prev=None, next=None):
        self.cur = cur
        self.prev = prev
        self.next = next


''' Doubly LinkedList with a cycle to represent the order of turns for players '''
class orderOfTurns:
    def __init__(self):
        self.head = Turn("head")
        self.turn = None
        self.count = 0

    # Assigns a player their turn in the game
    def addPlayer(self, lastJoined: player) -> None:
        newPlayer = Turn(lastJoined)
        if self.head.next is None:
            self.head.next = newPlayer
        else:
            curPos = self.head.next
            while curPos.next:
                curPos = curPos.next
            curPos.next = newPlayer
            newPlayer.prev = curPos
        print(f'{lastJoined} has joined')
        self.count += 1

    # Creates the cycle of turns in the doubly linked list when everyone has joined
    def cycleOfTurns(self) -> None:
        start = self.head.next

        curPos = start
        while curPos.next:
            curPos = curPos.next
        curPos.next = start
        start.prev = curPos

        self.turn = start

    # Moves to the turn of the next player based on the cycle direction
    def nextPlayer(self, reversal=False) -> None:
        if reversal is True:
            self.turn = self.turn.prev
        else:
            self.turn = self.turn.next
    
