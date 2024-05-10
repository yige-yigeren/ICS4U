import random
import os
import tkinter as tk
from tkinter import PhotoImage

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.playedcard = ""

    def playcard(self):
        if len(self.cards) == 0:
            return 1
        card = self.cards[0]
        self.cards.pop(0)
        return card
    
    def getcard(self,card):
        self.cards.append(card)

def player1_click():
    global playstatus, warstatus
    if playstatus == 0 or playstatus == 1:
        if warstatus == 1 and len(player1.cards) < 3:
            tempcards.append(desk1side[0])
            for i in range(len(player1.cards)-1):
                tempcards.append(player1.playcard())
            desk1side[1] += len(player1.cards)
            desk1side[0] = player1.playcard()
        elif warstatus == 1:
            tempcards.append(desk1side[0])
            tempcards.append(player1.playcard())
            tempcards.append(player1.playcard())
            desk1side[1] += 3
            if playstatus == 1:
                playstatus = 3
            else:
                playstatus = 2
            desk1side[0] = player1.playcard()
        else:
            desk1side[0] = player1.playcard()
            if playstatus == 1:
                playstatus = 3
            else:
                playstatus = 2
    button1.config(state='disabled')
    update_info()
    root.after(1000, rules)

def player2_click():
    global playstatus, warstatus
    if playstatus == 0 or playstatus == 2:
        if warstatus == 1 and len(player2.cards) < 3:
            tempcards.append(desk2side[0])
            for i in range(len(player2.cards)-1):
                tempcards.append(player2.playcard())
            desk2side[1] += len(player2.cards)
            desk2side[0] = player2.playcard()
        elif warstatus == 1:
            tempcards.append(desk2side[0])
            tempcards.append(player2.playcard())
            tempcards.append(player2.playcard())
            desk2side[1] += 3
            if playstatus == 2:
                playstatus = 3
            else:
                playstatus = 1
            desk2side[0] = player2.playcard()
        else:
            desk2side[0] = player2.playcard()
            if playstatus == 2:
                playstatus = 3
            else:
                playstatus = 1
    button2.config(state='disabled')
    update_info()
    root.after(1000, rules)

def prepare():
    player1.cards = []
    player2.cards = []
    global desk1side, desk2side, tempcards
    desk1side = [100, 0]
    desk2side = [100, 0]
    tempcards = []
    rawcards = [i for i in range(2, 54)]
    for i in range(52):
        card = random.choice(rawcards)
        rawcards.remove(card)
        if i % 2 == 0:
            player1.getcard(card)
        else:
            player2.getcard(card)
    global playstatus, warstatus, Notice, roundstatus
    playstatus = 0
    warstatus = 0
    Notice = 'Welcome to War Card Game!'
    roundstatus = 0
    update_info()

def rules():
    global playstatus, warstatus, tempcards, Notice, roundstatus, desk1side, desk2side
    if playstatus == 3:
        # Compare card A max, 2 min
        mark1 = (desk1side[0]+10) % 13
        mark2 = (desk2side[0]+10) % 13
        if mark1 == mark2:
            warstatus = 1
            playstatus = 0
            Notice = "War!"
        elif mark1 > mark2:
            player1.cards += tempcards
            player1.cards += [desk1side[0]]
            player1.cards += [desk2side[0]]
            Notice = "Player 1 get!"
            playstatus = 0
            warstatus = 0
            tempcards = []
            desk1side = [100, 0]
            desk2side = [100, 0]
        else:
            player2.cards += tempcards
            player2.cards += [desk1side[0]]
            player2.cards += [desk2side[0]]
            Notice = "Player 2 get!"
            playstatus = 0
            warstatus = 0
            tempcards = []
            desk1side = [100, 0]
            desk2side = [100, 0]
    if player1.cards == [] and playstatus != 2 and playstatus != 3:
        Notice = "Player 2 wins!"
        roundstatus = 1
    elif player2.cards == [] and playstatus != 1 and playstatus != 3:
        Notice = "Player 1 wins!"
        roundstatus = 1
    if roundstatus == 1:
        button1.config(state='disabled')
        button2.config(state='disabled')
        update_info()
        root.after(5000, prepare)
        return
    update_info()

