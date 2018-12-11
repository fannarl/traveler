loan = float(input("Input the cost of the item in $: "))
interest_rate = float(1.5)

ammount_of_payments = 0
interest_rate = float(0)
remaining_dept = float(0)
total_interest_paid = float(0)

if loan < 1000:
    interest_rate = float(0.015)
else:
    interest_rate = float(0.02)

interest_paid = float(0)
payment = float(50)

while payment < loan:

    interest_paid = interest_rate  * loan
    loan = loan - (payment - interest_rate * loan)    
    remaining_dept = loan
    ammount_of_payments += 1
    total_interest_paid += interest_paid
    print("Month:", ammount_of_payments, "Payment:", round((payment), 2) ,  "Interest paid:" , round((interest_paid), 2) , "Remaining debt:" ,round((remaining_dept), 2))

    if payment >= loan:
        interest_paid = interest_rate * loan
        payment = remaining_dept + interest_paid
        loan = loan - payment
        ammount_of_payments += 1
        remaining_dept = 0.0
        total_interest_paid += interest_paid
        print("Month:", ammount_of_payments, "Payment:", round((payment), 2) ,  "Interest paid:" , round((interest_paid), 2) , "Remaining debt:" , round((remaining_dept), 2))
        break
print("")
print("Number of months:" , ammount_of_payments)
print("Total interest paid:", round((total_interest_paid), 2))