class MyString():
    def __init__(self, string):
        self.string = len(string)
    
    def __gt__(self, Last_string):
        if self.string > Last_string.string:
            return True
        else:
            return False

    def __sub__(self, Last_string):
        obj = Last_string - self.string
        return abs(obj)

obj1 = MyString('this is a string')
obj2 = MyString('this is another one')
print(obj1 > obj2)
print(obj1-obj2)
