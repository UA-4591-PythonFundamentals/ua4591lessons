def check_age(age):
    try:
        age == int(age)
    except ValueError:
        raise ValueError("Incorect data type.")
    
    age_int = int(age)

    if age_int<0:
        raise Exception("Age can not be a negative number.")
    elif age_int%2==0:
        return ("Your age is even.")
    else:
        return ("Your age is odd.")



if __name__ == "__main__":
    while True:
        input_age = input("Enter your age (quit for exit): ")

        if input_age.lower() == "quit":
            print("End of programe")
            break

        try:
            result = check_age(input_age)
            print(result)
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as err:
            print(f"Error: {err}")