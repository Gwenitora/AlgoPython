from math import *
from random import *
from keyboard import *
from time import *
from os import *

def question(title, name, default="", pos=0):
    cls()
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
            if myKey == "enter": input()
            return myKey

        if "empty" in name:
            while not is_pressed("enter"):
                pass
            while is_pressed("enter"):
                pass
            input()
            return
            
    elif isinstance(name, list):
        while True:
            cls()
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

def cls(): system('cls')