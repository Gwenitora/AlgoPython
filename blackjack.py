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
    paquets = question('Numbers of paquets (8 by default):', 'input int', 8)
    return paquets, 

def gameplay(parameters):
    cards = Card(parameters[0])

    while len(cards.players) > 0:
        cards.update()
        reply = ['hit', 'stand', 'double']
        if len(cards.playerCards)==2 and (cards.playerPoint[0]==cards.playerPoint[1] or (cards.playerPoint[0] == 1 and cards.playerPoint[1] == 11) or (cards.playerPoint[0] == 11 and cards.playerPoint[1] == 1)):
            reply.append('split')
        if len(cards.players) > 1:
            reply.append('swap')
        play = question('Your cards\n    ' + printList(cards.playerCards, False, False) + '\n\nDealer cards\n    ' + printList(cards.dealerCards[:-1], False, False) + ', hide\n\nYour points: ' + str(sum(cards.playerPoint)) + '\nDealer points: ' + str(cards.dealerPoint[0]) + '\n', reply)
        if play==0:
            cards.hit()
        elif play==1:
            cards.stand()
        elif play==2:
            cards.double()
        elif play==3:
            cards.split()
        else:
            cards.swap()
    

    while sum(cards.dealerPoint) < 18:
        draw = cards.draw()
        cards.dealerPoint.append(draw[0])
        cards.dealerCards.append(draw[1])
        if sum(cards.dealerPoint) > 21:
            dealerPointReplace = replaceList(cards.dealerPoint, 11, 1)
            if not dealerPointReplace == False:
                cards.dealerPoint = dealerPointReplace
    question('Your cards\n    ' + printList(cards.playerCards, False, False) + '\n\nDealer cards\n    ' + printList(cards.dealerCards, False, False) + '\n\nYour points: ' + str(sum(cards.playerPoint)) + '\nDealer points: ' + str(sum(cards.dealerPoint)) + '\n', 'empty')

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
        
        self.playerPoint = []
        self.playerCards = []
        for i in range(2):
            draw = self.draw()
            self.playerPoint.append(draw[0])
            self.playerCards.append(draw[1])
        self.dealerPoint = []
        self.dealerCards = []
        for i in range(2):
            draw = self.draw()
            self.dealerPoint.append(draw[0])
            self.dealerCards.append(draw[1])
        self.players = [[]]
        self.standPlayer = []
        self.update()

    def draw(self) -> list:
        if self.cards == []:
            return False
        choose = choice(self.cards)
        self.cards.remove(choose)
        return choose
    
    def swap(self):
        self.update()
        temp = self.players[0]
        del self.players[0]
        self.players.append(temp)
        self.playerPoint, self.playerCards = self.players[0][0], self.players[0][1]
    
    def hit(self):
        draw = self.draw()
        self.playerPoint.append(draw[0])
        self.playerCards.append(draw[1])
        if sum(self.playerPoint) > 21:
            self.playerPointReplace = replaceList(self.playerPoint, 11, 1)
            if self.playerPointReplace == False:
                self.stand()
            else:
                self.playerPoint = self.playerPointReplace
    
    def stand(self):
        self.standPlayer.append(self.players[0])
        del self.players[0]
    
    def double(self):
        draw = self.draw()
        self.playerPoint.append(draw[0])
        self.playerCards.append(draw[1])
        if sum(self.playerPoint) > 21:
            self.playerPointReplace = replaceList(self.playerPoint, 11, 1)
            if not self.playerPointReplace == False:
                self.playerPoint = self.playerPointReplace
        self.stand()
    
    def split(self):
        draw = self.draw()
        self.players.append([[self.playerPoint[1], draw[0]], [self.playerCards[1], draw[1]]])
        draw = self.draw()
        self.playerPoint[1] = draw[0]
        self.playerCards[1] = draw[1]
        self.update()
    
    def update(self):
        self.players[0] = [self.playerPoint, self.playerCards]

play()