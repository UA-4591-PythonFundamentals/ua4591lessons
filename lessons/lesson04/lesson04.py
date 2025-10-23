from time import sleep

# for element in "Hello, World!":
#     print("begin iteration")
#     print(f"\t{element}")
#     print("end iteration")
# else:
#     print("end for")
#     print("else block executed")
#     print(element)
# print("main program end")

# text = "Hello, World!"
# while text:
#     print("begin iteration")
#     print(f"\t{text[0]}", end=" => ")
#     text = text[1:]
#     print(f"{text}")
#     print("end iteration")

# index = 0
# while index < len(text):
#     print("begin iteration")
#     print(f"\t{text[index]}")
#     index += 1
#     print("end iteration")

# from time import sleep


# while True:
#     print("begin iteration")
#     print("\tHello, World!")
#     print("end iteration")
#     sleep(5)


# input_text = input("Enter some Numbers (or 'quit' to exit): ")

# while input_text.lower() != 'quit':
#     if not input_text.isdigit():
#         print("Please enter only numeric values.")
#     else:
#         input_text = int(input_text)
#         print(f"Your numbers are: {input_text}")

#     input_text = input("Enter some Numbers (or 'quit' to exit): ")

# print("Program ended.")

# l = [1, 2, 3, 4, 5]
# for element in l:
#     print(f"\t{element} {l}")
#     l.append(len(l) + 1)
#     sleep(0.5)

# l = [1, 2, 3, 4, 5]
# for element in l:
#     print(f"\t{element} {l}")
#     l.insert(0, (len(l) + 1))
#     sleep(0.5)

# text = "12345"
# for i in text:
#     print(f"\t{i} {text}")
#     text = text + str(len(text) + 1)
# text = "12345"
# for i in text:
#     print(f"\t{i} {text}")
#     text = str(len(text) + 1) + text

# r = range(5)
# print(r)
# for i in r:
#     print(f"\t{i}")
# print(list(r))
# print(list(range(-5)))
# print(list(range(-5, 0)))
# print(list(range(-5, 5)))
# print(list(range(-5, 5, 2)))

# from random import randint
# l = [randint(-10, 10) for _ in range(5)]
# print(l)
# for i in range(len(l)):
#     old_value = l[i]
#     l[i] = l[i] ** 2
#     print(f"\tIndex {i}, Old Value {old_value}, New Value {l[i]}")
# print(l)
# enumerate_l = list(enumerate(l))
# print(enumerate_l)
# enumerate_l = list(enumerate("Hello"))
# print(enumerate_l)

# input_text = input("Enter some comma-separated values: ")
# # for row in enumerate(input_text.split(",")):
# #     print(f"Processing next item... {row}")
# #     print(f"Index {row[0]}, Value {row[1].strip()}")

# a, b = (5, 10)
# for index, value in enumerate(input_text.split(","), start=10):
#     print(f"Processing next item... Index {index}, Value {value.strip()}")

# text = input("Enter some comma-separated values: ")
# sum = 0
# for element in text.split():
#     print(f"Processing element {element}")
#     if element.isdigit():
#         print(f"\tNumeric value encountered: {element} -> adding to sum", end=", ")
#         sum += int(element)
#         print(f"\tCurrent sum: {sum}")
#         continue
#     print(f"\tNon-numeric value encountered: {element}")
#     print("\tSkipping to next element...")
# else:
#     print(f"Total sum of numeric values: {sum}")



# text = input("Enter some comma-separated values: ")
# sum = 0
# count_bad = 0
# for element in text.split():
#     print(f"Processing element {element}")
#     if element.isdigit():
#         print(f"\tNumeric value encountered: {element} -> adding to sum", end=", ")
#         sum += int(element)
#         print(f"\tCurrent sum: {sum}")
#         continue

#     count_bad += 1
#     print(f"\tNon-numeric value encountered: {element}  bad count: {count_bad}")
#     if count_bad >= 3:
#         print("\tToo many non-numeric values encountered. Exiting loop.")
#         break
#     print("\tSkipping to next element...")
# else:
#     print(f"Total sum of numeric values: {sum}")
#     print(f"Total non-numeric values encountered: {count_bad}")
# print("Loop has ended.")

# for _ in "Hello":
#     pass
# else:
#     pass


# i = 0

# while i < 100:
#     if i % 2 == 0:
#         print(i, end=", ")
#     i+=1
# print()


# for x in range(100):
#     if x % 2 == 0:
#         print(f"It is even number: {x}")

# for i in range(2, 100, 2):
#     print(f"{i}", end=", ")
# print()


# for i in range(100):
#     if (i % 2) == 0: 
#         continue
#     print(f"{i}", end=", ")

# for i in range(1, 100, 2):
#      print(f"{i}", end=", ")

# r = list(range(5))
# has_odd = False
# for i in r:
#     if i % 2 != 0:
#         has_odd = True
#         break
# print(has_odd)
r = list(range(5))
for i in r:
    if i % 2 != 0:
        break
else:
    print("No odd numbers found")
    print("All numbers are even")


list1 = (2, 4, 4, 6, 8, 7, 8, 6)
for i in list1:
    if i % 2 != 0: 
        break
    print(f"{i}", end=", ")