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
    pygame = (question("Do you want to play with pygame ?", ["Yes","No"]) - 1) * -1
    bot = (bot == 1)
    pygame = (pygame == 1)
    return bot, pygame

def gameplay(parameters):
    bot = parameters[0]
    pygame = parameters[1]
    Plateau = Table(bot, pygame)
    player = randint(1,2)
    playerStr = str(player).replace("1", "X").replace("2", "O")
    Plateau.printTable("Turn to player: " + playerStr)
    while True:
        # cls()
        Plateau.modify(player)
        player %= 2
        player += 1
        playerStr = str(player).replace("1", "X").replace("2", "O")
        check = Plateau.check(player)
        Plateau.printTable("Turn to player: " + playerStr)
        if check == -1:
            Plateau.printTable("Equality")
            Plateau.quitPygame()
            return question("Play again ?", ["Yes", "Yes, but with other parameters", "No, back to the menu"])
        elif check != 0:
            Plateau.printTable("Player " + str(check).replace("1", "X").replace("2", "O") + " Win")
            Plateau.quitPygame()
            return question("Play again ?", ["Yes", "Yes, but with other parameters", "No, back to the menu"])

class Table:
    table = [[0 for i in range(3)] for j in range(3)]
    def __init__(self, bot = False, pygame = False, key = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]):
        self.bot = bot
        self.key = key
        self.pygame = pygame
        if pygame:
            init()
            self.ecran = display.set_mode((600,700))
            display.set_caption('Morpion pas dans le calfrock mon copain' )
            self.lignes = [
                ((200,100),(200,700)),
                ((400,100),(400,700)),
                ((0,300),(600,300)),
                ((0,500),(600,500))
            ]
        self.connection = -1
        self.connections = [(100,200), (500,200), (100, 600), (500, 600)]
    
    def printTable(self, message = ''):
        if self.pygame:
            self.printPygame(message)
        else:
            self.printConsole(message)
    
    def printPygame(self, message = ''):
        self.ecran.fill((240,240,240))
        draw.rect(self.ecran, (0,0,0), ((0, 0), (600, 100)))
        text = font.Font('freesansbold.ttf', 50).render(message, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (300, 50)
        self.ecran.blit(text, textRect)
        for ligne in self.lignes :
            draw.line(self.ecran, (0,0,0), ligne[0], ligne[1], 10)
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                x = i * 200
                y = j * 200 + 100
                if self.table[i][j] == 1:
                    draw.line(self.ecran, (255, 0, 0), (x+20,y+180), (x+180,y+20), 15)
                    draw.line(self.ecran, (255, 0, 0), (x+20,y+20), (x+180,y+180), 15)
                elif self.table[i][j] == 2:
                    draw.ellipse(self.ecran, (0, 0, 255), (x+20, y+20, 160, 160), 10)
        
        if self.connection == 7:
            draw.line(self.ecran, (0, 255, 0), (self.connections[1][0] + 50, self.connections[1][1] - 50), (self.connections[2][0] - 50, self.connections[2][1] + 50), 20)
        elif self.connection == 6:
            draw.line(self.ecran, (0, 255, 0), (self.connections[0][0] - 50, self.connections[0][1] - 50), (self.connections[3][0] + 50, self.connections[3][1] + 50), 20)
        elif self.connection >=3:
            draw.line(self.ecran, (0, 255, 0), (self.connections[0][0] - 50, self.connections[0][1] + (self.connection - 3) * 200), (self.connections[1][0] + 50, self.connections[1][1] + (self.connection - 3) * 200), 10)
        elif self.connection >=0:
            draw.line(self.ecran, (0, 255, 0), (self.connections[0][0] + (self.connection) * 200, self.connections[0][1] - 50), (self.connections[-2][0] + (self.connection) * 200, self.connections[-2][1] + 50), 10)

        display.update()

    def printConsole(self, message = ''):
        text = ''
        for i in range(len(self.table)):
            k = ""
            for j in self.table[i]:
                k += " " + str(j).replace("1", "X").replace("2", "O").replace("0", " ") + " |"
            text += k[0:-1]
            if i != 2: text += "\n---+---+---\n"
        print(message + "\n" + text)
    
    def modify(self, player):
        if self.bot and player == 2:
            coord = self.dangerCase()
            self.table[coord[0]][coord[1]] = player
            return
        while True:
            if self.pygame:
                for even in event.get():
                    if even.type == MOUSEBUTTONUP and (even.pos[1]-100) // 200>=0:
                        x, y = even.pos[0] // 200, (even.pos[1]-100) // 200
                        if self.table[x][y] == 0:
                            self.table[x][y] = player
                            return
                    elif even.type == QUIT: 
                        exit()
            else:
                myKey = read_key()
                for i in range(len(self.key)):
                    for j in range(len(self.key[1])):
                        if myKey == self.key[i][j] and self.table[i][j] == 0:
                            self.table[i][j] = player
                            return
    
    def check(self, player, Plato = None):
        if Plato == None:
            Plateau = self.table
        else:
            Plateau = Plato

        number = 0
        for i in range(len(Plateau)):
            for j in range(len(Plateau[i])):
                if Plateau[i][j] == 0:
                    number += 1
                    zero = [i,j]
        
        if number == 1:
            Plateau[zero[0]][zero[1]] = player

        win = [0 for i in range(8)]
        for i in range(3):
            if 1 in Plateau[i] and 2 in Plateau[i]:
                win[i] = -1
            elif 0 in Plateau[i]:
                pass
            else:
                win[i] = Plateau[i][0]
                self.connection = i
        
        for i in range(3):
            if 1 in [Plateau[j][i] for j in range(3)] and 2 in [Plateau[j][i] for j in range(3)]:
                win[i + 3] = -1
            elif 0 in [Plateau[j][i] for j in range(3)]:
                pass
            else:
                win[i + 3] = Plateau[0][i]
                self.connection = i + 3
        
        for i in range(2):
            if 1 in [Plateau[j][(2 - j) * i - j * (i - 1)] for j in range(3)] and 2 in [Plateau[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
                win[i + 6] = -1
            elif 0 in [Plateau[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
                pass
            else:
                win[i + 6] = Plateau[0][i * 2]
                self.connection = i + 6
        
        if 1 in win:
            return 1
        if 2 in win:
            return 2
        if not 0 in win:
            return -1
        return 0

    def dangerCase(self):
        for k in [2,1]:
            for i in range(3):
                if self.table[i].count(k) >= 2:
                    for j in range(3):
                        if self.table[i][j] == 0:
                            return i,j
            for i in range(3):
                if [self.table[j][i] for j in range(3)].count(k) >= 2:
                    for j in range(3):
                        if self.table[j][i] == 0:
                            return j,i
            for i in range(2):
                if [self.table[j][(2 - j) * i - j * (i - 1)] for j in range(3)].count(k) >= 2:
                    for j in range(3):
                        if self.table[j][(2 - j) * i - j * (i - 1)] == 0:
                            return j,(2 - j) * i - j * (i - 1)
        
        coor = testBot(self.table)
        i, j = coor[0], coor[1]
        return i,j
    
    def quitPygame(self):
        if self.pygame:
            while True:
                for even in event.get():
                    if even.type == MOUSEBUTTONUP:
                        quit()
                        return
                    elif even.type == QUIT: 
                        exit()


def testBot(Plateau, Players = None):
    if Players == None:
        Player = 2
    else:
        Player = Players
    
    proba = [[0 for j in range(3)] for i in range(3)]

    for i in range(3):
        for j in range(3):
            if Plateau[i][j] == 0:
                tempPlateau = Plateau
                tempPlateau[i][j] = Player
                check = Table().check((Player % 2)+1, tempPlateau)
                if check == 0:
                    proba[i][j] = testBot(tempPlateau, (Player % 2)+1)
                elif check == -1 or check == 2:
                    proba[i][j] = 1
                elif check == 1:
                    proba[i][j] = 0
    
    if Players == None:
        better = []
        betterStat = 0
        for i in range(3):
            for j in range(3):
                if proba[i][j] > betterStat:
                    better = [[i, j]]
                    betterStat = proba[i][j]
                elif proba[i][j] == betterStat:
                    better.append([i, j])
        return choice(better)
    else:
        return sum([sum(proba[i]) for i in range(len(proba))]) / 9