

# print("Hello, world!")
# print("This is Lesson 11.")
# a, b = 5, 10
# print(f"The sum of {a} and {b} is {a / b}.")
# a, b = 5, 0
# print(f"The sum of {a} and {b} is {a / b}.")



# while True:
#     a = input("  Enter a number: ")
#     b = input("  Enter another number: ")
#     if a == "exit" or b == "exit":
#         break        
#     try:
#         a = int(a)
#         b = int(b)
#         result = a / b
#         print(f"\tThe result of {a} divided by {b} is {result}.")
#     except:
#         print("\tError")
#     print("Next iteration.")

# print("End of program.")


# while True:


#     try:
#         a = int(input("  Enter a number: ")) # raraise ValueError
#         if a < 4:
#             b = a/(a-3) # raise ZeroDivisionError if a == 3
#             print(f"\tValue of b = {b}")
#         else:
#             print(f"\tValue of b = {b}") # raise NameError if a >= 4 because b is not defined in that case
       
#     except:
#         print("\tError")
#     print("Next iteration.")

# while True:
#     a = None
#     if a == "exit":
#         break        
#     try:
#         a = int(input("  Enter a number: ")) # raraise ValueError
#         if a < 4:
#             b = a/(a-3) # raise ZeroDivisionError if a == 3
#             print(f"\tValue of b = {b}")
#         else:
#             print(f"\tValue of b = {b}") # raise NameError if a >= 4 because b is not defined in that case
       
#     except (ZeroDivisionError, NameError):
#         print("\tError ")
#     print("Next iteration.")


# while True:
#     a = None
#     if a == "exit":
#         break        
#     try:
#         a = int(input("  Enter a number: ")) # raraise ValueError
#         if a < 4:
#             b = a/(a-3) # raise ZeroDivisionError if a == 3
#             print(f"\tValue of b = {b}")
#         else:
#             print(f"\tValue of b = {b}") # raise NameError if a >= 4 because b is not defined in that case
       
#     except (ZeroDivisionError, NameError, ValueError) as err:
#         print(f"\tError {type(err)}\t{err}")
#     print("Next iteration.")



# while True:
#     a = None
#     if a == "exit":
#         break        
#     try:
#         a = int(input("  Enter a number: ")) # raraise ValueError
#         if a < 4:
#             b = a/(a-3) # raise ZeroDivisionError if a == 3
#             print(f"\tValue of b = {b}")
#         else:
#             print(f"\tValue of b = {b}") # raise NameError if a >= 4 because b is not defined in that case
       
#     except ZeroDivisionError:
#         print("\tZeroDivisionError occurred.")
#     except NameError:
#         print("\tNameError occurred.")
#     except ValueError:
#         print("\tValueError occurred.")
#     except:
#         print("\tSome other error occurred.")
#     print("Next iteration.")


# while True:
      
#     try:
#         a = int(input("  Enter a number: ")) # raraise ValueError
#         if a < 4:
#             b = a/(a-3) # raise ZeroDivisionError if a == 3
#             print(f"\tValue of b = {b}")
#         if a == 4:
#             raise FloatingPointError("This is a floating point error.")
            
#         else:
#             print(f"\tValue of b = {b}") # raise NameError if a >= 4 because b is not defined in that case
#     except ZeroDivisionError:
#         print("\tZeroDivisionError occurred.")
#     except ArithmeticError as err:
#         print(f"\tArithmeticError occurred: {type(err)} {err}")
#     except NameError:
#         print("\tNameError occurred.")
#     except ValueError:
#         if input("  Enter exit if you want to exit: ") == "exit":
#             break
#         print("\tValueError occurred.")
#     except:
#         print("\tSome other error occurred.")
#     print("Next iteration.")



# try:
#     text = input("Enter something: ")
#     number = int(text)
# except ValueError as ve:
#     print(f"ValueError: {ve}")
# else:
#     print(f"You entered the number {number}.")

# print("End of program.")


# def divide_numbers(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError as zde:
#         print(f"Error: Cannot divide by zero. {zde}")
#         return 0
#     else:
#         print(f"The result of {a} divided by {b} is {result}.")
#         return result
#     finally:
#         # return "returned from finally block"
#         print("Execution of divide_numbers is complete.")

# r = divide_numbers(10, 2)
# print(f"Returned value: {r}\n")
# r = divide_numbers(10, 0)
# print(f"Returned value: {r}\n")


class CustomError(Exception):
    pass

class AnotherCustomError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
    def __str__(self):
        return super().__str__() + f" (Error Code: {self.code})"

def raise_custom_error(type_of_error_number, message="Custom error occurred."):
    if type_of_error_number == 1:
        raise ValueError(message)
    elif type_of_error_number == 2:
        raise KeyError(message)
    elif type_of_error_number == 3:
        raise IndexError(message)
    elif type_of_error_number == 4:
        raise CustomError(message)
    elif type_of_error_number == 5:
        raise AnotherCustomError(message, code=500)
    else:
        raise Exception("Unknown error type.")
    
    
for i in range(10):
    try:
        raise_custom_error(i, f"This is error number {i}.")
    except ValueError as ve:
        print(f"Caught ValueError: {ve} {type(ve)}")
    except KeyError as ke:
        print(f"Caught KeyError: {ke} {type(ke)}")
    except IndexError as ie:
        print(f"Caught IndexError: {ie} {type(ie)}")
    except CustomError as ce:
        print(f"Caught CustomError: {ce} {type(ce)}")
    except AnotherCustomError as ace:
        print(f"Caught AnotherCustomError: /{ace}/ {type(ace)}")
    except Exception as e:
        print(f"Caught Exception: {e} {i} {type(e)}")