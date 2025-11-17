string = input("Enter a string: ")
dict = {}
for x in string:
    num = string.count(x)
    dict[f'{x}'] = num

print(dict)
