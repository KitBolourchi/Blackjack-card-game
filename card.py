class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    

    def show(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘') 
        # print(f'{self.value} of {self.suit}')

    def getValue(self):
        return self.value





