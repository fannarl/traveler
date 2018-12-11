import string
# Your function definition goes here
def count_case(string_input):
    upper_count = 0
    lower_count = 0
    for i in string_input:
        if(i.islower()):
            lower_count = lower_count + 1
        elif(i.isupper()):
            upper_count = upper_count + 1
    return upper_count, lower_count
    

user_input = input("Enter a string: ")

# Call the function here
upper, lower = count_case(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)