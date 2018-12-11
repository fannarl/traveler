class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    # def __repr__(self):
    #     return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # def __str__(self):
    #     return '{} - {}'.format(self.fullname(), self.email)
    
    # def __add__(self, other):
    #     return self.pay + other.pay

    # def __len__(self):
    #     return len(self.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(issubclass(Manager, Developer))

# print(isinstance(mgr_1, Developer))


# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)

# mgr_1.print_emp()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.email)
# print(dev_2.email)

# print(len(emp_1))


# print(emp_1 + emp_2)


# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))