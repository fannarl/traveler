price_of_share = ""
a_first = 0
number_of_shares = 0
original_input_price = ""
a_first = ""
a_middle = ""
a_last = ""

def price(input_price):
    first , middle ,last = input_price.split(" ")
    first = int(first)
    middle = int(middle)
    last = int(last)
    num_div_den = middle / last
    a_total_price = first + num_div_den
    a_total_price = float(a_total_price) * number_of_shares
    a_total_price = format(a_total_price, ".2f")
    return a_total_price

shares_bool = False
while not shares_bool:
    try:
        number_of_shares = int(input("Enter number of shares: "))
    except ValueError:
        print("Invalid number!")
        continue
    price_bool = False
    while not price_bool:
# Split the price input and putting it in three variables to be used later
# use the function to check for the value
        try:
            price_of_share = input("Enter price (dollars, numerator, denominator): ")
            original_input_price = original_input_price + price_of_share
            price_of_share = price(price_of_share)
            price_bool = True
            a_first, a_middle, a_last = original_input_price.split(" ")
            print(str(number_of_shares) + " shares with market price " + a_first + " " + a_middle + "/" + a_last + " have value $" + price_of_share)
            a_continue = input("Continue: ")
            if a_continue == "n":
                shares_bool = True
            elif a_continue == "y":
                price_of_share = ""
                original_input_price = ""
                shares_bool = False
        except ValueError:
#If invalid reset the variables and go again
            print("Invalid price!")
            price_of_share = ""
            original_input_price = ""
            continue

