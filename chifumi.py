from math import *
from random import *
from keyboard import *
from time import *
from os import *

languages = [
    "French",
    "English",
    "Japan"
]
chifumi = [
    ["Pierre", "Rock", "chi"],
    ["Feuille", "Paper", "fu"],
    ["Ciseaux", "Scissors", "mi"]
]

def play():
    global chifumi
    global languages

    system('cls')
    if question("Use the default key ?", ["Yes","No"]) == 0:
        players = [
            player(
                question("Name of player " + str(i+1) + " ?", "input", 0, "Player " + str(i))
            )
            for i in range(2)
        ]
        players[1].key = ["q","s","d"]
    else:
        players = [
            player(
                question("Name of player " + str(i+1) + " ?", "input", 0, "Player " + str(i)),
                [
                    question("Press the key of " + chifumi[j][1] + " for the player " + str(i), "key")
                    for j in range(len(chifumi))
                ]
            )
            for i in range(2)
        ]
    Rounds = question("Numbers of rounds won to win (2 by default) :", "input int")
    lang = question(
        "Choose the language of the result of a round", 
        [
            languages[i] + " (" + str(chifumi[0][i]) + " - " + str(chifumi[1][i]) + " - " + str(chifumi[2][i]) + ")"
            for i in range(len(languages))
        ]
    )
    while not(players[0].point==Rounds or players[1].point==Rounds):
        for i in range(len(players)):
            players[i].newround()
        timer = time()
        rebour = 5
        while time()-timer < 5:
            if not rebour == int(5 - (time()-timer)):
                system('cls')
                print("You can play")
                print("Timer: " + str(rebour))
                scoring(players, 2)
            rebour = int(5 - (time()-timer))
            for i in range(len(players)):
                players[i].play()
        
        system('cls')
        for i in range(len(players)):
            if players[i].round[-1] == -1:
                print(str(players[i].name) + ": Miss to play")
            else:
                print(str(players[i].name) + ": " + chifumi[players[i].round[-1]][lang])
        print("")
        if players[0].round[-1] == -1 and not players[1].round[-1] == -1:
            players[1].markpoint()
        elif players[1].round[-1] == -1 and not players[0].round[-1] == -1:
            players[0].markpoint()
        elif (players[0].round[-1] - 1) % len(chifumi) == players[1].round[-1]:
            players[0].markpoint()
        elif (players[1].round[-1] - 1) % len(chifumi) == players[0].round[-1]:
            players[1].markpoint()
        else:
            print("egality")
        scoring(players, 4)
        sleep(3)
    system('cls')
    for i in range(len(players)):
        if players[i].point == Rounds:
            print(players[i].name + " Win")
    scoring(players, 1)

    while not is_pressed("enter"):
        pass
    input()
    system('cls')
            

def question(title, name, pos=0, default=""):
    system('cls')
    print(title)

    if isinstance(name, str):
        if "input" in name:
            inp = input()
            if inp.replace(" ","") == "":
                inp = default
            if "int" in name:
                try:
                    inp = int(inp)
                except:
                    inp = 2
            while is_pressed("enter"):
                pass
            return inp

        if "key" in name:
            myKey = read_key()
            while is_pressed(myKey):
                pass
            return myKey
            
    else:
        while True:
            system('cls')
            print(title)
            for i in range(len(name)):
                if i == pos:
                    print("▶  " + str(name[i]))
                else:
                    print("      " + str(name[i]))
            
            sleep(0.2)
            myKey = read_key()
            if myKey=="haut":
                pos = max(0,min((pos - 1), len(name)-1))
            if myKey=="bas":
                pos = max(0,min((pos + 1), len(name)-1))
            if myKey=="enter":
                while is_pressed("enter"):
                    pass
                input()
                return pos

def scoring(players, lines):
    for i in range(8 - lines):
        print("")
    for i in range(len(players)):
        print(players[i].name + "'s score: " + str(players[i].point))

class player:
    def __init__(self, name, key=["1","2","3"]):
        self.name = name
        self.key = key
        self.point = 0
        self.round = [-1]
    
    def newround(self):
        self.round.append(-1)

    def play(self):
        for i in range(len(self.key)):
            if is_pressed(self.key[i]):
                self.round[-1] = i
    
    def markpoint(self):
        self.point += 1
        print(self.name + " have mark the point")