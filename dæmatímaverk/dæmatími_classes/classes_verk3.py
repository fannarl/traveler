class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def get_first_word(self):
        words = self.sentence.split()
        return str(words[0])

    def get_all_words(self):
        self.all_words = self.sentence
        return self.all_words.split()
    
    def replace(self, index, new_word):
        try:
            word_list = self.sentence.split()
            word_list[index] = new_word
            self.sentence = word_list
            self.sentence = " ".join(self.sentence)
            return self.sentence
        except IndexError:
            pass


    
sent = Sentence('This is a test')
print(sent.get_first_word())
#assert str(sent.get_first_word()) == "This"

print(sent.get_all_words())
#assert sent.get_all_words() == 'This is a test'.split()

sent.replace(3, "must")
print(sent.get_all_words())
#assert sent.get_all_words() == 'This is a must'.split()