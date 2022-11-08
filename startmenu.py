from library import *
import chifumi

games = [
    "Chifumi",
    "Quit"
]

def start():
    global games

    question("Welcome on the games of Gwenitora (G.Tech1 - group B)", "empty")
    while True:
        game = question("Choose a game:", games)
        if games[game] == games[0]:
            chifumi.play()
        elif games[game] == games[-1]:
            break
    question("Thanks for playing, bye.", "empty")
    cls()

start()