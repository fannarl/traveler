# A prime number is a whole number greater than 1 whose only factors are 1 and itself.
# Write a program using a while statement, that given an int as the input, prints out "Prime" if the int is a prime number, 
# otherwise it prints "!Prime".

n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
count = 1
i = 0
prime = 0

while count <= n:
    if n % count == 0:
        i += 1
    count += 1
if i == 2:
    prime = 1


# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("!Prime")
