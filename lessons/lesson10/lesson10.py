# list 
# print(list, type(list))
# l = [1, 2, 3]
# print(l, type(l))

# class MyFirstClass:

#     """This is my first class"""
#     pass

# print(MyFirstClass, type(MyFirstClass))
# obj = MyFirstClass()
# print(obj, type(obj))

# class Person:
#     a = 10
#     def print_info(self):
#         print("This is a person class")

# p = Person()
# p.print_info()
# print(p.a, type(p.a))
# print(p.print_info, type(p.print_info))
# f = p.print_info
# f()
# f2 = Person.print_info
# f2("asda")
# print(f2, type(f2))

# def func1(a):
#     print("This is func1")

# Person.f1 = func1
# p.f1()

# class Person:
#     cm = ["Class variable"]
#     ci = "Class variable"
#     def __init__(self, n=1):
#         print("This is init method", self.__dict__)
#         self.im = ["Instance variable"]*n
#         self.ii = "Instance variable"*n
#         print("After init", self.__dict__)

#     def print_info(self):
#         print(f"cm: {self.cm}, ci: {self.ci} ii: {self.ii}, im: {self.im}")
# p1 = Person()
# p2 = Person(2)
# p1.print_info()
# p2.print_info()

# Person.cm.append("New class var")
# Person.ci = "Modified class variable"
# p1.im.append("New instance var for p1")
# p2.ii = "Modified instance variable for p2"
# p1.print_info()
# p2.print_info()
# print(dir(p2))
# print(p2.__dict__)
# print(Person.__dict__)
# p2.cm.append("Added via p2")
# p2.ci = "Modified via p2"

# print()
# p1.print_info()
# p2.print_info()
# print(p1.__dict__)
# print(p2.__dict__)

# from pprint import pprint
# from re import U

# class Point:

#     # def __new__(cls, *args, **kwargs):
#     #     print("Creating instance of", cls)
#     #     print("This is new method")
#     #     instance = super().__new__(cls)
#     #     return instance
#     def __init__(self, x=0, y=0):
#         print("This is init method")
#         self.x = x
#         self.y = y
#         print("After init:", self.__dict__)
#     def __del__(self):
#         print("Deleting instance", self)
#     def print_info(s):
#         print(f"Point({s.x}, {s.y})")
#     def distance_to_zero(self):
#         return (self.x**2 + self.y**2)**0.5
    
# # p1 = Point(3, 4)
# # p2 = Point()
# # p3 = Point(6, 8)
# # p1.print_info()
# # p2.print_info()
# # p3.print_info()
# # f = Point.print_info
# # # f() #TypeError: Point.print_info() missing 1 required positional argument: 'self'
# # f(p1)
# # print(p1.__dict__)
# # pprint(Point.__dict__)
# # def create_point(x, y):
# #     return Point(x, y)
# # print("Creating point using factory function")
# # create_point(1, 2)
# # print("Creating point using direct call")
# # print("Creating point using factory function")
# # pp = create_point(11, 21)
# # print("Creating point using direct call")
# # print("dell")
# # del pp
# # #

# # p = Point(3, 4)

# class UserClass:
#     count = 0
#     users = []
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#         UserClass.count += 1
#         UserClass.users.append(self)
#     def __repr__(self):
#         return f"{self.name}/{self.email}/{self.age}"
#     def __del__(self):
#         UserClass.count -= 1
#         UserClass.users.remove(self)
#         print(f"User {self.name} deleted")
#     def __eq__(self, value):
#         return (self.name == value.name and
#                 self.email == value.email and
#                 self.age == value.age)  
#     def print_info(self, tab=0):
#         print(f"{'\t' * tab}Name: {self.name}, Email: {self.email}, Age: {self.age}")
    
#     @classmethod
#     def print_class_info(cls):
#         print(f"Total users: {cls.count}")
#         for user in cls.users:
#             user.print_info(1)

#     @staticmethod
#     def static_method_example():
#         print("This is a static method")


# def generate_users(n=5):
#     users = []
#     from random import randint, choice
#     names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"]
#     domains = ["example.com", "mail.com", "test.org", "demo.net"]
#     while n > 0:
#         name = choice(names)
#         email = f"{name.lower()}{randint(1,100)}@{choice(domains)}"
#         age = randint(18, 60)
#         u = UserClass(name, email, age)
#         if age % 2 == 0:
#             users.append(u)
#             n -= 1
#         else:
#             print(f"User {name} with age {age} not added (age not even) {u}")
#             del u
#     return users
# user = UserClass("Alice", "alice@example.com", 30)
# # user.print_info()

# # UserClass.print_class_info()
# # user.print_class_info()

# users = generate_users(10)
# UserClass.print_class_info()
# print(users)


# class EncapsulationExample:
#     def __init__(self, value):
#         self.__private_var = value
#         self._protected_var = value * 2
#         self.public_var = value * 3
#     def __str__(self):
#         return (f"Private: {self.__private_var}, "
#                 f"Protected: {self._protected_var}, "
#                 f"Public: {self.public_var}")
    
#     def get_private_var(self):
#         print(f"Getting private var {self.__private_var}")
#         return self.__private_var
#     def set_private_var(self, value):
#         print(f"Setting private var from {self.__private_var} to {value}")
#         if value < 0:
#             print("Value cannot be negative")
#             return
#         self.__private_var = value

#     private_var = property(get_private_var, set_private_var)

#     @property
#     def protected_var(self):
#         print(f"Getting protected var {self._protected_var}")
#         return self._protected_var
#     @protected_var.setter
#     def protected_var(self, value):
#         print(f"Setting protected var from {self._protected_var} to {value}")
#         self._protected_var = value
# obj = EncapsulationExample(5)
# print(obj)
# print(obj.public_var)
# print(obj._protected_var)
# print(obj._EncapsulationExample__private_var)
# obj.set_private_var(20)
# print(obj.get_private_var())

# obj.private_var = -10
# print(obj.private_var)
# obj.private_var = 15
# print(obj.private_var)
# obj.protected_var = 50
# print(obj.protected_var)
# print(obj)


class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
class Fish(Animal):
    def speak(self):
        print("Fish blubs")
    def speak(self, volume=1):
        print("Fish blubs" + "!" * volume)

animals = [Dog(), Cat(), Fish()]
for animal in animals:
    animal.speak()