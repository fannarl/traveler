# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) : 
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = int(input("Input a number "))
d = dict()

for i in range(1, 1+n):
    d[i] = i*i

print(d)