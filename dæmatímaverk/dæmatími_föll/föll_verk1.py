# find_min function definition goes here
def find_min(x, y):
    if x <= y:
        return x
    else:
        return y
        


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

minimum = find_min(first, second)
# Call the function here
print("Minimum: ", minimum)