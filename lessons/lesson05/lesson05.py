# # list 

# my_list = []
# print(type(my_list), my_list)

# my_list = [1, "hello", 3.14, True]
# print(type(my_list), my_list)

# my_list = list()
# print(type(my_list), my_list)

# my_list = list((1, 2, 3))
# print(type(my_list), my_list)
# my_list = list("hello")  # string to list
# print(type(my_list), my_list)
# # my_list = list(150)  # TypeError: 'int' object is not iterable

# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))  # length of the list
# print(my_list[0])  # first element
# print(my_list[-1])  # last element
# print(my_list[1:4])  # slicing
# print(my_list[::2])  # slicing
# my_list = my_list + [6, 7,[10,20,30]]  # concatenation
# print(my_list)
# print(my_list[7])  # accessing nested list element
# print(my_list[7][1])  # accessing nested list element
# my_list = my_list * 2  # repetition
# print(my_list)
# my_list[0] = 100  # modifying element
# print(my_list)
# print(3 in my_list)  # membership test
# print(30 in my_list)  # membership test
# print([10,20,30] in my_list)  # membership test
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = [2, 1, 3]
# print(l1 == l2)  # equality test
# print(l1 == l3)  # equality test
# print(l1 is l2)  # identity test
# print(id(l1), id(l2))

# print("----- list methods -----")
# print([method for method in dir(list()) if not method.startswith("_")])

# my_list = [1, 2, 3]
# print("Original list:", my_list)
# my_list.append(4)  # add element at the end
# my_list.append([5, 6])  # add nested list at the end
# my_list.append("hello")  # add string at the end
# my_list.append([5, 6])  # add nested list at the end
# my_list.append(my_list)  # add self reference at the end
# # print(my_list)
# # print("Length of list after appends:", len(my_list))
# # print(my_list[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1])  # accessing self reference
# # my_list.extend(10) #TypeError: 'int' object is not iterable
# my_list.extend([7, 8, 9])  # extend list with another list
# my_list.extend("world")  # extend list with string (iterable)
# # print("List after extends:", my_list)
# # print(my_list.count(3))  # count occurrences of 3
# # print(my_list.count("3"))  # count occurrences of 3
# # print(my_list.count([5,6]))  # count occurrences of 3
# # print(my_list.index([5,6]))  # index of first occurrence of 4
# # print(my_list.index([5,6], my_list.index([5,6])+1))  # index of first occurrence of 4 after a given index
# # my_list.index("hello test")  # ValueError: list.index(x): x not in list
# my_list.insert(0, 0)  # insert 0 at index 0
# my_list.insert(5, [5, 6, 7])  # insert [5, 6, 7] at index 5
# print("List after insert:", my_list)
# element = my_list.pop()  # remove and return last element
# print("Popped element:", element, "Updated list:", my_list)
# element = my_list.pop(3)  # remove and return element at index 3
# print("Popped element at index 3:", element, "Updated list:", my_list)
# my_list.remove([5, 6])  # remove first occurrence of [5, 6]
# print("List after remove:", my_list)
# # my_list.remove(10)  # ValueError: list.remove(x): x not in list
# my_list.reverse()  # reverse the list
# print("Reversed list:", my_list)
# r_l =reversed(my_list)  # returns an iterator
# print("Reversed list using reversed():", list(r_l))  # converting iterator to list
# print("Original list remains unchanged:", my_list)
# my_list.sort(key=lambda x: len(x) if type(x) in (list, str) else x)  # sort the list
# print("Sorted list:", my_list)
# sorted_list = sorted(my_list, reverse=True, key=lambda x: len(x) if type(x) in (list, str) else x)  # returns a new sorted list
# print("Sorted list (new):", sorted_list)


# l = [5, 2, 9, 1, 5, 6]
# print("Original list:", id(l), l)
# l.clear()  # clear the list
# print("Cleared list:", id(l), l)
# l = [5, 2, 9, 1, 5, 6]
# print("Original list:", id(l), l)
# l = []  # reassign to empty list
# print("Reassigned to empty list:", id(l), l)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l = [7, 8, l1, l2]
# print(f"{l1=}")
# print(f"{l2=}")
# print("Original list:", l)
# print(f"{l[2] is l1=}")
# print(f"{l[3] is l2=}")
# l1.clear()
# l2 = []
# print("After clearing l1 and reassigning l2 to empty list:")
# print(f"{l1=}")
# print(f"{l2=}")
# print("Updated list:", l)
# copy_l = l.copy()  # shallow copy
# print("Shallow copy of list:", copy_l)
# l1.append(9)
# print("After modifying l1:")
# print(f"{l1=}")
# print("Original list:", l)
# print("Shallow copy of list:", copy_l)

# import copy
# deepcopy_l = copy.deepcopy(l)  # deep copy
# print("Deep copy of list:", deepcopy_l)
# l1.append(10)
# print("After modifying l1 again:")
# print(f"{l1=}")
# print("Original list:", l)
# print("Deep copy of list:", deepcopy_l)


