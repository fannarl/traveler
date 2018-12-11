a = int(input("Input the first integer: ")) # Do not change this line
b = int(input("Input the second integer: ")) # Do not change this line

for i in range(1, b+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)