class Employee():
    """Information about empoyees"""

    total_number = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_number+=1

    @classmethod
    def info_total_number(cls):
        print (f"The total number of employees is {cls.total_number}")

    def info(self):
        """Displays the information about employee."""
        print(f"Employee name: {self.name}, salary: {self.salary:.2f}" )


emp1 = Employee(name="Frank Ocean", salary=10000)
emp1.info()
Employee.info_total_number()

emp2 = Employee(name="Mark Lord", salary=11000)
emp3 = Employee(name="Bred Pitt", salary=17000)
Employee.info_total_number()

print("\n\tTHIS IS THE ADDITIONAL INFO")
print(f"\nThe base classes from which the employee class is inherited: {Employee.__bases__}")
print(f"\nThe class namespace: {Employee.__dict__}")
print(f"\nThe class name: {Employee.__name__}")
print(f"\nThe module name: {Employee.__module__}")
print(f"\nThe documentation bar: {Employee.__doc__}")