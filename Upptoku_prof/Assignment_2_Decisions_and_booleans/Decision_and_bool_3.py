# Write a program that reads in 3 integers and prints out the maximum of the three.

num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

# Fill in the missing code below
if num2 < num1 > num3:
    max_int = num1
elif num1 < num2 > num3:
    max_int = num2
else:
    max_int = num3

print("The maximum is: ", max_int) # Do not change this line