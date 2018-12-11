class Card(object):
    def __init__(self, __rank = 0, __suit = ''):
        if type(__rank) is int and __rank > 0 and __rank < 14:
            if __rank == 1:
                self.rank = 'A'
            elif __rank == 11:
                self.rank = 'J'
            elif __rank == 12:
                self.rank = 'Q'
            elif __rank == 13:
                self.rank = 'K'
            else:
                self.rank = __rank
            
        elif type(__rank) is str and len(__rank) == 'AJQKajqk':
            self.rank = __rank.upper()
        else:
            self.rank = 0
        if type(__suit) is str and len(__suit) == 1 and __suit in 'HSDChsdc':
            self.suit = __suit.upper()
        else:
            self.suit = ''

    def __str__(self):
        if self.is_blank():
            return 'blk'
        else:
            return '{0:>3}{1}'.format(self.rank, self.suit)

    def is_blank(self):
        return self.rank == 0 or self.suit == ''
