n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below

count = 1
i = 0
prime = 0

while count <= n:
    if n % count == 0:
        i = i + 1
    count = count + 1
if i == 2:
    prime = 1
# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("!Prime")