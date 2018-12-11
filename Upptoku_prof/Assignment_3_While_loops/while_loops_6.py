# Write a program using a while statement, that prints out the two-digit number such that when you square it, 
# the resulting three-digit number has its rightmost two digits the same as the original two-digit number.  
# That is, for a number in the form AB:
# AB * AB = CAB, for some C. 

num = 10
sum_num = 0
while num < 100:
    sum_num = num * num
    if (sum_num % 100 == num) and (sum_num < 1000):
        print(num)
    num = num + 1
