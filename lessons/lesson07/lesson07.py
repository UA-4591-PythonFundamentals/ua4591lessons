

# def print_hello_world():
#     print("Hello, World!")
#     print("This is Lesson 07.")


# print(print_hello_world)
# f = print_hello_world
# print(f)
# f()
# print_hello_world()
# print_hello_world()

# def print_hello_world():
#     """Prints Hello, World! and a lesson message.
#         return: None
#     """
#     print("Hello, World!")
#     return 1
#     print("This is Lesson 07.")

# print()
# result = print_hello_world()
# print("The result of the function is:", result)
# print(print_hello_world.__doc__)
# help(print_hello_world)

# def print_info(name, age):
#     """Prints the name and age of a person.
#         name: str - The name of the person.
#         age: int - The age of the person.
#         return: str - A formatted string with the person's name and age.
#     """
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     return f"{name} is {age} years old.".upper()

# info = print_info("Alice", 30)
# print(info)
# info = print_info("Bob", 25)
# print(info)
# info = print_info("Charlie", 35)
# print(info)

# def absolute_value(num):
#     """Returns the absolute value of a number.
#         num: int or float - The number to get the absolute value of.
#         return: int or float - The absolute value of the number.
#     """
#     if num < 0:
#         return -num
#     else:
#         return num
#     print("This line will never be executed.")
# print(absolute_value(-10))
# print(absolute_value(5))

# def greet(name, age):
#     """Greets a person with their name and age.
#         name: str - The name of the person.
#         age: int - The age of the person.
#         return: str - A greeting message.
#     """
#     return f"Hello, {name}! You are {age} years old."

# # def greet(name: str, age: int) -> list:
# #     """Greets a person with their name and age.
# #         name: str - The name of the person.
# #         age: int - The age of the person.
# #         return: str - A greeting message.
# #     """
# #     return f"Hello, {name}! You are {age} years old."
# message = greet("Diana", 28)
# print(message)
# message = greet(28, "Diana")
# print(message)
# # greet() #TypeError: greet() missing 2 required positional arguments: 'name' and 'age'
# # greet("Eve")  # TypeError: greet() missing 1 required positional argument: 'age'
# greet("Frank", "thirty")  # No error, but age is expected to be an int
# greet(1,2,3)  # TypeError: greet() takes 2 positional arguments but 3 were given

# def greet(name, age=18):
#     """Greets a person with their name and age.
#         name: str - The name of the person.
#         age: int - The age of the person.
#         return: str - A greeting message.
#     """
#     return f"Hello, {name}! You are {age} years old."
# # greet() #TypeError: greet() missing 1 required positional argument: 'name'
# message = greet("George")
# print(message)
# message = greet("Hannah", 22)
# print(message)
# # greet("Ian", "twenty", 30)  # TypeError: greet() takes from 1 to 2 positional arguments but 3 were given

# def print_user_info(name, age=18, city="New York"):
#     print("User Information:")
#     print(f"\tName: {name}")
#     print(f"\tAge: {age}")
#     print(f"\tCity: {city}")
# print_user_info("Jack")
# print_user_info("Kathy", 25)
# print_user_info("Liam", 30, "Los Angeles")
# print_user_info("Los Angeles", "Liam", 30)
# print_user_info(city="Los Angeles", name="Liam", age=30)


# def print_elements(*rrr):
#     print("Elements:", rrr)
# print_elements(1,2,3,4)
# print_elements(1,2,3,4,5,6,7,8,9,10)
# print_elements("a", "b", "c")
# print_elements()
# def print_elements(*args, **kwargs):
#     print(f"{args=} {kwargs=}")

# print_elements(1,2,3,4)
# print_elements(1,2,3,4,5,6,7,8,9,10)
# print_elements("a", "b", "c")
# print_elements()
# print_elements(name="Alice", age=30)
# print_elements(1,2, three=3, four=4)
# print_elements(a=1, 2, three=3, four=4) # SyntaxError: positional argument follows keyword argument
# def f(a=1, b):
#     pass  # SyntaxError: non-default argument follows default argument
# def f(a, b, *args, c=10, d=20, **kwargs):
#     print(f"{a=}, {b=}, {args=}, {c=}, {d=}, {kwargs=}")
# f(1,2)
# f(1, 2, 3, 4, 5, c=30, z=40, x=100, y=200)


# global_var = "I am a global variable"
# def demonstrate_scope():
#     local_var = "I am a local variable"
#     print(f"{local_var=}")
#     return local_var
# print(f"{global_var=}")
# l = demonstrate_scope()
# print(f"{l=}")
# # print(local_var)  # NameError: name 'local_var' is not defined

# global_var = "I am a global variable"
# def demonstrate_scope():
#     local_var = "I am a local variable"
#     print(f"{global_var=}")
#     print(f"{local_var=}")

# demonstrate_scope()
# global_var = "I am a global variable"
# print(f"{global_var=}")
# def demonstrate_scope():
#     local_var = "I am a local variable"
#     print(f"\t{global_var=}") #UnboundLocalError: cannot access local variable 'global_var' where it is not associated with a value 
#     global_var = "I am a local variable with the same name as global"
#     print(f"\t{global_var=}")
#     print(f"\t{local_var=}")

# demonstrate_scope()
# print(f"{global_var=}")

