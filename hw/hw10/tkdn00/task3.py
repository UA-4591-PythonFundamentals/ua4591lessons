# TASK3
from pprint import pprint

class Employee():
    counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def employee_counter(self):
        print(Employee.counter)

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


a = Employee("Jack", 1000)
a.display()
a.employee_counter()

b = Employee("Taras", 1000)
b.display()
a.employee_counter()

pprint(Employee.__doc__)
pprint(Employee.__name__)
pprint(Employee.__base__)
pprint(Employee.__dict__)
pprint(Employee.__module__)