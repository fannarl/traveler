top_num = int(input("Upper number for the range: ")) # Do not change this line


for i in range(1 , top_num + 1):
    divisor = 1
    sum_of_divisor = 0
    while divisor < i:
        if(i % divisor == 0):
            sum_of_divisor += divisor
        divisor += 1
    if(sum_of_divisor == i):
        print(i)    
        

