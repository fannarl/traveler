from card import Card

class PlayingHand(object):
    NUMBER_CARDS = 13

    def __init__(self):
        self.cards = []
        for i in range(PlayingHand.NUMBER_CARDS):
            self.cards.append(Card())

    def __str__(self):
        result = ''
        for i in range(PlayingHand.NUMBER_CARDS):
            result += '{0}'.format(str(self.cards[i]))
        result += '\n'
        return result

    def add_card(self, card):
        for i in range(PlayingHand.NUMBER_CARDS):
            if self.cards[i].is_blank():
                self.cards[i] = card
                return