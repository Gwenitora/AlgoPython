from library import *
#definir la fonction play sans parametre 
def play():
    #initialisé playing egal a 1 
    playing = 1
    #tant que playeing est equivalent a 1
    while playing == 1:
        #initialisé parameters egal a la fonction parameter sans parametre 
        parameters = parameter()
        #initialisé playing egal a 0 
        playing = 0
        #tant que playing est equivalent a 0 
        while playing == 0:
            #initialiser playing a la fonction gameplay de parametre parameters 
            playing = gameplay(parameters)

# definir la fonction parameter sans parametre
def parameter():
    # initialiser bot egal a a la fonction question de parametre ("Do you want to play with a bot ?", ["Yes","No"], 1) moins un, le tout multiplié par moins 1
    bot = (question("Do you want to play with a bot ?", ["Yes","No"], 1) - 1) * -1
    # initialisé pygame egal a la fonction question de parametre ("Do you want to play with pygame ?", ["Yes","No"]) moins un, le tout multiplié par moins un 
    pygame = (question("Do you want to play with pygame ?", ["Yes","No"]) - 1) * -1
    # initialiser bot a l'assertion bot equivalent a 1
    bot = (bot == 1)
    # initialiser pygame a l'assertion pygame equivalent a 1
    pygame = (pygame == 1)
    #retourner bot, pygame
    return bot, pygame

# definir la fonction gameplay de parametre parameters
def gameplay(parameters):
    #initialisé bot egal a l'indice zero de parameters
    bot = parameters[0]
    # initialisé pygame egal a l'inidice 1 de parameters
    pygame = parameters[1]
    # initialisé plateau egal a la class Table de parametre bot, pygame
    Plateau = Table(bot, pygame)
    # initialisé player egal a la fonction randint de parametre 1 et 2
    player = randint(1,2)
    #initialisé playerStr de parametre str(player).replace("1", "X").replace("2", "O")
    playerStr = str(player).replace("1", "X").replace("2", "O")
    #appeler la fonction printTable de Plateau de parametre ("Turn to player: " + playerStr)
    Plateau.printTable("Turn to player: " + playerStr)
    # tant que True 
    while True:
        # cls()
        # appeler la fonction modify dans Plateau de parametre player
        Plateau.modify(player)
        # initialiser modulo player egal a 2 
        player %= 2
        # initialiser zell en compteur plus 1 
        player += 1
        # initialisé playerStr egal str(player).replace("1", "X").replace("2", "O")
        playerStr = str(player).replace("1", "X").replace("2", "O")
        # initialiser check egal a la fonction check dans Plateau de parametre (player)
        check = Plateau.check(player)
        #appeler la fonction printTable de parametre ("Turn to player: " + playerStr) dans Plateau
        Plateau.printTable("Turn to player: " + playerStr)
        #si check equivalent a -1 
        if check == -1:
            #Alors appeler la fonction print table de parametre ("Equality", True)
            Plateau.printTable("Equality", True)
            #retourner la fonction question de parametre ("Play again ?", ["Yes", "Yes, but with other parameters", "No, back to the menu"])
            return question("Play again ?", ["Yes", "Yes, but with other parameters", "No, back to the menu"])
        # sinon si check est different de 0
        elif check != 0:
            #appeler la fonction printTable de parametre ("Player " + str(check).replace("1", "X").replace("2", "O") + " Win", True)
            Plateau.printTable("Player " + str(check).replace("1", "X").replace("2", "O") + " Win", True)
            # retourner la fonction question de parametre ("Play again ?", ["Yes", "Yes, but with other parameters", "No, back to the menu"])
            return question("Play again ?", ["Yes", "Yes, but with other parameters", "No, back to the menu"])

