from random import randint
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.build() 
        
    def build(self):
        suits = ['♥', '♦', '♣', '♠']
        card_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for s in suits:
            for v in card_value:
                self.cards.append(Card(v, s))
    
    def show(self):
        for c in self.cards:
            c.show()


    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r =  randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def drawCard(self):
        return self.cards.pop()
            


