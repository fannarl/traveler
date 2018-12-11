# The function definition goes here
def in_range(num_input):
        if num_input <= 1:
            print(str(num_input) + " is outside the range!")
        elif num_input >= 555:
            print(str(num_input) + " is outside the range!")
        else:
            print(str(num_input) + " is in range!")

num = int(input("Enter a number: "))

in_range(num)
# You call the function here