# print("lesson13.py loaded")

# l = [i*i for i in range(10)]
# s ={i*i for i in range(10)}
# d = {i: i*i for i in range(10)}

# print("List:", l)
# print("Set:", s)
# print("Dict:", d)

# t = (i*i for i in range(10))
# print("Tuple (generator):", t)

# n = 10
# for i in range(5):
#     l = [j for j in range(n)]
#     print(f"Size of list with {n} size:", l.__sizeof__(), sep="\t")
#     t = (j for j in range(n))
#     print(f"Size of generator with {n} size:", t.__sizeof__(), sep="\t")
#     n *= 10


# l1 = [1,2,3,4]
# l2 = ['a','b','c','d','e']
# l3 = [100,200,300,400,500, 600]
# zipped = zip(l1, l2, l3)
# print("Zipped object:", zipped)
# print("Zipped as list:", list(zipped))
# sst = "ab"
# zipped2 = zip(l1, sst)
# print("Zipped2 as list:", list(zipped2))

# map1 = map(lambda x: x*x, range(10))
# print("Map object:", map1)
# print("Map as list:", list(map1))
# filter1 = filter(lambda x: x%2==0, range(10))
# print("Filter object:", filter1)
# print("Filter as list:", list(filter1))


# from functools import reduce
# l = [1,20,300,4000,50000]
# def my_add(x, y):
#     print(f"Adding {x} and {y}")
#     return x + y
# reduce1 = reduce(my_add, l)
# print("Reduce result:", reduce1)
# reduce1 = reduce(my_add, l, -1_000_000)
# print("Reduce result:", reduce1)

# l = ["apple", "banana", "cherry", "date"]
# print("List l:", l)
# for el in l:
#     print(f"Element: {el}")
# print(f"l[0]: {l[0]}")
# print(f"l[1]: {l[1]}")
# print(f"l[2]: {l[2]}")
# print(f"l[3]: {l[3]}")
# it = iter(l) # l.__iter__()
# print(it)
# print(f"next(it): {next(it)}") # it.__next__()
# print(f"next(it): {next(it)}") # it.__next__()
# print(f"next(it): {next(it)}") # it.__next__()
# print(f"next(it): {next(it)}") # it.__next__()
# print(f"next(it): {next(it)}") # it.__next__()

# for el in l:
#     print(f"Element: {el}")






# class MyRange:
#     def __init__(self, start, end=None, step=1):
#         if end is None:
#             self.start = 0
#             self.end = start
#         else:
#             self.start = start
#             self.end = end
#         self.step = step

#     def __iter__(self):
#         print("MyRange __iter__ called")
#         self.current = self.start
#         return self

#     def __next__(self):
#         print("MyRange __next__ called")
#         if self.current < self.end:
#             val = self.current
#             self.current += self.step
#             return val
#         else:
#             raise StopIteration
            
        
#     def __str__(self):
#         return f"MyRange({self.start}, {self.end}, {self.step})"
    
# r = MyRange(5)
# print("MyRange object:", r)
# for i in r:
#     print(i)
# r = MyRange(5, 15)
# print("MyRange object:", r)
# r = MyRange(-5, 15, 2)
# print("MyRange object:", r)
# r_iter = iter(r)
# print("Iterator object:", r_iter)

# print(next(r_iter))
# print(next(r_iter))
# print(next(r_iter))

# def my_generator(n):
#     print("my_generator started")
#     for i in range(n):
#         print(f"my_generator yielding {i}")
#         yield i
#         print(f"my_generator resumed after yielding {i}")
#     print("my_generator ended")
# print(type(my_generator))
# gen = my_generator(3)
# print("Generator object:", gen)
# print(f"next(gen): {next(gen)}")
# print("="*40)
# print(f"next(gen): {next(gen)}")
# print("="*40)
# print(f"next(gen): {next(gen)}")
# print("="*40)
# print(f"next(gen): {next(gen)}")


# def decorator_function(original_function):
#     print("Decorator executed")
#     print(f"Original function name: {original_function.__name__}")
#     return original_function


# def add(x, y):
#     return x + y

# add = decorator_function(add)

# a = add(2, 3)
# print("Add result:", a)
# a = add(5, 6)
# print("Add result:", a)

# @decorator_function
# def multiply(x, y):
#     return x * y

# m = multiply(2, 3)
# print("Multiply result:", m)
# m = multiply(5, 6)
# print("Multiply result:", m)


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(f"Wrapper executed before calling {original_function.__name__} arguments: {args}, {kwargs}")
#         result = original_function(*args, **kwargs)
#         print(f"Wrapper executed after calling {original_function.__name__} result: {result}")
#         return result
#     return wrapper_function


# def add(x, y):
#     return x + y

# add = decorator_function(add)

# a = add(2, 3)
# print("Add result:", a)
# a = add(5, 6)
# print("Add result:", a)

# # @decorator_function
# def multiply(x, y):
#     return x * y

# m = multiply(2, 3)
# print("Multiply result:", m)
# m = multiply(5, 6)
# print("Multiply result:", m)



# def super_star_decorator(original_function):
#     def wrapper_function(*args, **kwargs):
#         print("*** Super Star Decorator *****")
#         print(f"Wrapper executed before calling {original_function.__name__} arguments: {args}, {kwargs}")
#         result = original_function(*args, **kwargs)
#         print(f"Wrapper executed after calling {original_function.__name__} result: {result}")
#         print("******************************")
#         return result
#     return wrapper_function


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(f"Wrapper executed before calling {original_function.__name__} arguments: {args}, {kwargs}")
#         result = original_function(*args, **kwargs)
#         print(f"Wrapper executed after calling {original_function.__name__} result: {result}")
#         return result
#     return wrapper_function


# def add(x, y):
#     return x + y

# add = decorator_function(add)

# a = add(2, 3)
# print("Add result:", a)
# a = add(5, 6)
# print("Add result:", a)

# @super_star_decorator
# @decorator_function
# @super_star_decorator
# def multiply(x, y):
#     return x * y

# m = multiply(2, 3)
# print("Multiply result:", m)
# m = multiply(5, 6)
# print("Multiply result:", m)



def chars(char, repeat=10):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(char * repeat)
            result = original_function(*args, **kwargs)
            print(f"Wrapper executed before calling {original_function.__name__} arguments: {args}, {kwargs} result: {result}")
            print(char * repeat)
            return result
        return wrapper_function
    return decorator_function



@chars("-", repeat=40)
@chars("=", repeat=5)
@chars("*", repeat=3)
@chars("-", repeat=10)
def add(x, y):
    return x + y

# print(list)
# print(list())

a = add(2, 3)
print("Add result:", a)