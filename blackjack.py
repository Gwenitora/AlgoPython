from library import *

def play():
    playing = 1
    while playing == 1:
        parameters = parameter()
        playing = 0
        while playing == 0:
            gameplay(parameters)
            playing = question("Play again ?", ["Yes", "Yes, but with other parameters", "No, back to the menu"])

def parameter():
    return question('Numbers of paquets (8 by default):', 'input int', 8)

def gameplay(parameters):
    cards = Card(parameters)

    playerPoint = []
    playerCards = []
    for i in range(2):
        draw = cards.draw()
        playerPoint.append(draw[0])
        playerCards.append(draw[1])
    dealerPoint = []
    dealerCards = []
    for i in range(2):
        draw = cards.draw()
        dealerPoint.append(draw[0])
        dealerCards.append(draw[1])
    while True:
        reply = ['hit', 'stand', 'double']
        if len(playerCards)==2 and playerPoint[0]==playerPoint[1]:
            reply.append('split')
        play = question('Your cards\n    ' + printList(playerCards, False, False) + '\n\n' + 'Dealer cards\n    ' + printList(dealerCards[:-1], False, False) + ', hide\n\n' + 'Your points: ' + str(sum(playerPoint)) + '\n' + 'Dealer points: ' + str(dealerPoint[0]) + '\n', reply)
        if play==0:
            draw = cards.draw()
            playerPoint.append(draw[0])
            playerCards.append(draw[1])
        elif play==1:
            break
    question('', 'empty noClear')

class Card:
    def __init__(self, numbers:int = 8) -> None:
        special = ['V', 'D', 'R', 'A']
        symbol = ['♥', '♦', '♠', '♣']
        self.cards = []
        for n in range(numbers):
            for i in range(1, 14):
                for j in symbol:
                    number = i
                    text = str(i)
                    if i==1:
                        number = 11
                        text = special[-1]
                    elif i>10:
                        number = 10
                        text = special[i%11]
                    self.cards.append([number, text + j])

    def draw(self) -> list:
        if self.cards == []:
            return False
        choose = choice(self.cards)
        self.cards.remove(choose)
        return choose

play()