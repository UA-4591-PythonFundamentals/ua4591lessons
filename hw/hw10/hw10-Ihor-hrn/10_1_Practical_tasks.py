"""Task1"""

# class Polygon:
#     pass

# class Rectangle(Polygon):
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width

#     def rect_sq(self):
#         return self.width * self.height


# rect = Rectangle(5,6)
# print(rect.rect_sq())
# ================================================

"""Task2"""

# class Human:
#     def __init__(self, name):
#         self.name = name

#     def greetings(self):
#         return f"Hello, {self.name}!"
    
#     @classmethod
#     def homo_info(cls):
#         return "Human species is Homosapiens."
    
#     @staticmethod
#     def something():
#         return "An arbitrary message that is not tied to either an object or a class."
    

# pers = Human('Ihor')
# print(pers.greetings())
# print(Human.homo_info())
# print(Human.something())
# ================================================

"""Task3"""

# class Employee:
#     """Class for representing an employee."""
#     employees = []
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.employees.append(self)

#     def count_employee(self):
#         return len(Employee.employees)
    
#     def employee_info(self):
#         return f"Employee name: {self.name}, Employee salary: {self.salary}"
    
# worker1 = Employee('John', 2500)
# worker2 = Employee("Eve", 3000)
# print(worker1.count_employee())
# print(worker2.count_employee())
# print(worker2.employee_info())
# print(Employee.employees[0].employee_info())
# print(Employee.__base__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__doc__)
