# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character 
# are same from a given list of strings. Go to the editor 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

arr = input("Input a comma seperated list: ").split(',')

def match_words(arr):
    count = 0

    for word in arr:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1
    return count

print(match_words(arr))