# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

color = input("Input a comma seperated list: ").split(',')

color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]

print(color)