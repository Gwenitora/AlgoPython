from library import *
import chifumi

games = [
    "Chifumi",
    "Quit"
]

def start():
    global games

    question("Welcome on the games of Gwenitora and LoBot (G.Tech1B - group 1)", "empty")
    while True:
        game = question("Choose a game:", games)
        if games[game] == games[0]:
            chifumi.play()
        elif games[game] == games[-1]:
            break
    question("Thanks for playing, bye.", "empty")
    cls()

start()