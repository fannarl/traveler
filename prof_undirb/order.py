from order_line import OrderLine

class Order(object):
    def __init__(self):
        self.lines = []

    def __str__(self):
        result = 'Product   Price    Quantity    Discount\n'
        result += '=======================================\n'
        for line in self.lines:
            result += '{0}\n'.format(str(line))
        result += '=======================================\n'
        total, totalExcludingDiscount, discount = self.getTotals()
        result += 'Total excluding discount:{0:>22.0f}\n'.format(totalExcludingDiscount)
        result += 'Total discount:{0:>32.0f}\n'.format(discount)
        result += 'Total:{0:>41.0f}\n'.format(total)
        return result


    def addLine(self, name, price, number, discount):
        self.lines.append(OrderLine(name, price, number, discount))

    def getTotals(self):
        total_ex = 0
        total_disc = 0
        for line in self.lines:
            total_ex += line.price * line.number
            total_disc += line.price * line.number * (line.discount / 100)
        return (total_ex - total_disc, total_ex, total_disc)