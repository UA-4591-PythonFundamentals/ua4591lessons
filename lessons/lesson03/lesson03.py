# a = 5
# b = 10
# print(f"{a == b = }")  # Output: a == b = False
# print(f"{a != b = }")  # Output: a != b = True  
# print(f"{a < b = }")   # Output: a < b = True
# print(f"{a <= b = }")  # Output: a <= b = True
# print(f"{a > b = }")   # Output: a > b = False
# print(f"{a >= b = }")  # Output: a >= b = False
# print(f"{a is b = }")  # Output: a is b = False
# print(f"{a is not b = }")  # Output: a is not b = True 

# a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())
# print(f"{a =} {b =} {c =}")

# print(f"{a < b < c = }")      # Chained comparison

# a = True
# b = False
# print(f"{a=}\t{not a = }")  # Logical NOT
# print(f"{b=}\t{not b = }")  # Logical NOT

# a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())
# print(f"{a =} {b =} {c =}")

# print(f"{(a < b) and (b < c) = }")      # Logical AND
# print(f"{(a < b) or (b > c) = }")       # Logical OR

# def true(n):
#     print(f"true_{n}", end=" => ")
#     return True
# def false(n):
#     print(f"false_{n}", end=" => ")
#     return False

# print("Evaluating AND:")
# result_and = true(1) and false(2) and true(3)
# print(f"Result of AND: {result_and}\n")
# print("Evaluating OR:")
# result_or = false(1) or true(2) or false(3)
# print(f"Result of OR: {result_or}\n")
# # Short-circuit evaluation demonstration
# print("Evaluating AND with short-circuit:")
# result_and_short = false(1) and true(2) and true(3) 
# print(f"Result of AND with short-circuit: {result_and_short}\n")
# print("Evaluating OR with short-circuit:")
# result_or_short = true(1) or false(2) or false(3)

# result_and_or = true(1) and false(2) or true(3) and true(4)
# print()
# result_and_or = true(1) and false(2) or false(3) and (true(4) or true(5))
# result_and_or = true(1) and false(2) or (false(3) and true(4)) and true(5)


# print( "text" and "more text" and 123 )  # Output: 123
# print( "text" and "more text" and 123 and [] and 456 )  # Output: []
# print( [] or 0 or "" or None or "final value" )  # Output: final value
# print( [] or 0 or "" or False or None )  # Output: None


# is_false = [False, 0, 0.0, "", None, [], {}, set(), tuple()]

# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = l1
# print(f"{l1 == l2 = }")      # Output: True (values are equal)
# print(f"{l1 is l2 = }")      # Output: False (different objects
# print(f"{l1 is l3 = }")      # Output: True (same object)
# print(f"{l1 is not l2 = }")  # Output: True (different objects)

# "1" in 20 #TypeError: argument of type 'int' is not a container or iterable
# a = [
#     1, 2, 3, 4, 5,
#     [6, 7, 8, 9, 10],
#     "hello", 
#     (11, 12, 13)
# ]
# print(f"{3 in a = }")               # Output: True
# print(f"{7 in a = }")               # Output: False
# print(f"{7 in a[5] = }")            # Output: True
# print(f"{[6, 7, 8, 9, 10] in a = }")          # Output: True
# print(f"{'hello' in a = }")         # Output: True
# print(f"{'hell' in a = }")          # Output: False
# print(f"{'hell' in a[6] = }")          # Output: False
# print(f"{11 in a = }")              # Output: False
# print(f"{11 in a[7] = }")           # Output: True
# print(f"{(11, 12, 13)  in a = }")          # Output: True


# a = int(input("Enter an integer a: "))
# if a > 0 and a < 100:
#     print(f"\t{a} is a positive)")
#     print("\tnumber less than 100") 
#     print(f"\t{a} is a positive number less than 100")
# print("End of program")

# if a > 0:
#     print(f"\t{a} is a positive")
# else:
#     print(f"\t{a} is negative or zero")
# print("End of program")
# if a >= 0:
#     print(f"\t+++++++++")
#     print(f"\t{a} is a positive or zero")
#     print(f"\t+++++++++")
# else:
#     print(f"\t----------")
#     print(f"\t{a} is negative")
#     print(f"\t----------")
# print("End of program")

# age = int(input("Enter your age: "))

