#task3

user_input = input("Enter your word: ")

user = user_input.lower().replace(" ", "")

def chr_number(user):
    result = dict()
    for chr in user:
        result[chr] = user.count(chr)
    return result

print(chr_number(user))