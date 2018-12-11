# Write a Python program that reads a file named words.txt containing one word/token per line with an empty line between sentences.  The program prints out the longest word found in the file along with its length.
 
# Example output:
# Longest word is 'innflutningstollum' of length 18
 
# The first few lines from words.txt looks like this:

def find_longest_word():
    text = open("words.txt", "r")
    long_w = ""
    long_w_len = 0
    for line in text:
        if len(line) > len(long_w):
            long_w = line
            long_w_len = len(long_w) - 1
            long_w = line.strip()
    print("Longest word is " + "'" + long_w + "'" + " of length " + str(long_w_len) )
    return long_w

find_longest_word()