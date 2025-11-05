"""1. Jenny's secret message"""

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

"""2. Simple: Find The Distance Between Two Points"""

import math

def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

"""3. No yelling!"""

def filter_words(st):
    return " ".join(st.split()).capitalize()

"""4. Convert a Number to a String!"""

def number_to_string(num):
    return str(num)

"""5. Reversing Words in a String"""

def reverse(st):
    words = st.split()
    return " ".join(reversed(words))

"""6. Reverse List Order"""

def reverse_list(l):
    'return a list with the reverse order of l'
    return l[::-1]

"""7. Multiples of 3 or 5"""

def solution(number):
    set_of_multiples = set()
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            set_of_multiples.add(i)
    return sum(set_of_multiples)

"""8. Will you make it?"""

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

"""9. Are You Playing Banjo?"""

def are_you_playing_banjo(name):
    # Implement me!
    return f'{name} plays banjo' if name.lower()[0:1] == 'r' else f'{name} does not play banjo'

"""10. Convert boolean values to strings 'Yes' or 'No'."""

def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

"""11. Counting sheep"""

def count_sheeps(sheep):
  # TODO May the force be with you
    return sheep.count(True)

"""12. Is this my tail?"""

def correct_tail(body, tail):
     return body[-1] == tail
