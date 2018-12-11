# Input a six-digit integer.
# Assign first_three (int) to be the first three digits.
# Assign last_two (int) to be the last two digits.
# Assign middle_two (int) to be the middlt two digits.
# Print out the three values.
# Hint: use quotient (//) and remainder (%)
# For example, if the input is 123456
# The first three digits: 123
# The last two digits: 56
# The middle two digits: 34

x_str = input('Input x: ')
# remember to convert to an int
x_int = int(x_str)
# first_three =
first_three = x_int // 1000
# last_two =
last_two = x_int % 100
# middle_two =
middle_two = (x_int // 100) % 100

print('Original input: ' + x_str)
print('First three:', first_three)
print('Last two:', last_two)
print('Middle two:', middle_two)