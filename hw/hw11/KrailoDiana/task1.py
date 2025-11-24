def even_or_odd(age):
    if age < 0:
        raise ValueError(f"You entered a negative value")
    print(f"The age you entered: {age}")

    if age % 2 == 0:
        return "Your age is even"
    else:
        return "Your age is odd"
    
try:
    age = int(input("Enter your age in full years: "))
    print(even_or_odd(age))
except ValueError as ve:
    print(f"ValueError: {ve}")