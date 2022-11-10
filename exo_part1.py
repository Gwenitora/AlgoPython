from library import *
cls()

# # -------------------------------------------------------------------------------------------------
# # DEBUT

# r = 12000
# s = 1250
# e = 10
# rh = 230

# calcOne = ( (365 * 3) / (24 - (16 - 8)) ) * (rh) #=>    15740.625
# calcTwo = e * s #=>                                     12500

# assertionOne = calcOne > r #=>                          15740.625 > 12000 -> True
# assertionTwo = calcTwo < r #=>                          12500 < 12000 -> False
# assertionUn = assertionOne == assertionTwo #=>          True == False -> False

# # FIN
# # -------------------------------------------------------------------------------------------------
# # DEBUT

# r = 12000
# s = 1250
# e = 10
# rh = 230

# calcOne = (365 * 3) / (4 - (12 - 8)) * (rh) #=>         False
# calcTwo = e * s #=>                                     12500

# assertionOne = calcOne > r #=>                          False > 12000 -> False
# assertionTwo = calcTwo < r #=>                          12500 < 12000 -> False
# assertionUn = assertionOne == assertionTwo #=>          False == False -> True

# # FIN
# # -------------------------------------------------------------------------------------------------
# # DEBUT

# def returnSixPlusTrois():
#     return 6 + 3
# def returnSixPlusX(x):
#     return 6 + x

# print("Qui vole un " + str(returnSixPlusTrois()) + ", vole un boeuf")
# print("Qui vole un " + str(returnSixPlusX(3)) + ", vole un boeuf")

# # FIN
# # -------------------------------------------------------------------------------------------------
# # DEBUT

# def add(x, y):
#     return x+y
# def sub(x, y):
#     return x-y
# def mult(x, y):
#     return x*y
# def div(x, y):
#     try:
#         return x/y
#     except:
#         return None
# def mod(x, y):
#     try:
#         return x%y
#     except:
#         return None

# def calcSalaireBySeconde(salHour, daysOpen, hourByDay):
#     return (salHour * hourByDay * daysOpen) / (3600 * 24 * 365)

# def netSalaire(brut, coeff):
#     # Calculer et assigner multiplicateur du coeff
#     multiplicateurCoeff = 1 - coeff / 100
#     # Retrouner le salaire net
#     return brut * multiplicateurCoeff

# print(calcSalaireBySeconde(12000,235,8))

# # FIN
# # -------------------------------------------------------------------------------------------------
# # DEBUT

# def withdrawFees(total, taxes):
#     return total * (1 - taxes / 100)


# def netSalaire(brut, public):
#     if public:
#         return withdrawFees(brut, 15)
#     else:
#         return withdrawFees(brut, 23)

# salaire = 1000
# print("salaire net dans le public: " + str(netSalaire(salaire, True)))
# print("salaire net dans le privé: " + str(netSalaire(salaire, False)))

# # FIN
# # -------------------------------------------------------------------------------------------------
# # DEBUT

# def div(x, y):
#     try:
#         return x/y
#     except:
#         return None

# # FIN
# # -------------------------------------------------------------------------------------------------
# # DEBUT

# def game(char = "abcdefghijklmnopqrstuvwxyz"):

#     # Choisir un charactère dans la palette de charactères
#     char = choice(str(char)).lower()

#     # Initialisation du compteur de tour
#     count = 0

#     # Tant que le joueur ne donne pas le bon charactère, mettre une erreur, compter l'erreur et recommencer
#     while char != input("Enter a character: ").lower():
#         count += 1
#         print("wrong character, try again\n")

#     # Quand le joueur a mis le bon charactère, féliciter et finir
#     print("You have find the good character in " + str(count) + " try, GG\n")
#     return

# game('f')

# def gameRecursif(char = "abcdefghijklmnopqrstuvwxyz", count = 0):

#     # Choisir un caractère dans la palette de caractères
#     char = choice(str(char)).lower()

#     # Si le caractère choisis est bon, féliciter et finir
#     if char == input("Enter a character: ").lower():
#         print("You have find the good character in " + str(count) + " try, GG\n")
    
#     # Sinon mettre une erreur et recommencer avec le même caractère, mais compte une fois en plus
#     else:
#         print("wrong character, try again\n")
#         gameRecursif(char, count+1)
#     return

# gameRecursif('f')

# # FIN
# # -------------------------------------------------------------------------------------------------
# # DEBUT

# def comma(str1:str, str2:str)->str:
#     # Concatene les deux strings avec une virgule
#     return str1 + ',' + str2

# def indexs(tab:list, val)->str:
#     # Créer un texte vide qui contienderas les index
#     possibl = '|'
#     # Parcoure la liste
#     for i in range(len(tab)):
#         # Si la valeur parcouru de la liste est égale à la valeur ajouter, alors, concatener l'index
#         if tab[i]==val:
#             possibl += ", " + str(i)
#     # Retourner les index en str, et en enlevant la virgule au début
#     return possibl.replace("|, ", '').replace('|', "Null")

# print(indexs([0,1,1,1,0,1,1,0,1], 0))

# # FIN
# # -------------------------------------------------------------------------------------------------
# DEBUT

# def fibonacci(len:int, x:int = 1)->list:
#     fibo = [0, x]
#     for i in range(len - 2):
#         fibo.append(fibo[-1] + fibo[-2])
#     return fibo

# print(fibonacci(10))

def displayTab(tab:list):
    for i in tab:
        text = ''
        for j in i:
            text += str(j).replace('0',"□  ").replace('1',"■  ")
        print(text)
    print('')

def connwayBoardSystem(table:list, xY:list)->list:
    tableReturn = []
    for col in range(len(table)):
        for row in range(len(table[col])):
            if xY[0] == col and xY[1] == row:
                for i in range(-1,2):
                    for j in range(-1,2):
                        if (i != 0 or j != 0) and col-i >= 0 and row-j >= 0:
                            try:
                                tableReturn.append(table[col - i][row - j])
                            except:
                                pass
                return tableReturn


            # assertion = (col - 1 >= 0 )  ? " Vrai" : "Faux"
            # toto = col - 1 if (col - 1 >= 0 ) else Null

def connwayNewFrame(table:list)->list:
    tableTwo = [[0 for i in range(len(table))] for j in range(len(table))]
    for col in range(len(table)):
        for row in range(len(table)):
            tableTwo[col][row] = connwayBoardSystem(table, [col, row]).count(1)
    for col in range(len(table)):
        for row in range(len(table)):
            if tableTwo[col][row] == 3:
                table[col][row] = 1
            elif tableTwo[col][row] < 2 or tableTwo[col][row] > 3:
                table[col][row] = 0
    cls()
    displayTab(table)
    return table

def connway(table:list, frames:int = 0, speed:float = 0)->None:
    displayTab(table)
    if frames <= 0:
        while True:
            sleep(speed)
            table = connwayNewFrame(table)
    else:
        for i in range(frames):
            sleep(speed)
            table = connwayNewFrame(table)

def connwayWithLength(length:int, frames:int = 0, speed:float = 0)->None:
    connway([[randint(0,1) for i in range(length)] for j in range(length)], frames)

# connway([
#     [0,0,0],
#     [1,1,1],
#     [0,0,0]
# ], 20, 0.2)
# connway([
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,1,1,1,1,1,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0]
# ], 20, 0.2)

connwayWithLength(30)

# FIN
# -------------------------------------------------------------------------------------------------
# DEBUT



# FIN
# -------------------------------------------------------------------------------------------------
# DEBUT



# FIN