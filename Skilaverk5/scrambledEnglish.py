# This program will take all the letters in the middle of the string and keep the first and last letter the same    #
# but shuffle the middle part for example the word "letter" could be "lteter". It has two functions to do it.       #
# get_word_string will take the input and check if it is a file and then read it and move it into a string.         #
# the function scramble_string will take all words longer than 3 and shuffle the middle part of it.                 #
#####################################################################################################################
import random 
import string

str_punctuation = string.punctuation
status = True
def get_word_string(dataFile):
# checks if its a valid file name and then moves its contents to a string
    try:
        dataFile = open(filename, "r")
        word_string = ""
        for line in dataFile:
            word_string += line.replace('\n',' ')
        return word_string
    except FileNotFoundError:
        print("File " + dataFile + " not found")


def scramble_string(w_string):
    try:
        not_scrambled = w_string.split(" ")
        n_scrambled = []
        for i in not_scrambled:
            punct_check = []
            if len(i) >= 4:
                punct_check.append(i[-1])
# if the last part of a word is a punctuation like "help." than the first letter is "h" and last is "p" by shifting by 
# having the split for the middle variable be -2 instead of -1
                if punct_check[0] in str_punctuation:
                    first, middle, last = i[0],i[1:-2],i[-2:]
                    middle = list(middle)
                    random.shuffle(middle)
                    n_scrambled.append(first + "".join(middle) + last)
# Similar to the if statement except for that since the word does not contain a punctuation in the end it will have the shift
# be -1
                else:
                    first, middle, last = i[0],i[1:-1],i[-1]
                    middle = list(middle)
                    random.shuffle(middle)
                    n_scrambled.append(first + "".join(middle) + last)
# else if the letter is less than 4 characters we wont shuffle it and just append it to the list immiediatly
            else:
                n_scrambled.append(i)
        return ' '.join(n_scrambled)
    except AttributeError:
        return ""
# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)