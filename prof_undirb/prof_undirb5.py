# Create a program that lets the user input an integer, lets call it size. 
# This integer should denote the size of a list. Next you should let the user input size many values to a list. 
# Next you should let the user input a value, lets call it target. 
# If target is in the list the program should print “<target> is in the list“. 
# Otherwise it should print “<target> is not in the list“. 
# You can solve this with built in functions and the in operator but I recommend trying to solve this without using 
# builtin functions or the in operator as well (excluding .append()).

size = int(input('Input size: '))

arr = []
for i in range(size):
    arr.append(int(input('Enter value {0}: '.format(i + 1))))

target = int(input('Input target: '))
########################################################
# if target in arr:
#     print('{0} is in the list.').format(target))
# else:
#     print('{0} is not in the list.').format(target))
########################################################
found = False
for i in arr:
    if target == i:
        found = True

if found:
    print('{0} is in the list.'.format(target))
else:
    print('{0} is not in the list'.format(target))

