import string   
sentence = input("Input a sentence: ")

# Here you should add the missing part
unique_letters = []
not_allowed = string.punctuation + string.whitespace

for i in sentence[::]:
    if i not in unique_letters and i not in not_allowed:
        unique_letters.append(i)

print("Unique letters:", unique_letters)
