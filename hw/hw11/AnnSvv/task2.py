def day(number):
    days = ["Monday", "Tuesday", "Wednesday", 
            "Thursday", "Friday", "Saturday",
            "Sunday"]
    
    try:
        number == int(number)
    except ValueError:
        raise ValueError("Incorect data type.")
    
    number = int(number)

    if number>7 or number<=0:
        raise Exception("Incorect number.")
    else:
        return (days[number-1])
    

if __name__ == "__main__":

    while True:
        user_num=input("Enter your number to get the day (quit for end): ")

        if user_num == "quit":
            print("End programe.")
            break

        try:
            result = day(user_num)
            print(result)
        except ValueError as ve:
            print ("Incorect data type.")
        except Exception as err:
            print (f"Error: {err}")