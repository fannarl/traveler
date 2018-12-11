num = 10
sum_num = 0
while num < 100:
    sum_num = num * num
    if (sum_num % 100 == num) and (sum_num < 1000):
        print(num)
    num = num + 1
