days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def analyzer(number):
    if 0 < number < len(days) + 1:
        return days[number - 1]
    else:
        raise IndexError(f"You have entered a number that " \
                          "can't represent one of the days of the week")
    
try: 
    number = int(input("Enter a number from one to seven: "))
    print(analyzer(number))
except IndexError as ie:
    print(f"IndexError: {ie}")
except ValueError as ie:
    print(f"ValueError: please enter a numerical value")