"""
This game will be Blackjack with betting implemeted

Me vs dealer

Rules
: each player given two cards (faceup), m
: Dealer has one card face up and one card face down
: with your two cards, either 'hit' for another card, or stand to lock in your cards
: Aim is to get to 21 or as close as possible
: If you go above 21 then you are out
: winner is either closest to or on 21
"""
from deck import Deck
from player import Player
from card import Card


class Blackjack():
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    def play(self):
        p_status = self.player.draw(self.deck)
        d_status = self.dealer.draw(self.deck)

        self.player.showHand()

        if p_status == 1:
            print('Player has got a BlackJack!!')
            
            if d_status == 1:
                print('Dealer has BlackJack also! it is a tie')
            return 1
        
        if self.player.getScore() > 21:
            print('Player has gone bust')
            return 1

        cmd = ''
        while cmd != 'Stand':
            bust = 0
            cmd = input(f'You currently have {self.player.getScore()} will you HIT, or will your STAND? ')
            
            if cmd == 'Hit':
                bust = self.player.hit(self.deck)
                self.player.showHand()

            if bust == 1:
                    print(f'You scored {self.player.getScore()} Player has gone bust!')
                    return 1
            
        
        self.dealer.showHand()
        while self.dealer.getScore() < self.player.getScore() and self.dealer.getScore() < 21:
            self.dealer.hit(self.deck)
            
            if self.dealer.getScore() == 21:
                print(f'Dealer has a score of {self.dealer.getScore()}, dealer has got Blackjack')
                return 1
            
            elif self.dealer.getScore() > 21:
                print(f'Dealer has scored {self.dealer.getScore()}, dealer has gone bust')
                return 1
        
        if self.player.getScore() == self.dealer.getScore():
            print(f'Dealer scored {self.dealer.getScore()}, It is a tie')

        elif self.player.getScore() > self.dealer.getScore():
            print(f'Dealer scored {self.dealer.getScore()}, Player wins')
        
        elif self.player.getScore() < self.dealer.getScore():
            print(f'Dealer scored {self.dealer.getScore()}, Dealer has won')
        


b = Blackjack()
b.play()
