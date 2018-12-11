word_str = ""
vowels_str = "aeiouy"
consonant_str = ""
firstLetter_str = ""
vowel = 0

while word_str != ".":
    length_int = 0
    consonant_str = ""   
    word_str = input("Enter a word: ")
    firstLetter_str = word_str[0]
    vowel = 0
    if word_str == ".":
        break
    #Ef að fyrsti stafurinn er vowel prenta "yay" aftast
    for i in vowels_str:
        if word_str[0] == i:
            print(word_str + "yay")
            vowel = 1
            firstLetter_str = i
            break
    if vowel == 0:
    #Ef að fyrsti stafurinn er ekki vowel safna öllum stöfum fyrir aftan fyrsta
    #vowel og henda því fyrir aftan það og prenta "ay" aftast
        for n in word_str:
            if ((n != "a") and (n != "e") and (n != "i") and (n != "o") and (n != "u") and (n != "y")):
                consonant_str = consonant_str + n
            else:
                break
        length_int = len(consonant_str)
        lengt_word = len(word_str)
        word_str_length = word_str[length_int:]

        print(word_str_length + consonant_str+ "ay")
        

            
            
           