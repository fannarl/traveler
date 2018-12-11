class Student:
    def __init__(self, student_id, grades):
        self.__student_id = student_id
        self.__grades = grades
    
    def __str__(self):
        output = "Student ID: {}\nGrades: {}".format(self.__student_id, self.__grades)
        return output

    def __lt__(self, other):
        return True if self.get_average() < other.get_average() else False
    
    def get_average(self):
        return sum(self.__grades) / len(self.__grades)


def main():
    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    john = Student(student_id, grades)

    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    alice = Student(student_id, grades)

    print("John's info")
    print(john)

    if (john < alice):
        print("John has a lower average grade than Alice")
    else:
        print("Alice has a lower average grade than John")