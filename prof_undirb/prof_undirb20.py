from order import Order
#from order_line import OrderLine

def main():
    order = Order()
    order.addLine("eggs", 60, 12, 0)
    order.addLine("bread", 200, 1, 10)
    order.addLine("milk", 120, 2, 5)
    total, _, _ = order.getTotals()
    print("The total price is: {0:.0f}".format(total))
    print(order)

main()