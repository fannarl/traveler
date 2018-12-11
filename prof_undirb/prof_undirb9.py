# Create a program that lets the user input an integer, lets call it size. This integer should denote the size of a list. 
# Next you should let the user input size many values to a list. Next the program should print the sum of all the values in the list. 
# You can solve this with built in functions but I recommend trying to solve this without using builtin functions as well (excluding .append()).

size = int(input('Input size: '))
arr = []
for i in range(size):
    arr.append(int(input('Enter value {0}: '.format(i + 1))))

total = 0

for i in arr:
    total += i

print('{0} is the total.'.format(total))