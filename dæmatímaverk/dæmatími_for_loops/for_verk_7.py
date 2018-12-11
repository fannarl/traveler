top_num = int(input("Input a number between 0 and 999: "))
for i in range(0, top_num):
    pow_of_num = 0
    sum_of_num = 0
    num = str(i)   
    for n in range(0, len(num)):
        pow_of_num = len(num)
        sum_of_num += int(num[n]) ** pow_of_num
    if sum_of_num == i:
        print(sum_of_num)

