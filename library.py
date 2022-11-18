from math import *
from random import *
from keyboard import *
from time import *
from pygame import *
from sys import *
from os import *
from copy import *


def question(questi, answers, default=""):
    if not "noClear" in answers: cls()
    print(questi)

    if isinstance(answers, str):
        if "input" in answers:
            inp = input()
            if inp.replace(" ","") == "":
                inp = default
            if "int" in answers:
                try:
                    inp = int(inp)
                except:
                    try:
                        inp = int(default)
                    except:
                        inp = 0
            while is_pressed("enter"):
                pass
            return inp

        if "key" in answers:
            myKey = read_key()
            while is_pressed(myKey):
                pass
            question(questi + "\nYou choice the key '" + myKey + "'\nType enter to continue", "empty")
            return myKey

        if "empty" in answers:
            while not is_pressed("enter"):
                pass
            while is_pressed("enter"):
                pass
            input()
            return
            
    elif isinstance(answers, list):
        try:
            pos = int(default)
        except:
            pos = 0
        
        while True:
            cls()
            print(questi)
            for i in range(len(answers)):
                if i == pos:
                    print("▶  " + str(answers[i]))
                else:
                    print("      " + str(answers[i]))
            
            sleep(0.2)
            myKey = read_key()
            if myKey=="haut":
                pos = max(0,min((pos - 1), len(answers)-1))
            if myKey=="bas":
                pos = max(0,min((pos + 1), len(answers)-1))
            if myKey=="enter":
                while is_pressed("enter"):
                    pass
                input()
                return pos

def cls(): system('cls')