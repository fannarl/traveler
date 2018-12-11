import string
# palindrome function definition goes here
def is_palindrome(str_input):
    special = string.whitespace + string.punctuation
    str_modif = str_input.lower()

    for char in str_modif:
        if char in special:
            str_modif = str_modif.replace(char,"")
    if str_modif == str_modif[::-1]:
        print("\"" + str_input + "\" is a palindrome.")
    else:
        print("\"" + str_input + "\" is not a palindrome.")
            


in_str = input("Enter a string: ")

# call the function and print out the appropriate message

is_palindrome(in_str)