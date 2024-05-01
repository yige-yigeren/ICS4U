import random

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.playedcard = ""

    def playcard(self, card):
        if len(self.cards) == 0:
            return False
        choice = random.choice(self.cards)
        self.cards.remove(choice)
        return choice
    
    def getcard(self,card):
        self.cards.append(card)

rawcards = [[(str(i) if i <= 10 else {11: 'J', 12: 'Q', 13: 'K'}[i]) + j, True] for i in range(1, 14) for j in ["H", "S", "C", "D"] + ["JR", "JB"]]

player1 = Player("Player1")
player2 = Player("Player2")
desk1side = []
desk2side = []

for i in range(54):
    card = random.choice(rawcards)
    rawcards.remove(card)
    if i % 2 == 0:
        player1.getcard(card[0])
    else:
        player2.getcard(card[0])
    
while True:
    desk1side.append(player1.playcard())
    desk2side.append(player2.playcard())

    
