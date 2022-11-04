from library import *

languages = [
    "French",
    "English",
    "Japan latin",
    "Japan"
]
chifumi = [
    ["Pierre", "Rock", "hi", "ひ"],
    ["Feuille", "Paper", "fu", "ふ"],
    ["Ciseaux", "Scissors", "mi", "み"]
]

def play():
    global chifumi
    global languages

    nbrPlayer = 2 + (question("Do you want to play with a bot ?", ["Yes","No"]) - 1)

    cls()
    if question("Use the default key ?", ["Yes","No"]) == 0:
        players = [
            player(
                question("Name of player " + str(i+1) + " ?", "input", "Player " + str(i+1))
            )
            for i in range(nbrPlayer)
        ]
        players[0].key = ["q","s","d"]
    else:
        players = [
            player(
                question("Name of player " + str(i+1) + " ?", "input", "Player " + str(i+1)),
                [
                    question("Press the key of " + chifumi[j][1] + " for the player " + str(i), "key")
                    for j in range(len(chifumi))
                ]
            )
            for i in range(nbrPlayer)
        ]
    Rounds = question("Numbers of rounds won to win the game (2 by default) :", "input int")
    lang = question(
        "Choose the language of the result of a round", 
        [
            languages[i] + " (" + str(chifumi[0][i]) + " - " + str(chifumi[1][i]) + " - " + str(chifumi[2][i]) + ")"
            for i in range(len(languages))
        ]
    )
    if nbrPlayer == 1:
        players.append(player("BOT", "botkey"))

    while not(players[0].point==Rounds or players[1].point==Rounds):
        for i in range(len(players)):
            players[i].newround()
        timer = time()
        rebour = 5
        while time()-timer < 5:
            if not rebour == int(5 - (time()-timer)):
                cls()
                print("You can play")
                print("Timer: " + str(rebour))
                scoring(players, 2)
            rebour = int(5 - (time()-timer))
            for i in range(len(players)):
                players[i].play()
        
        cls()
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
    cls()
    for i in range(len(players)):
        if players[i].point == Rounds:
            print(players[i].name + " Win")
    scoring(players, 1)

    while not is_pressed("enter"):
        pass
    input()
    cls()

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
        if self.key == "botkey":
            if self.round[-1] == -1:
                self.round[-1] = randint(0,2)
        else:
            for i in range(len(self.key)):
                if is_pressed(self.key[i]):
                    self.round[-1] = i
    
    def markpoint(self):
        self.point += 1
        print(self.name + " have mark the point")

cls()
play()