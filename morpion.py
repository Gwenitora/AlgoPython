from library import *

def play():
    playing = 1
    while playing == 1:
        parameters = parameter()
        playing = 0
        while playing == 0:
            playing = gameplay(parameters)

def parameter():
    bot = (question("Do you want to play with a bot ?", ["Yes","No"], 1) - 1) * -1
    bot = (bot == 1)
    return bot

def gameplay(parameters):
    Plateau = Table(parameters)
    player = randint(1,2)
    playerStr = str(player).replace("1", "X").replace("2", "O")
    table = Plateau.printTable("Turn to player: " + playerStr)
    while True:
        cls()
        print(table)
        Plateau.modify(player)
        player %= 2
        player += 1
        playerStr = str(player).replace("1", "X").replace("2", "O")
        check = Plateau.check()
        table = Plateau.printTable("Turn to player: " + playerStr)
        if check == -1:
            Plateau.printTable()
            question((table + ' ')[18:-1] + "\n\nEquality", "empty")
            return question("Play again ?", ["Yes", "Yes, but with other parameters", "No, back to the menu"])
        elif check != 0:
            Plateau.printTable()
            question((table + ' ')[18:-1] + "\n\nPlayer " + str(check) + " Win", "empty")
            return question("Play again ?", ["Yes", "Yes, but with other parameters", "No, back to the menu"])

class Table:
    def __init__(self, bot, key = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]):
        self.table = [[0 for i in range(3)] for j in range(3)]
        self.bot = bot
        self.key = key
    
    def printTable(self, message = ''):
        text = ''
        for i in range(len(self.table)):
            k = ""
            for j in self.table[i]:
                k += " " + str(j).replace("1", "X").replace("2", "O").replace("0", " ") + " |"
            text += k[0:-1]
            if i != 2: text += "\n---+---+---\n"
        return message + "\n" + text
    
    def modify(self, player):
        if self.bot and player == 2:
            coord = self.dangerCase()
            self.table[coord[0]][coord[1]] = player
            return
        while True:
            myKey = read_key()
            for i in range(len(self.key)):
                for j in range(len(self.key[1])):
                    if myKey == self.key[i][j] and self.table[i][j] == 0:
                        self.table[i][j] = player
                        return
    
    def check(self):
        win = [0 for i in range(8)]
        for i in range(3):
            if 1 in self.table[i] and 2 in self.table[i]:
                win[i] = -1
            elif 0 in self.table[i]:
                pass
            else:
                win[i] = self.table[i][0]
        
        for i in range(3):
            if 1 in [self.table[j][i] for j in range(3)] and 2 in [self.table[j][i] for j in range(3)]:
                win[i + 3] = -1
            elif 0 in [self.table[j][i] for j in range(3)]:
                pass
            else:
                win[i + 3] = self.table[0][i]
        
        for i in range(2):
            if 1 in [self.table[j][(2 - j) * i - j * (i - 1)] for j in range(3)] and 2 in [self.table[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
                win[i + 6] = -1
            elif 0 in [self.table[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
                pass
            else:
                win[i + 6] = self.table[0][i * 2]
        
        if 1 in win:
            return 1
        if 2 in win:
            return 2
        if not 0 in win:
            return -1
        return 0

    def dangerCase(self):
        for i in range(3):
            if self.table[i].count(1) >= 2:
                for j in range(3):
                    if self.table[i][j] == 0:
                        return i,j
        for i in range(3):
            if [self.table[j][i] for j in range(3)].count(1) >= 2:
                for j in range(3):
                    if self.table[j][i] == 0:
                        return j,i
        for i in range(2):
            if [self.table[j][(2 - j) * i - j * (i - 1)] for j in range(3)].count(1) >= 2:
                for j in range(3):
                    if self.table[j][(2 - j) * i - j * (i - 1)] == 0:
                        return j,(2 - j) * i - j * (i - 1)

        i,j = randint(0,2),randint(0,2)
        while not self.table[i][j] == 0:
            i,j = randint(0,2),randint(0,2)
        return i,j
