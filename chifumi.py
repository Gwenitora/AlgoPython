from math import *
from random import *
from keyboard import *
from time import *
from os import *

chifumi = [
    ["Pierre", "Rock", "chi"],
    ["Feuille", "Sheet", "fu"],
    ["Ciseaux", "Scissors", "mi"]
]

def play():
    global chifumi

    system('cls')
    if question("Use the default key ?", ["Yes","No"]) == 0:
        players = [
            player(
                question("Color of player " + str(i+1) + " ?", ["Red","Blue","Green"]),
                question("Name of player " + str(i+1) + " ?", "input")
            )
            for i in range(2)
        ]
        players[1].key = ["q","s","d"]
    else:
        players = [
            player(
                question("Color of player " + str(i+1) + " ?", ["Red","Blue","Green"]),
                question("Name of player " + str(i+1) + " ?", "input"),
                [
                    question("Press the key of " + chifumi[j][1] + " for the player " + str(i), "key")
                    for j in range(len(chifumi))
                ]
            )
            for i in range(2)
        ]
    Rounds = question("Numbers of rounds won to win (2 by default) :", "input int")
    print(Rounds)

def question(title, name, pos=0):
    system('cls')
    print(title)

    if isinstance(name, str):
        if "input" in name:
            inp = input()
            if "int" in name:
                try:
                    inp = int(inp)
                except:
                    inp = 2
            while is_pressed("enter"):
                wait = 1
            return inp

        if "key" in name:
            myKey = read_key()
            while is_pressed(myKey):
                wait = 1
            return myKey
            
    else:
        while True:
            system('cls')
            print(title)
            for i in range(len(name)):
                if i == pos:
                    print("▶ " + str(name[i]))
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
                    wait = 1
                input()
                return pos

class player:
    def __init__(self, color, name, key=["1","2","3"]):
        self.color = color
        self.name = name
        self.key = key
        self.point = 0

#    def play(round):

play()