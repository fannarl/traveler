def main():
    p = float(50)
    loan = float(input('Input the cost of the item in $:'))
    interest_r = interest_rate(loan)
    payements(p, loan, interest_r)

def interest_rate(loan):
    interest_r = 0
    if loan <= 1000:
        interest_r = float(0.015)
    else:
        interest_r = float(0.02)
    return interest_r


def payements(p, loan, interest_r):
    interest_p = 0
    ammount_of_payments = 0
    total_interest_p = 0
    while loan > 0:
        interest_p = loan * interest_r
        if p < loan:
            loan = loan - (p - interest_p)
        elif p >= loan:
            p = loan + interest_p
            loan = loan - p
            loan = float(0)

        ammount_of_payments += 1
        total_interest_p += interest_p
        print("Month:", ammount_of_payments, "Payment:", round((p), 2) ,  "Interest paid:" , round((interest_p), 2) , "Remaining debt:" ,round((loan), 2))
    print("")
    print("Number of months:" , ammount_of_payments)
    print("Total interest paid:", round((total_interest_p), 2))

main()