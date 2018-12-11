def get_word_list(fpointer):
    word_string = ""
    for line in fpointer:
        word_string += line
    word_string = word_string.split('\n')
    return word_string


def main():
    a_dict = {}
    filename = input("Enter name of file: ")
    fpointer = open(filename)
    word_list = get_word_list(fpointer)
    print(word_list)

main()