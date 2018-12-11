# Write a program that reads a file called 'test.txt' and prints out the contents on the screen after removing all spaces and newlines. Punctuations will be preserved.
 
# For example, if 'test.txt' contains:
# This is a test file, for chapter 06.
# This a new line in the file!
# Then, your program's output will show:
# Thisisatestfile,forchapter06.Thisanewlineinthefile!
# Hint:
# Consider using the strip() and replace() functions.
with open("dæmatímaverk/dæmatími_files_exceptions/test.txt", "r") as f:
    test = f.read()
    test = test.replace(" ", "")
    test = test.replace("\n", "")
    print(test,end="")
