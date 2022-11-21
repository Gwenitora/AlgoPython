from library import *
import chifumi
import morpion

games = [
    "Chifumi",
    "Morpion (with Logan)",
    "Quit"
]

def start():
    global games

    question("Welcome on the games of Gwenitora (G.Tech1 - group B)", "empty")
    while True:
        game = question("Choose a game:", games, 1)
        if games[game] == games[-1]:
            break
        if games[game] == games[0]:
            chifumi.play()
        elif games[game] == games[1]:
            morpion.play()
    question("Thanks for playing, bye.", "empty")
    cls()

start()
