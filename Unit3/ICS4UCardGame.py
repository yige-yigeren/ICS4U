import random

def choicecard():
    global cardremain
    if cardremain == 0:
        return None
    for i in range(20): # try 20 times to find a card that hasn't been chosen
        card = random.choice(cards)
        if card[1]:
            card[1] = False
            cardremain -= 1
            return card[0]
    for i in range(52): # choose the first card that hasn't been chosen
        if cards[i][1]:
            cards[i][1] = False
            cardremain -= 1
            return cards[i][0]

def returncard(showcards): # return the card not in showcards back to the cards
    global cardremain
    for i in range(52):
        if cards[i][0] not in showcards:
            cards[i][1] = True
            cardremain += 1

def playcard(card):
    global playedcard
    for i in range(len(playercards)): 
        if playercards[i] == card:
            playercards.pop(i)
            playedcard = card
            break

cards = [[(str(i) if i <= 10 else {11: 'J', 12: 'Q', 13: 'K'}[i]) + j, True] for i in range(1, 14) for j in ["H", "S", "C", "D"]]
cardremain = 52
playercards = []
playedcard = ""

while True:
    print ("Player Hand: " + ", ".join(playercards))
    print ("Played Card: " + playedcard)
    while True:
        action = input("Do you want to (t)ake a card, (p)lay a card, (r)eturn a card, or (q)uit? ")
        if action == "t":
            if len(playercards) < 5:
                playercards.append(choicecard())
                break
            else:
                print ("You already have 5 cards.")
        elif action == "p":
            card = input("Which card do you want to play? ")
            if card in playercards:
                playcard(card)
                break
            else:
                print ("You don't have that card.")
        elif action == "r":
            showcards = [playedcard] + playercards
            returncard(showcards)
        elif action == "q":
            exit()
        else:
            print ("Invalid action.")

