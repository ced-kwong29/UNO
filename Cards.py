''' Parent class for all cards types in the deck '''
class card:
    colors = {'red', 'blue', 'green', 'yellow'}
    def __init__(self, color: str, func: str, value: int):
        self.color = color
        self.func = func
        self.value = value


''' Number-type cards that do not perform any action '''
class numberCard(card):
    def __init__(self, color: str, num: int):
        card.__init__(self, color, 'num', num)
        self.num = num

    def __repr__(self):
        return f'Card({self.color}, {self.num})'

    def __str__(self):
        return f'{self.color} {self.num}'


''' Cards that perform actions except for wild cards and draw-4s '''
class actionCard(card):
    types = {'reverse', 'skip', 'draw2'}
    val = 20
    def __init__(self, color: str, action: str):
        card.__init__(self, color, action, actionCard.val)
        self.action = action

    def __repr__(self):
        return f'Card({self.color}, {self.action})'

    def __str__(self):
        return f'{self.color} {self.action}'


''' Allow players that played them to change the color for the next turn '''
class wildCard(card):
    types = {'wild', 'draw4'}
    val = 50
    def __init__(self, action: str):
        card.__init__(self, str(None), action, wildCard.val)
        self.action = action

    def __repr__(self):
        return f'Card({self.action})'

    def __str__(self):
        return f'{self.action}'
