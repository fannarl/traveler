class OrderLine(object):
    def __init__(self, name, price, number, discount):
        self.name = name
        self.price = price
        self.number = number
        self.discount = discount

    def __str__(self):
        return "{0:<11}{1:<9}{2:<11}{3:<12}{4:<5}".format(self.name, self.price, self.number, self.discount, self.price * self.number)