def update_info(): # Update all info on the screen
    button1.config(image=card_images[0] if len(player1.cards) > 0 else card_images[1])
    button2.config(image=card_images[0] if len(player2.cards) > 0 else card_images[1])
    label0.config(text=Notice)
    label1.config(text="Remaining cards: " + str(len(player1.cards)))
    label2.config(text="Remaining cards: " + str(len(player2.cards)))
    label_desk1_0.config(image=card_images[desk1side[0]] if desk1side[0] != 100 else card_images[1])
    label_desk2_0.config(image=card_images[desk2side[0]] if desk2side[0] != 100 else card_images[1])
    if desk1side[1] != 0:
        label_desk1_1.config(image=card_images[0])
        label_desk1_1_value.config(text=str(desk1side[1]))
        label_desk1_1.pack(side='left')
        label_desk1_1_value.pack(side='left')
    else:
        label_desk1_1.pack_forget()
        label_desk1_1_value.pack_forget()

    if desk2side[1] != 0:
        label_desk2_1.config(image=card_images[0])
        label_desk2_1_value.config(text=str(desk2side[1]))
        label_desk2_1.pack(side='right')
        label_desk2_1_value.pack(side='right')
    else:
        label_desk2_1.pack_forget()
        label_desk2_1_value.pack_forget()

    if desk1side[1] != 0:
        label_desk1_1.config(image=card_images[0])
        label_desk1_1_value.config(text=str(desk1side[1]))
    if desk2side[1] != 0:
        label_desk2_1.config(image=card_images[0])
        label_desk2_1_value.config(text=str(desk2side[1]))

    global playstatus, roundstatus
    if playstatus == 0 and roundstatus == 0:
        button1.config(state='normal')
        button2.config(state='normal')

# Global var
Notice = ''
playstatus = 0 # 0: no card played, 1: player1 played, 2: player2 played, 3: compare
warstatus = 0 # 0: no war, 1: war
roundstatus = 0 # 0: in round, 1: game ends
player1 = Player("Player1")
player2 = Player("Player2")
# first card on the desk, second cards not displayed
desk1side = [100, 0]
desk2side = [100, 0]
tempcards = [] # All card not show

# gui tk
root = tk.Tk()
root.title("War Card Game")
root.geometry("1000x700")

# card files path
files = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cards\\')
print(files)
card_images = [PhotoImage(file=files + "back.png"), PhotoImage(file=files + "empty.png")] + [PhotoImage(file=f"{files}{i}.png") for i in range(1,53)]

frame0 = tk.LabelFrame(root, height=200, text="Desk")
frame1 = tk.LabelFrame(root, height=200, text="Player 1")
frame2 = tk.LabelFrame(root, height=200, text="Player 2")
desk1 = tk.Frame(frame0, width=400, height=200)
desk0 = tk.Frame(frame0, width=200, height=200)
desk2 = tk.Frame(frame0, width=400, height=200)
button1 = tk.Button(frame1, image=card_images[0] if len(player1.cards) > 0 else card_images[1], command=player1_click)
button2 = tk.Button(frame2, image=card_images[0] if len(player2.cards) > 0 else card_images[1], command=player2_click)

label0 = tk.Label(desk0, text=Notice)
label1 = tk.Label(frame1, text="Remaining cards: " + str(len(player1.cards)))
label2 = tk.Label(frame2, text="Remaining cards: " + str(len(player2.cards)))
label_desk1_0 = tk.Label(desk1, image=card_images[1])
label_desk1_0.pack(side='left')
label_desk1_1 = tk.Label(desk1, image=card_images[0])
label_desk1_1.pack(side='left')
label_desk1_1_value = tk.Label(desk1, text='0')
label_desk1_1_value.pack(side='left')
label_desk2_0 = tk.Label(desk2, image=card_images[1])
label_desk2_0.pack(side='right')
label_desk2_1 = tk.Label(desk2, image=card_images[0])
label_desk2_1.pack(side='right')
label_desk2_1_value = tk.Label(desk2, text='0')
label_desk2_1_value.pack(side='right')

frame1.pack(fill='both', expand=True, side='top')
frame0.pack(fill='both', expand=True, side='top')
frame2.pack(fill='both', expand=True, side='bottom')
desk1.pack(fill='both', expand=True, side='left')
desk0.pack(fill='both', expand=True, side='left')
desk2.pack(fill='both', expand=True, side='right')

button1.pack()
button2.pack()
label0.pack()
label1.pack(side='left')
label2.pack(side='right')
label_desk1_0.pack()
label_desk2_0.pack()
prepare()

root.mainloop()