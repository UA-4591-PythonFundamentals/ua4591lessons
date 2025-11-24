class Employee:
    '''This class count the number of employees and 
    show information about each of them'''
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
    
    def show_counter(self):
        print(f"The total number of emploees is {Employee.counter}")

    def show_info(self):
        print(f"Employee name is {self.name}, \nEmployee salary is {self.salary}")

adam = Employee("Adam", 2000)
adam.show_counter()
adam.show_info()

eva = Employee("Eva", 2500)
eva.show_counter()
eva.show_info()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)