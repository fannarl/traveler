import string
str_punct = string.punctuation

continues = False
t_o_f = False

def file_list(filename):
    result = []
    try:
        file_stream = open(filename)
        word_string = ""
        for line in file_stream:
            if line == "<NEW DOCUMENT>\n":
                result.append(word_string)
                word_string = ""
            word_string += line.replace('<NEW DOCUMENT>','')
        result.append(word_string)
        try:
            result.remove('')
        except ValueError:
            pass
        t_o_f = True
    except FileNotFoundError:
        print("Documents not found")
        t_o_f = False
    return t_o_f, result
    
def word_list_to_dict(doc_list):
    word_dict = {}
    list_of_docs = []
    count = 0
    for doc in doc_list:
        words = doc_list[count]
        word = words.split()
        list_of_words = []
        for index in word:
            string = str(index)
            string = string.strip(str_punct).lower()
            list_of_words.append(string)
        list_of_docs.append(list_of_words)
        count += 1
    count = 0
    for ls in list_of_docs:
        for word in ls:
            if word in word_dict:
                word_dict[word].add(count)
            else:
                word_dict[word] = set([count])
        count += 1
    return word_dict

def search(doc_list):
    search_list = []
    a_list = []
    b_list = []
    c_list = []
    count = 0
    search_list = input("Enter search words: ").split()
    doc_dict = word_list_to_dict(doc_list)
    for item in search_list:
        if search_list[count] in doc_dict:
            value = doc_dict.get(search_list[count])
            a_list.append(value)
        count += 1
    for ls in a_list:
        for item in ls:
            b_list.append(item)
    for item in b_list:
        if b_list.count(item) == len(a_list):
            c_list.append(item)
    if not b_list:
        print("No match.")
    else:
        Documents_search = set(c_list)
        Documents_search = str(Documents_search).strip(str_punct).replace(", ", " ")
        print("Documents that fit search: " + Documents_search)

def print_list(doc_list):
    try:
        doc_numb = int(input("Enter document number: "))
        print("Document #" + str(doc_numb))
        print(doc_list[doc_numb])
    except IndexError:
        print("Invalid document number")
    except ValueError:
        print("Invalid Input number")

def quit_program():
    continues = True
    print("Exiting program.")
    return continues

def choice():
    continues = False
    while continues is not True:
        u_input = input("What would you like to do?\n1. Search Documents\n2. Print Document\n3. Quit Program\n> ")
        if u_input == "1":
            search(doc_list)
        elif u_input == "2":
            print_list(doc_list)
        else:
            print("Exiting program.")
            continues = True
            
#  Main program starts here
#while t_o_f is not True:
filename = input("Document collection: ")
t_o_f, doc_list = file_list(filename)
if t_o_f == True:
    choice()
else:
    pass