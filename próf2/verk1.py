# Function definitions start here
def open_file(dataFile):
    try:
        dataFile = open(filename, "r")
        word_string = ""
        for line in dataFile:
            word_string += line.replace('\n',' ')
        return word_string
    except FileNotFoundError:
        print("File " + dataFile + " not found") 

def get_longest_word(str_inp):
    list_inp = []
    list_inp.append(str_inp)
    longest_word
    
    for i in list_inp:
        if len(i[0]) > 

    

# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close()
else:
	print('File',filename,'not found!')