# Create a program that lets the user input an integer, lets call it size. This integer should denote the size of a list. 
# Next you should let the user input size many values to a list. 
# Next you should create a list that has all the same values as the initial list except with no duplicates. 
# You can solve this with built in functions but I recommend trying to solve this without using builtin functions as well (excluding .append()).

size = int(input('Input size: '))
arr = []
unique_array = []
for i in range(size):
    arr.append(int(input('Enter value {0}: '.format(i + 1))))

for i in arr:
    found = False
    for j in unique_array:
        if j == i:
            found = True
    if not found:
        unique_array.append(i)
print('The list: ', end='')
print(arr)
print('The list with no duplicates: ', end='')
print(unique_array)