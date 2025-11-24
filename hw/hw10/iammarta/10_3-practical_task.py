class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name         
        self.salary = salary  
        Employee.employee_count += 1

    @classmethod
    def print_total_employees(cls):
        print(f"Total number of employees: {cls.employee_count}")

    def print_info(self):
        print(f"Employee name: {self.name}, salary: {self.salary}")


# ----- EXAMPLE USAGE -----
emp1 = Employee("Marta Kozak", 5000)
emp2 = Employee("John Doe", 6000)

emp1.print_info()
emp2.print_info()

Employee.print_total_employees()

# ----- CLASS INFORMATION -----
print("Base classes (__base__):", Employee.__base__)
print("Class namespace (__dict__):", Employee.__dict__)
print("Class name (__name__):", Employee.__name__)
print("Module name (__module__):", Employee.__module__)
print("Documentation (__doc__):", Employee.__doc__)
