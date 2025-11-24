def day_of_week():

    try:
        number = int(input('Enter a number: '))
    except ValueError:
        return 'This is not a number!'

    valid_days = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}

    if number in valid_days:
        result=valid_days[number]
    else:
        result = 'Enter a number between 1 and 7'
    return result


if __name__ == '__main__':
    print(day_of_week())
