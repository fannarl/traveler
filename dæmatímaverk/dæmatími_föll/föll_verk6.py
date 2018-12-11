# Your function definition goes here
def fibo(int_range):
    n1 = 0
    n2 = 1
    count = 0

    while count <= n - 1:
        if int_range <= 0:
            print("please enter a positive integer")
        #elif int_range == 1:
            #print(n1)
        else:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count = count + 1
            print(n1,end=" ")
        



n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here        
fibo(n)