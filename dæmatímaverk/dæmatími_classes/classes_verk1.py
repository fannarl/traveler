class Student():
    def __init__(self, score=10):
        self.score = score

    
    def __str__(self):
        return str(self.score)
    
    def add_score(self):
        self.score += 10

    def decrease_score(self):
        self.score -= 10

    
p = Student()
print(p)
p.add_score()
print(p)
p.decrease_score()
print(p)