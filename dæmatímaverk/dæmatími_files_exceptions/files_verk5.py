# Write a Python program that reads a file named words.txt containing one word/token per line with an empty line between sentences  #
# and writes out one sentence per line into a file called sentences.txt.                                                            #
# The program should also print out (to the screen) each sentence.                                                                  #
# It is ok to have one space between the end of a sentence (e.g. period) and the last word.                                         #
#####################################################################################################################################

with open("dæmatímaverk/dæmatími_files_exceptions/words.txt", "r") as words:
    with open("dæmatímaverk/dæmatími_files_exceptions/sentances.txt", "w") as sentances:
            line = words.read()
            line = line.replace("\n", " ")
            line = line.replace("  ", " \n")
            sentances.write(line)
            print(line)