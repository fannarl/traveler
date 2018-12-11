from card import Card
import random

class Deck(object):
    def __init__(self):
        self.cards = []
        for i in range(1, 14):
            for a in 'SHDC':
                self.cards.append(Card(i, a))

    def __str__(self):
        result = ''
        for i in range(4):
            for j in range(13):
                index = (i * 13) + j
                if index >= len(self.cards):
                    return result
                result += '{0}'.format(str(self.cards[index]))
            result += '\n'
        return result

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        result = self.cards[0]
        self.cards = self.cards
        return result