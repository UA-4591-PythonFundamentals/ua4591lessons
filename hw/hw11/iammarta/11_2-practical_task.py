def day_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    if number < 1 or number > 7:
        raise ValueError("Number must be between 1 and 7!")
    
    print(f"The day of the week is {days[number]}.")

try:
    user_input = input("Enter a number from 1 to 7 for the day of the week: ")
    number = int(user_input)
    day_of_week(number)
except ValueError as e:
    print("Error:", e)
