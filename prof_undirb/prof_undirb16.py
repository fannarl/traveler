# Skrifið Python forrit sem biður notandann að slá inn nafn skrár sem inniheldur eitt orð/tóka í línu með auðri línu á milli setninga.  
# Forritið prentar út lengsta orðið í skránni ásamt lengd þess.  
# Ef inntaksskrá finnst ekki þá skal fallið open_file skila None og aðalforritið prentar þá út viðeigandi villuskilaboð. 
# Aðal forritið er gefið og því má EKKI breyta.

def get_file_name():
    file_name = input('File name: ')
    return file_name

def get_longest_word(file_stream):   
    longest_word = ''
    for word in file_stream:
        word = word.strip()
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def open_file(file_name):
    file_stream = open(file_name, 'r')
    return file_stream

def main():
    file_name = get_file_name()
    try:
        file_stream = open_file(file_name)
        longest_word = get_longest_word(file_stream)
        print('Longest word is \'{0}\'  of length {1}'.format(longest_word, len(longest_word)))
        file_stream.close()
    except Exception:
        print("File {0} not found!".format(file_name))


main()