from math import *
from random import *
from keyboard import *
import os

def play():
    os.system('cls')
    key = question("Use the default key ?", ["Yes","No"])
    print(key)


def question(title, name, pos=0):
    wait = True
    while wait:
        os.system('cls')
        print(title)
        for i in range(len(name)):
            if i == pos:
                print("▶ " + str(name[i]))
            else:
                print("    " + str(name[i]))
        if read_key()=="haut": pos = max(0,min((pos - 1), len(name)-1))
        if read_key()=="bas": pos = max(0,min((pos + 1), len(name)-1))
        if read_key()=="enter":
            return pos

class player:
    def __init__(self, color, name, key):
        self.color = color
        self.name = name
        self.key = key
        self.point = 0

#    def play():

play()