# definir une class Table
class Table:
    # definir une fonction __init__ de parametre (self, bot, pygame, key = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]], keyPygame = [[K_KP7, K_KP8, K_KP9], [K_KP4, K_KP5, K_KP6], [K_KP1, K_KP2, K_KP3]])
    def __init__(self, bot, pygame, key = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]], keyPygame = [[K_KP7, K_KP8, K_KP9], [K_KP4, K_KP5, K_KP6], [K_KP1, K_KP2, K_KP3]]):
        # initialiser self.table egal au parcours de la table par trois a l'horizontal et 3 a la vertical 
        self.table = [[0 for i in range(3)] for j in range(3)]
        # initialiser self.bot egal a bot 
        self.bot = bot
        # initialiser self.key egal a key 
        self.key = key
        # initialiser self.pygame egal pygame
        self.pygame = pygame
        # si pygame
        if pygame:
            # Alors self.keyPygame egal a keyPygame
            self.keyPygame = keyPygame
            # appeler al fonction init sans parametre 
            init()
            # initialiser self.ecran egal a la creation d'une fenetre de parametre 600, 700 
            self.ecran = display.set_mode((600,700))
            # donner un titre a cette fenetre 'Morpion pas dans le calfrock mon copain'
            display.set_caption('Morpion pas dans le calfrock mon copain' )
            #initialiser self.lignes a cette table [((200,100),(200,700)),((400,100),(400,700)),((0,300),(600,300)),((0,500),(600,500))
            self.lignes = [
                ((200,100),(200,700)),
                ((400,100),(400,700)),
                ((0,300),(600,300)),
                ((0,500),(600,500))
            ]
        # initialiser self.connection egal a -1
        self.connection = -1
        # initialiser self.connection egal a [(100,200), (500,200), (100, 600), (500, 600)]
        self.connections = [(100,200), (500,200), (100, 600), (500, 600)]
    
    # definir printTable de parametre (self, message = '', valid = False)
    def printTable(self, message = '', valid = False):
        # si self.pygame 
        if self.pygame:
            # alors appeler self.printPygame de parametre message
            self.printPygame(message)
            # si valid
            if valid:
                # tant que K_RETURN ou K_KP_ENTER n'est pas pressé 
                while not(key.get_pressed()[K_RETURN] or key.get_pressed()[K_KP_ENTER]):
                    # pour tout les even dans event.get()
                    for even in event.get():
                        # si even.type equivalent mousebuttonup
                        if even.type == MOUSEBUTTONUP:
                            #appeler la fonction quit sans parametre 
                            quit()
                            # retourner
                            return
                        # sinon si even.type equivalent a QUIT
                        elif even.type == QUIT: 
                            #Appeler la fonction exit sans parametre
                            exit()
                # appeler la fonction quit sans parametre
                quit()
        # sinon 
        else:
            # appaler la fonction self.printConsole de parametre message
            self.printConsole(message)
            # si valid 
            if valid:
                # tant que la fonction de parametre pressed n'est pas:
                while not(is_pressed('enter')):
                    # pass
                    pass
    
    # definir la fonction printPygame de parametre (self, message = '')
    def printPygame(self, message = ''):
        # donner une couleur grise a la fenetre 
        self.ecran.fill((240,240,240))
        # definir un rectangle noir dans la fenetrede parametre a la position 600,100
        draw.rect(self.ecran, (0,0,0), ((0, 0), (600, 100)))
        #initialiser text egal a un font d'epaisseur 50 de couleur blanche 
        text = font.Font('freesansbold.ttf', 50).render(message, True, (255, 255, 255))
        # initialiser textRect egal a l'appel de la fonction text.get_rect
        textRect = text.get_rect()
        #initialiser textRect.center egal a la position (300,50)
        textRect.center = (300, 50)
        # appeler la fonction self.ecran.blit de parametre text, textRect
        self.ecran.blit(text, textRect)
        # pour tout ligne dans self.lignes 
        for ligne in self.lignes :
            # dessiner de couleur noir les element d'indice 0 et d'indice 1 d'epaisseur 10 dans la liste self.ecran
            draw.line(self.ecran, (0,0,0), ligne[0], ligne[1], 10)
        # pour tout i dans le parcour de self.table
        for i in range(len(self.table)):
            # pour tout j dans le parcour des index de self.table
            for j in range(len(self.table[i])):
                # initialiser x egal a i multiplié par 200 
                x = i * 200
                # initialiser y = a j multiplié par 200 plus 100
                y = j * 200 + 100
                # si les indice i et j de self.table equivalent a 1 
                if self.table[i][j] == 1:
                    #dessiner une ligne rouge de position x+20, y+180 et x+180, y+20 d'epaisseur 15 
                    draw.line(self.ecran, (255, 0, 0), (x+20,y+180), (x+180,y+20), 15)
                    #dessiner une ligne rouge de position x+20, y+20 et x+180, y+180 d'epaisseur 15 
                    draw.line(self.ecran, (255, 0, 0), (x+20,y+20), (x+180,y+180), 15)
                # sinon si les indice i et j de self.table egal a 2 
                elif self.table[i][j] == 2:
                    # dessiner une elipse bleu de position x+20,y+20, 160 ,160 et d'epaisseur 10
                    draw.ellipse(self.ecran, (0, 0, 255), (x+20, y+20, 160, 160), 10)
        
        # si self.connection == 7
        if self.connection == 7:
            # dessiner une ligne de parametre (self.ecran, (0, 255, 0), (self.connections[1][0] + 50, self.connections[1][1] - 50), (self.connections[2][0] - 50, self.connections[2][1] + 50), 20)
            draw.line(self.ecran, (0, 255, 0), (self.connections[1][0] + 50, self.connections[1][1] - 50), (self.connections[2][0] - 50, self.connections[2][1] + 50), 20)
        # sinon si self.connection equivalent a 6
        elif self.connection == 6:
            # dessiner une ligne de parametre (self.ecran, (0, 255, 0), (self.connections[0][0] - 50, self.connections[0][1] - 50), (self.connections[3][0] + 50, self.connections[3][1] + 50), 20)
            draw.line(self.ecran, (0, 255, 0), (self.connections[0][0] - 50, self.connections[0][1] - 50), (self.connections[3][0] + 50, self.connections[3][1] + 50), 20)
        # sinon si self.connection superieur ou egal a 3
        elif self.connection >= 3:
            # dessiner une ligne de parametre (self.ecran, (0, 255, 0), (self.connections[0][0] - 50, self.connections[0][1] + (self.connection - 3) * 200), (self.connections[1][0] + 50, self.connections[1][1] + (self.connection - 3) * 200), 10)
            draw.line(self.ecran, (0, 255, 0), (self.connections[0][0] - 50, self.connections[0][1] + (self.connection - 3) * 200), (self.connections[1][0] + 50, self.connections[1][1] + (self.connection - 3) * 200), 10)
        # sinon si self.connection superieur ou egal a 0
        elif self.connection >=0:
            # dessiner une ligne de parametre (self.ecran, (0, 255, 0), (self.connections[0][0] + (self.connection) * 200, self.connections[0][1] - 50), (self.connections[-2][0] + (self.connection) * 200, self.connections[-2][1] + 50), 10)
            draw.line(self.ecran, (0, 255, 0), (self.connections[0][0] + (self.connection) * 200, self.connections[0][1] - 50), (self.connections[-2][0] + (self.connection) * 200, self.connections[-2][1] + 50), 10)
        #mettre a jour la fenetre
        display.update()

    # definir la fonction printConsole de parametre (self, message = '')
    def printConsole(self, message = ''):
        # initialiser text egal a ''
        text = ''
        # pour tout i dans le parcours de self.table
        for i in range(len(self.table)):
            # initialiser k egal a ""
            k = ""
            # pour tout j dans les indice de self.table
            for j in self.table[i]:
                # initialiser un compteur de k plus " " plus str(j).replace("1", "X").replace("2", "O").replace("0", " ") + " |"
                k += " " + str(j).replace("1", "X").replace("2", "O").replace("0", " ") + " |"
            #initialiser un compteur de text + k[0:-1]
            text += k[0:-1]
            # si i est different de 2 
            if i != 2: 
                # alors mettre un compteur de text + "\n---+---+---\n"
                text += "\n---+---+---\n"
        # imprimer (message + "\n" + text)
        print(message + "\n" + text)
    
    # definir une fonction modify de parametre sekf. player
    def modify(self, player):
        # si self.bot et player equivalent a 2 
        if self.bot and player == 2:
            # initialiser coor egal a self.dangerCase()
            coord = self.dangerCase()
            # initialiser self.table[coord[0]][coord[1]] egal a player 
            self.table[coord[0]][coord[1]] = player
            # retourner
            return
        # tant que True 
        while True:
            # si self.pygame
            if self.pygame:
                # pour tout even dans event.get
                for even in event.get():
                    # si even.type equivalent a la pression de clique gauche et si le clique s'effecture a partir de -100 en partant du haut
                    if even.type == MOUSEBUTTONUP and (even.pos[1]-100) // 200>=0:
                        # initialiser x,y egal a la position de even d'indice 0 divisé par 200 en renvoyent un entier
                        x, y = even.pos[0] // 200, (even.pos[1]-100) // 200
                        # si les indice x et y de self.table sont equivalent a 0 
                        if self.table[x][y] == 0:
                            # alors initialiser les indice x et y self.table egal a player 
                            self.table[x][y] = player
                            # retourner 
                            return
                    #sinon si event.type equivalent a QUIT        
                    elif even.type == QUIT:
                        # exit()
                        exit()
                # pour tout i dans le parcours self.keyPygame
                for i in range(len(self.keyPygame)):
                    # pour tout j dans le parcours de self.keyPygame[i]
                    for j in range(len(self.keyPygame[i])):
                        # si key.get_pressed [self.keyPygame[j][i]] and self.table[i][j] equivalent a 0 
                        if key.get_pressed()[self.keyPygame[j][i]] and self.table[i][j] == 0:
                            # initialiser les indice i et j de self.table egal a player 
                            self.table[i][j] = player
                            # retourner
                            return
            #sinon si 
            else:
                # initialiser myKey egal a la fonction read_key
                myKey = read_key()
                # pour tout i dans le parcours de self.key
                for i in range(len(self.key)):
                    # pour tout j dans le parcours des indice de self.key
                    for j in range(len(self.key[i])):
                        # si myKey equivalent au indice i et j de self.key et de self.table equivalent a 0
                        if myKey == self.key[i][j] and self.table[i][j] == 0:
                            # initialiser les indice i et j de self.table egal a player 
                            self.table[i][j] = player
                            # retourner
                            return
    # definir la fonction check de parametre self, player, Table = True
    def check(self, player, Table = True):
        
        # initialiser Bool egal a False
        Bool = False
        # si Table equivalent a True 
        if Table == True:
            # Table egal a deepcopy(self.table)
            Table = deepcopy(self.table)
            #initialiser Bool egal True
            Bool = True

        # initialiser number egal a 0
        number = 0
        # pour tout i dans le parcours de Table
        for i in range(len(Table)):
            # pourt tout j dans le parcours des indice de Table
            for j in range(len(Table[i])):
                # si les indice i et j de Table equivalent a 0
                if Table[i][j] == 0:
                    # Alors initialiser un compteur de number plus 1 
                    number += 1
                    # initialiser zero egal au indice i et j 
                    zero = [i,j]
        # si number equivalent a 1 
        if number == 1:
            # initialiser les indice zero 0 et zero 1 de Table egal a player
            Table[zero[0]][zero[1]] = player
        # initialiser connect = -1 
        connect = -1

        # initialiser win egal a  
        win = [0 for i in range(8)]
        # pour tout i dans le retour de l'execution de la fonction range de parametre 3
        for i in range(3):
            # si 1 dans l'indice de Table et 2 
            if 1 in Table[i] and 2 in Table[i]:
                #initialiser l'indice de win egal -1
                win[i] = -1
            # sinon si 0 dans l'indice de Table 
            elif 0 in Table[i]:
                # pass
                pass
            #sinon
            else:
                # initialiser l'indice de win egal a l'indice i et 0 de Table 
                win[i] = Table[i][0]
                # initialiser connect egal a i 
                connect = i
        # pour tout i dans le retour de l'execution de la fonction range de parametre 3 
        for i in range(3):
            # si 1 dans [Table[j][i] for j in range(3)] et 2 dans [Table[j][i] for j in range(3)]
            if 1 in [Table[j][i] for j in range(3)] and 2 in [Table[j][i] for j in range(3)]:
                # initialiser l'indice de win +3 egal a moins 1
                win[i + 3] = -1
            # sinon si 0 dans [Table[j][i] for j in range(3)]
            elif 0 in [Table[j][i] for j in range(3)]:
                # pass
                pass
            # sinon 
            else:
                #initialiser l'indice de win +3 egal au indice 0 et i de Table 
                win[i + 3] = Table[0][i]
                # initialiser connect egal i plus 3
                connect = i + 3
        
        # pour tout i dans le retour de l'execution de la fonction range de parametre 2 
        for i in range(2):
            # si 1 dans [Table[j][(2 - j) * i - j * (i - 1)] for j in range(3)] et 2 dans  [Table[j][(2 - j) * i - j * (i - 1)] for j in range(3)]
            if 1 in [Table[j][(2 - j) * i - j * (i - 1)] for j in range(3)] and 2 in [Table[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
                # Alors initialiser l'indice i+6 de win egal a -1
                win[i + 6] = -1
            # sinon si 0 dans [Table[j][(2 - j) * i - j * (i - 1)] for j in range(3)]
            elif 0 in [Table[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
                # pass
                pass
            # sinon 
            else:
                # initialisé l'indice i+6 de win egal a l'indice i multiplié par 2 de Table
                win[i + 6] = Table[0][i * 2]
                # initialiser connect egal a i plus 6
                connect = i + 6
        
        # si Bool
        if Bool:
            #initialiser self.connection egal a connect
            self.connection = connect

        # si 1 dans win 
        if 1 in win:
            # retourner 1
            return 1
        # si 2 dans win 
        if 2 in win:
            # retourner 2 
            return 2
        # si pas de 0 dans win
        if not 0 in win:
            # retourner moins 1 
            return -1
        # retourner 0
        return 0

    # definir une fonction dangerCase de parametre self
    def dangerCase(self):
        # pour tout k dans [2,1]
        for k in [2,1]:
            # pour tout i dans le retour de l'execution de la fonction range de parametre 3
            for i in range(3):
                # si le compte de k des indice de self.table sont superieur ou egal a 2 
                if self.table[i].count(k) >= 2:
                    # pour tout j dans le retour de l'execution de la fonction range de parametre 3
                    for j in range(3):
                        # si les indice i et j de  self.table sont equivalent a 0
                        if self.table[i][j] == 0:
                            # retourner i, j
                            return i,j
            # pour tout i dans le retour de l'execution de la fonction range de parametre 3
            for i in range(3):
                #si les indice i et j de self.table pour tout j dans le retour de l'execution de la fonction range de parametre 3 sont superieur ou egal a 2 
                if [self.table[j][i] for j in range(3)].count(k) >= 2:
                    # pour tout j dans le retour de l'execution de la fonction range de parametre 3 
                    for j in range(3):
                        # si les indice j et i sont equivalent a 0
                        if self.table[j][i] == 0:
                            # retourner j, i
                            return j,i
            # pour tout i dans le retour de l'execution de la fonction range de parametre 2 
            for i in range(2):
                # si le compte de l'element j dans self.table multiplié par (2 moins j) multiplié par i moins j multiplié par (i moins 1) pour tout j dans le retour de l'execution de la fonction 3 sont superieur ou egal a 2 
                if [self.table[j][(2 - j) * i - j * (i - 1)] for j in range(3)].count(k) >= 2:
                    # pour tout j dans le retour de l'execution de la fonction range de parametre 3 
                    for j in range(3):
                        # si l'element d'indice j dans self.table et l'element d'indice 2moinsj) multiplié par i - j multiplié par (i moins 1) equivalent 0 
                        if self.table[j][(2 - j) * i - j * (i - 1)] == 0:
                            # retourner j,(2 - j) * i - j * (i - 1)
                            return j,(2 - j) * i - j * (i - 1)
        
        # si self.table son equivalent a la table [[0,0,0],[0,0,0],[0,0,0]]
        if self.table == [[0,0,0],[0,0,0],[0,0,0]]:
            # retourner un chiffre entre 0 et 1 et un chiffre enter 0 et 1 multiplié par 2 
            return randint(0,1) * 2, randint(0,1) * 2

        # initialiser eval = self.minimax(deepcopy(self.table),2)
        eval = self.minimax(deepcopy(self.table), 2)
        # initialiser i, j = a l'index 1 dans la table eval, index2 de la table eval 
        i, j = eval[1], eval[2]
        
        # retourner i,j 
        return i,j

    # definir une fonction minimax de parametre self Tableau et Player 
    def minimax(self, Tableau, Player):
        # initialiser Table egal a la fonction deepcopy de parametre tableau
        Table = deepcopy(Tableau)

        # initialiser check egal a self.check(Player, deepcopy(table))
        check = self.check(Player, deepcopy(Table))
        # si check equivalent a -1 
        if check == -1: 
            # alors initialiser check egal a 1,5
            check = 1.5
        # si check superier a 0
        if check > 0:
            # retourner la table check
            return [check]
        # initialiser maxeval un float de parametre '-inf'
        maxeval = float('-inf')
        # initialiser mineval un float de parametre 'inf'
        mineval = float('inf')
        # initialoiser val egal a une table vide
        val = []
        
        # pour tout i dans le retour de l'execution de la fonction range de parametre 9
        for i in range(9):
            # si l'element i modulo 3 et i diviser par 3 retournant un entier de Table equivalent a 0 
            if Table[i % 3][i // 3] == 0:
                # initialiser Plate egal a la fonction deepcopy de parametre Table
                Plate = deepcopy(Table)
                # initialiser les element i modulo 3 et i divisé par 3 renvoyant un entier de Plate egal a player
                Plate[i % 3][i // 3] = Player

                # si Player equivalent a 2
                if Player == 2:
                    # eval egal a la fonction minimax de parametre Plate, 1
                    eval = self.minimax(Plate, 1)
                    # si l'element d'indice 0 superieur a maxeval 
                    if eval[0] > maxeval:
                        # alors initialiser val egal a une table vide
                        val = []
                    #initialiser maxeval egal a la fonction max de parametre maxeval , et eval d'indice 0    
                    maxeval = max(maxeval, eval[0])
                    # si l'element d'indice 0 dans eval equivalent a maxeval
                    if eval[0] == maxeval:
                        # Alors appeler la fonction append de parametre i%3, i//3 
                        val.append([i % 3, i // 3])

                #sinon si Player equivalent a 1
                elif Player == 1:
                    # initialiser eval egal a la fonction minimax de parametre plate, 2
                    eval = self.minimax(Plate, 2)
                    # initialiser mineval egal a la fonction min de parametre mineval, eval[0]
                    mineval = min(mineval, eval[0])
        
        # si Player equivalent 2 
        if Player == 2:
            # initialiser val egal a la fonction choice de parametre val 
            val = choice(val)
            # initialiser x, y egal a l'element d'indice 0 de val et l'element d'indice 1 de val
            x, y = val[0], val[1]
            # retourner maxeval,x ,y
            return maxeval, x, y
        # sinon si Player equivalent a 1 
        elif Player == 1:
            # retourner [mineval]
            return [mineval]