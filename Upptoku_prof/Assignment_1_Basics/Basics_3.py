import math
# You likely learned the Euclidean distance formula in high school -- the formula to find the distance between two points in a plane.  
# You will take the two coordinates as input and output the distance between them.
# Hint: You can use the sqrt function in the math module.

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

# convert strings to ints

x1_int = int(x1_str)
y1_int = int(y1_str)
x2_int = int(x2_str)
y2_int = int(y2_str)

#  d =
d = math.sqrt(pow((x1_int - x2_int), 2) + pow((y1_int - y2_int), 2))
print('d = ',d)