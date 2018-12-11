# Create a program that lets the user input an integer, lets call it size. 
# This integer should denote the size of a list. Next you should let the user input size many values to a list. 
# Next you should print the content of the list.

size = int(input('Input size: '))

arr = []
for i in range(size):
    arr.append(int(input('Enter value {0}:'.format(i + 1))))

print(arr)