# if age < 0:
#     print("Error: Age cannot be negative.")
# else:
#     if age < 12:
#         print(f"\t{age} is a child.")
#     else:
#         if age < 18:
#             print(f"\t{age} is a teenager.")
#         else:
#             if age < 65:
#                 print(f"\t{age} is an adult.")
#             else:
#                 print(f"\t{age} is a senior citizen.")
# print("End of program")
# if age < 0:
#     print("Error: Age cannot be negative.")
# elif age < 12:
#     print(f"\t{age} is a child.")
# elif age < 18:
#     print(f"\t{age} is a teenager.")
# elif age < 65:
#     print(f"\t{age} is an adult.")
# else:
#     print(f"\t{age} is a senior citizen.")

# print("End of program")


# a = int(input("Enter an integer a: "))
# if a % 2 == 0:
#     print(f"\t{a} is even")
#     text = "even"
# else:
#     print(f"\t{a} is odd")
#     text = "odd"
# print(text)

# a = int(input("Enter an integer a: "))
# #  result =  a % 2 == 0 ? "even" : "odd"
# result  = "even" if a % 2 == 0 else "odd"
# print(f"\t{a} is {result}")

# if a % 2 == 0:
#     result  = "even" 
# else:
#     result  = "odd"
# a = int(input("Enter an integer a: "))


# is_false = [False, 0, 0.0, "", None, [], {}, set(), tuple()]
# if a != 0:
#     result = "non-zero"


# status_code = int(input("Enter status code (e.g., 200, 404, 500): "))

# match status_code:
#     case 200:
#         print("OK: The request has succeeded.")
#     case 301:
#         print("Moved Permanently: The resource has been moved to a new URL.")
#     case 400:
#         print("Bad Request: The server could not understand the request due to invalid syntax.")
#     case 401 | 402 | 405 as current_code:
#         print(f"Client Error: There was an error with the request from the client. {status_code} {current_code}")
#     case 403:
#         print("Forbidden: The client does not have access rights to the content.")
#     case 404:
#         print("Not Found: The server can not find the requested resource.")
#     case _ :
#         print("Unknown Status Code.")
# print("End of program.")

# ANSI escape codes for colors and reset
# RED = '\033[31m'
# BLUE = '\033[34m'
# GREEN = '\033[32m'
# RESET = '\033[0m' # Resets text formatting to default

# text = """
# save https://www.example.com/index.html index.html
# save https://www.example.com/about.html about.html contact.html text.txt
# ,jasgkchdbs  cjjs jbsj
# load index.html
# load about.html contact.html
# delete index.html"""

# for line in text.strip().split("\n"):
#     print(f"Processing line: {line}")
#     elements = line.split()
#     print(f"\t{elements = }")
#     match elements:
#         case "load", url:
#             print(BLUE + f"\t Loading from {url}" + RESET)
#         case "save", url, filename:
#             print(BLUE + f"\t Saving {url} to {filename}" + RESET)
#         case "save", url, *filenames:
#             print(BLUE + f"\t Saving {url} to multiple files:" + RESET)
#             for filename in filenames:
#                 print(GREEN + f"\t\t to {filename}" + RESET)
#         case ["load", *urls]:
#             print(BLUE + f"\t Loading from:" + RESET)
#             for url in urls:
#                 print(GREEN + f"\t\t {url}" + RESET)
#         case _:
#             print(RED +"\tUnknown command" + RESET)

# input_text =  input("Enter some text: ").strip()
# input_text = input_text.split()
# print(f"{input_text = }")
# numbers_text = list(filter(str.isdigit, input_text))
# print(f"{numbers_text = }")
# numbers = list(map(int, numbers_text))
# print(f"{numbers = }")
# # if len(numbers) > 0:
# if numbers:
#     max_number = max(numbers)
#     min_number = min(numbers)
#     sum_numbers = sum(numbers)
#     avg_number = sum_numbers / len(numbers)
#     print(f"Max: {max_number}")
#     print(f"Min: {min_number}")
#     print(f"Sum: {sum_numbers}")
#     print(f"Average: {avg_number}")
# else:
#     print("No numbers found in the input.")


# map(fun, iterable)
# def my_map(func, iterable):
#     results = []
#     for item in iterable:
#         results.append(func(item))
#     return results


text = """      
save https://www.example.com/index.html index.html
    save https://www.example.com/about.html about.html    contact.html    text.txt    
     ,jasgkchdbs  cjjs jbsj      
load    index.html  
load about.html contact.html
delete index.html      """
print(f"{text = }")
text = text.strip()
print(f"{text = }")
text = text.split("\n")
print(f"{text = }")
# elements = text[0].split()
# print(f"{elements = }")

for line in text:
    print(f"Processing line: {line}")
    elements = line.split()
    print(f"\t{elements = }")