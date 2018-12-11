import string

upperCase_int = 0
lowerCase_int = 0
digits_int = 0
punctuation_int = 0
punct_str = string.punctuation

sentance_str = input("Enter a sentence: ")

for i in sentance_str: 
    if(i.islower()):
        lowerCase_int = lowerCase_int + 1
    elif(i.isupper()):
        upperCase_int = upperCase_int + 1
    elif(i.isdigit()):
        digits_int = digits_int + 1
    for n in punct_str:
        if (i == n):
            punctuation_int = punctuation_int + 1


print('{:>15s} {:>5d}'.format('Upper case', upperCase_int))
print('{:>15s} {:>5d}'.format('Lower case', lowerCase_int))
print('{:>15s} {:>5d}'.format('Digits', digits_int))
print('{:>15s} {:>5d}'.format('Punctuation', punctuation_int))
