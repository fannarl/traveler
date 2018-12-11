import string
#build_wordlist() function goes here
str_punct = string.punctuation

def build_wordlist(file_stream):
    word_string = ""
    for line in file_stream:
        word_string += line.replace('\n',' ')
    word_string = word_string.split(' ')
    word_string = [i.strip(str_punct) for i in word_string]
    return word_string

#find_unique() function goes here
def find_unique(word_list):
    new_list = []
    for i in word_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

        
def main():
    infile = open("dæmatímaverk/dæmatími_more_func/test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()