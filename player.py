from card import Card
from deck import Deck


class Player():
    def __init__(self, isDealer, deck):
        self.hand = []
        self.score = 0
        self.isDealer = isDealer
        self.deck = deck
    
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        self.hand.append(deck.drawCard())
        self.getScore()
        if self.score == 21:
            return 1
        else:
            return 0
    
    def hit(self, deck):
        self.hand.append(deck.drawCard())
        self.getScore()
        if self.score > 21:
            return 1
        else:
            return 0
    
    def showHand(self):
        for c in self.hand:
            c.show()
    
    def getScore(self):
        self.score = 0
        for c in self.hand:
            self.score += c.getValue()
        return self.score
