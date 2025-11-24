class Employee:
    """This clas creates an employee object and counts the number of employees"""
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @staticmethod
    def count_of_employees():
        return Employee.count

    def display_employee_info(self):
        return f'Employee {self.name}, salary {self.salary}'


if  __name__ == '__main__':
    employees = [Employee('John', 20000), Employee('Jane', 30000), Employee('Mary', 1000000), Employee('David', 50000),
                 Employee('Patrick', 40000)]

    print(Employee.count_of_employees())

    for employee in employees:
        print(employee.display_employee_info())

    print('------------------------------')
    print(Employee.__base__)
    print(Employee.__dict__)
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__doc__)