# class MyClass:
#     def __del__(self):
#         print("MyClas instance is being deleted")


# def f(a):
#     obj = MyClass()
#     if a:
#         return obj

# print("Calling f with True:")
# f(True)
# print("Calling f with True:")
# g = f(True)
# print("Calling f with True:")
# del g
# print("End of program")

# l_truthy = [1, "hello", [3, 4], True, 5.6]
# l_falsy = [0, "", [], False, None]
# print(all(l_truthy))  # True
# print(all(l_truthy+[0]))  # False
# print(any(l_falsy))  # False
# print(any(l_falsy+ [1]))  # True

# print(list(enumerate(l_truthy)))  # list of tuples (index, value)
# print(min(list("hello")))  # list from string

# l = []
# for i in range(5):
#     l.append(i * i)
# print("List using append in loop:", l)
# l = [i * i for i in range(5)]
# print("List using list comprehension:", l)
# l = []
# for i in range(10):
#     for j in range(i, 10):
#         if (i + j) % 2 == 0:
#             l.append((i, j))
# print("List of tuples using append in nested loop:", l)
# l = [(i, j) for i in range(10) for j in range(i, 10) if (i + j) % 2 == 0]
# print("List of tuples using list comprehension:", l)




# # tuple
# t = ()
# print(type(t), t)
# t = (1,2,3)
# print(type(t), t)
# t = (1) # not a tuple
# print(type(t), t)
# t = (1,)
# print(type(t), t)
# t = tuple([1, 2, 3])
# print(type(t), t)
# t = tuple("hello")
# print(type(t), t)
# print(len(t))
# print(t[0])

# print("----- tuple methods -----")
# print([method for method in dir(tuple) if not method.startswith("_")])
# # t[0] = 100  # TypeError: 'tuple' object does not support item assignment
# l = [1, 2, 3]
# t = (10,20, l)
# print("Original tuple:", t)
# # t[2] = [4,5,6]  # TypeError: 'tuple' object does not support item assignment
# t[2][0] = 100  # modifying nested list inside tuple
# l.append(4)
# print("After modifying nested list in tuple:", t)

# t = ([1, 2], [3, 4], {"test"}, (5,6))
# print("Original tuple:", t)

# tt = t
# print("Shallow copy of tuple:", tt)
# print(f"{tt is t=}")

#set

# s = set()
# print(type(s), s)
# s = set("hello")
# print(type(s), s)

# # s = set([1, 2, 3, 2, [1,2,3]])  # TypeError: unhashable type: 'list'
# s = {} # this creates an empty dict, not a set
# print(type(s), s)
# s = {1, 2, 3, 4, 5, 5, 4}
# print(type(s), s)

# print("----- set methods -----")
# print([method for method in dir(set) if not method.startswith("_")])
# s = {1, 2, 3}
# s.add(4)
# s.add("hello")
# print("Set after add:", s)
# s.update([5, 6, 7])
# s.update("hello")
# print("Set after update:", s)
# element = s.pop()
# print("Popped element:", element, "Updated set:", s)
# s.remove(3)
# print("Set after remove:", s)
# # s.remove(10)  # KeyError: 10

# dict

# d = {}
# print(type(d), d)
# d = {"a": 1, 10: 2, (1,2,3): lambda x: x*x}
# print(type(d), d)
# d = dict()
# print(type(d), d)
# d = dict(a=1, b=2, c=3)
# print(type(d), d)
# d = dict([("x", 10), ("y", 20)])
# print(type(d), d)
d = {"a": 1, 10: 2, (1,2,3): lambda x: x*x}
print(type(d), d)
print(len(d))
print(d["a"])  # access value by key
print(d[10]) # access value by key
print(d[(1,2,3)])  # access value by key
print(d[(1,2,3)](5))  # access value by key
# print(d["test"])  # KeyError
d["a"] = 100  # modify value by key
print(d)
d["new_key"] = "new_value"  # add new key-value pair
print(d)

print("----- dict methods -----")
print([method for method in dir(dict) if not method.startswith("_")])

print(d.get("a"))  # get value by key
print(d.get("non_existing_key"))  # get value by key with default
print(d.get("non_existing_key", "default_value"))  # get value by key with default
d.update({"a": 200, "b": 300})  # update multiple key-value pairs
print(d)
element = d.pop("new_key")  # remove key-value pair by key
# d.pop() # TypeError: pop expected at least 1 argument, got 0
print(element)
print(d)
dd = d.fromkeys(["x", "y", "z"], 0)  # create new dict from keys with default value
print(dd)
d.setdefault("a", 500)  # set default value for key if not exists
d.setdefault("c", 400)  # set default value for key if not exists
print(d)
print(d.keys())  # get all keys
print(d.values())  # get all values
print(d.items())  # get all key-value pairs

for key in d:
    print(f"Key: {key}, Value: {d[key]}")

for key, value in d.items():
    print(f"Key: {key}, Value: {value}")    