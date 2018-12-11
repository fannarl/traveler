import string
import operator
from operator import itemgetter
str_punct = string.punctuation


# Main program starts here
def main():
    filename = input("Enter name of file: ")
    fpointer = open(filename)
    word_list = get_word_list(fpointer) 
    bi_dict = word_list_to_dict(word_list)
    word_count_tuples = dict_to_tuple(bi_dict)
    print(sorted(word_count_tuples,key=itemgetter(1),reverse = True)[:10])

def get_word_list(fpointer):
    word_string = ""
    for line in fpointer:
        word_string += line
        word_string = word_string.lower()
    word_string = word_string.split()
    word_string = [i.strip(str_punct) for i in word_string]
    return word_string

def word_list_to_dict(w_list):
    bigram_dict = {}
    previous_word = ''
    for word in w_list:
        if previous_word != '':
            #build bigram
            bigram = (previous_word, word)
            if bigram in bigram_dict:
                bigram_dict[bigram] += 1
            else:
                bigram_dict[bigram] = 1
        previous_word = word
    return bigram_dict

def word_list_to_counts(bigram_dict):
    word_count_dict = {}
    value = 1
    for bigram in bigram_dict:
        if bigram in word_count_dict:
            word_count_dict[bigram] += 1
        else:
            word_count_dict[bigram] = value
    return word_count_dict


def dict_to_tuple(list_to_tuple):
    dictlist = []
    for key, value in list_to_tuple.items():
        temp = (key,value)
        dictlist.append(temp)
    return dictlist

main()