# global_var = "I am a global variable"
# print(f"{global_var=}")
# def demonstrate_scope():
#     global global_var
#     local_var = "I am a local variable"
#     print(f"\t{global_var     =}")
#     global_var = "I am a local variable with the same name as global"
#     print(f"\t{global_var=}")
#     print(f"\t{local_var=}")

# demonstrate_scope()
# print(f"{global_var=}")
# a = 10
# b = 20
# c = 30
# def s(a,b,c):
#     return a > b > c
# print(f"{a=}, {b=}, {c=} {a>b>c=} {s(a,b,c)=}")


# def funk(name, age):

#     def inner_funk( city="Unknown" ):
#         return f"{name} is {age} years old and lives in {city}."

#     return inner_funk

# person1 = funk("Alice", 30)
# print(person1())
# print(person1("New York"))
# person2 = funk("Bob", 25)
# print(person2("Los Angeles"))
# print(person2())


# global_var = "I am a global variable"
# def outer_function():
#     local_var = "I am an outer variable"

#     def inner_function():
#         inner_var = "I am an inner variable"
#         print(f"{global_var=}")
#         print(f"{local_var=}")
#         print(f"{inner_var=}")

#     return inner_function
#     # print(f"{inner_var=}")  # NameError: name 'inner_var' is not defined
# f = outer_function()
# f()
# global_var = "I am a global variable"
# def outer_function():
#     local_var = ["I am an outer variable", 0]

#     def inner_function():
#         nonlocal local_var
#         inner_var = "I am an inner variable"
#         print(f"{global_var=}")
#         local_var[0] = "Modified outer variable"
#         local_var[1] += 1
#         print(f"{local_var=}")
#         print(f"{inner_var=}")

#     return inner_function
#     # print(f"{inner_var=}")  # NameError: name 'inner_var' is not defined
# f = outer_function()
# f()
# f()
# f()

# def recursive_factorial(n):
#     return n * recursive_factorial(n - 1)
    # if n == 0 or n == 1:
    #     return 1
    # else:
    #     return n * recursive_factorial(n - 1)

# import sys
# # sys.setrecursionlimit(2000)    
# print(recursive_factorial(5))  # Output: 120
# print(recursive_factorial(0))  # Output: 1

def factorial(n, prev_val=[]):
    print(f"factorial called with n={n}")
    prev_val.append(str(n))
    if n == 0 or n == 1:
        print(f"\t {"*".join(prev_val)}")
        return 1
    else:
        print(f"\t {"*".join(prev_val)}*factorial({n-1})")
        val = n * factorial(n - 1, prev_val)
        print(f"\t {val}")
        return val
result = factorial(5)
print(f"{result=}")  # Output: 120

# d = {
#   "level1_object": {
#     "level2_array": [
#       {
#         "level3_object": {
#           "property1": "value1",
#           "property2": "value2"
#         }
#       },
#       {
#         "level3_object_other": {
#           "property3": "value3"
#         }
#       }
#     ]
#   }
# }

# print(d)
# def print_nested(d, indent=0):
#     for key, value in d.items():
#         print(' ' * indent + str(key) + ": ", end="")
#         if isinstance(value, dict):
#             print()
#             print_nested(value, indent + 2)
#         elif isinstance(value, list):
#             print()
#             for item in value:
#                 if isinstance(item, dict):
#                     print_nested(item, indent + 2)
#                 else:
#                     print(' ' * (indent + 2) + str(item))
#         else:
#             print(str(value))

# print_nested(d)

# def convert_to_celsius(fahrenheit):
#     """Converts Fahrenheit to Celsius.
#         fahrenheit: float - Temperature in Fahrenheit.
#         return: float - Temperature in Celsius.
#     """
#     celsius = (fahrenheit - 32) * 5.0/9.0
#     return celsius
# # convert_to_celsius = lambda fahrenheit: (fahrenheit - 32) * 5.0/9.0
# temp_f = 100
# temp_c = convert_to_celsius(temp_f)
# print(f"{temp_f}°F is equal to {temp_c:.2f}°C")

celsius_to_fahrenheit = lambda celsius: (celsius * 9.0/5.0) + 32
print(f"0°C is equal to {celsius_to_fahrenheit(celsius=0)}°F")

# l = [0, 32, 100, 212]
# # fahrenheit_temps = list(map(lambda c: (c * 9.0/5.0) + 32, l))
# fahrenheit_temps = list(map(celsius_to_fahrenheit, l))
# print("Celsius to Fahrenheit:", fahrenheit_temps)

# def increment(list_of_numbers=[]):
#     list_of_numbers.append(1)
#     print(list_of_numbers)

# increment()
# increment([1,2,3,4])
# increment()
# increment()
# def increment(list_of_numbers=None):
#     if list_of_numbers is None:
#         list_of_numbers = []
#     list_of_numbers.append(1)
#     print(list_of_numbers)

# increment()
# increment([1,2,3,4])
# increment()
# increment()

# add = lambda a, b, c: a + b + c
# result = add(1, 2, 3)
# print(f"The result of adding 1, 2, and 3 is: {result}")

# def add_(a, b, c):
#     return a + b + c
# result_ = add_(1, 2, 3)
# print(f"The result of adding 1, 2, and 3 is: {result_}")

f = lambda x: x if x>=0 else -x

print(f(-10))
print(f(5))