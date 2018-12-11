import string
str_punct = string.punctuation

def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer) 
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))

def get_word_list(fpointer):
    word_string = ""
    for line in fpointer:
        word_string += line
        word_string = word_string.lower()
    word_string = word_string.split()
    word_string = [i.strip(str_punct) for i in word_string]
    return word_string

def word_list_to_counts(w_list):
    word_count_dict = {}
    for word in w_list:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict

def dict_to_tuple(list_to_tuple):
    dictlist = []
    for key, value in list_to_tuple.items():
        temp = (key,value)
        dictlist.append(temp)
    return dictlist

main()