class Employee:
    
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def print_count(self):
        print(f"Total number of employees: {Employee.emp_count}")

    def print_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


emp1 = Employee("Slavik", 5000)
emp2 = Employee("Viacheslav", 7000)

emp1.print_employee()
emp2.print_employee()
emp1.print_count()

print(f"Employee.__base__: {Employee.__base__}")
print(f"Employee.__dict__: {Employee.__dict__}")
print(f"Employee.__name__: {Employee.__name__}")
print(f"Employee.__module__: {Employee.__module__}")
print(f"Employee.__doc__: {Employee.__doc__}")