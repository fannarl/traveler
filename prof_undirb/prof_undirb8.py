# Create a program that lets the user input an integer, lets call it size. 
# This integer should denote the size of a list. Next you should let the user input size many values to a list. 
# Next the program should print the lowest value in the list. 
# You can solve this with built in functions but I recommend trying to solve this without using builtin functions as well (excluding .append()).

size = int(input('Input size: '))
arr = []
for i in range(size):
    arr.append(int(input('Enter value {0}: '.format(i + 1))))

highest = float("inf")

for i in range(len(arr)):
    if arr[i] < highest:
        highest = arr[i]

print('{0} is the lowest.'.format(highest))