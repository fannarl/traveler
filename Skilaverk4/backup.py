import random 
import string

str_punctuation = (",",".")

def get_word_string(dataFile):
    dataFile = open(filename, "r")
    word_string = ""
    for line in dataFile:
        word_string += line.replace('\n',"")
    return word_string

def scramble_string(w_string):
    not_scrambled = w_string.split(" ")
    wordString = ""
    n_scrambled = []
    for i in not_scrambled:
        punct_check = []
        if len(i) >= 4:
            punct_check.append(i[-1])
            if punct_check[0] in str_punctuation:
                first, middle, last = i[0],i[1:-2],i[-2:]
                middle = list(middle)
                random.shuffle(middle)
                n_scrambled.append(first + "".join(middle) + last)
            else:
                first, middle, last = i[0],i[1:-1],i[-1]
                middle = list(middle)
                random.shuffle(middle)
                n_scrambled.append(first + "".join(middle) + last)
        else:
            n_scrambled.append
    return n_scrambled
        

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)





import random 
import string

str_punctuation = string.punctuation

def get_word_string(dataFile):
    dataFile = open(filename, "r")
    word_string = ""
    for line in dataFile:
        word_string += line.replace('\n',"")
    return word_string

def scramble_string(w_string):
    w_string.replace("\n", "")
    not_scrambled = w_string.split(" ")
    n_scrambled = []
    for scramble in not_scrambled:
        if len(scramble) >= 4:
            if scramble in str_punctuation:
                n_scrambled.append(scramble[0:-1])               
            else:
                first, middle, last = scramble[0], scramble[1:-1], scramble[-1]
                middle = list(middle)
                random.shuffle(middle)
                n_scrambled.append(first + "".join(middle) + last)
        else:
            n_scrambled.append(scramble)
    return ' '.join(n_scrambled)

            
# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)