from pprint import pprint

class Employees:
    employees_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employees.employees_count += 1

    @classmethod
    def total_number(cls):
        return f"The total number of employees: {cls.employees_count}"
    
    def employees_info(self):
        return f"Employee {self.name} has a salary of ${self.salary}."
    

person1 = Employees("Andrea Sachs", 8000)
person2 = Employees("Anya Forger", 9500)
person3 = Employees("Kirigaya Kazuto", 8700)
person4 = Employees("Joel Miller", 7800)
person5 = Employees("Yami Sukehiro", 9000)


print(person1.employees_info())
print(person2.employees_info())
print(person3.employees_info())
print(person4.employees_info())
print(person5.employees_info())
print(Employees.total_number())

print(f"Base: {Employees.__base__}")
print(f"Name: {Employees.__name__}")
print(f"Module: {Employees.__module__}")
print(f"Doc: {Employees.__doc__}")
pprint(Employees.__dict__)
