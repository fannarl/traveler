n = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
count = 0
while count <= n:
    count = count + 1
    if n % count == 0:
        print(count)