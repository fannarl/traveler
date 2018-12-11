# Create a program that lets the user input an integer, lets call it size. 
# This integer should denote the size of a list. Next you should let the user input size many values to a list. 
# Next you should let the user input a value, lets call it target. Next you should count how often the value target occurs in the list. 
# Next the program should print how many times the value target occurs in the list. 
# You can solve this with built in functions but I recommend trying to solve this without using builtin functions as well (excluding .append()).


size = int(input('Input size: '))
arr = []
for i in range(size):
    arr.append(int(input('Enter value {0}: '.format(i + 1))))

target = int(input('Input target: '))

found = 0
for i in arr:
    if target == i:
        found += 1

print('{0} is {1} times in the list.'.format(target, found))
