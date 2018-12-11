def to_list(inp):
    inp = inp.replace(" ",",")
    inp_out = inp.split(",")
    return inp_out

# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)