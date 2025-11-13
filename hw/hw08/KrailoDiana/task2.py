letters_lower = "abcdefghijklmnopqrstuvwxyz"
letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
characters = "$#@"

password = input("Check if your password is really secure: ")

def check_password (password):
    """Check if the given password passws all inspections"""
    counts_letter_upper = 0
    counts_letter_lower = 0
    counts_numbers = 0
    counts_characters = 0
    result = ""

    if len(password) >=6 and len(password) <= 16:
        for i in password:
            if i in letters_upper:
                counts_letter_upper += 1

        for i in password:
            if i in letters_lower:
                counts_letter_lower += 1
        
        for i in password:
            if i in numbers:
                counts_numbers += 1

        for i in password:
            if i in characters:
                counts_characters += 1

        if (counts_letter_upper >= 1 
            and counts_letter_lower >= 1 
            and counts_numbers >= 1
            and counts_characters >= 1):
            result = "Your password is super duper strong"
            
        else:
            if counts_letter_upper == 0:
                result = "There are not enough capital letters in the password"
            elif counts_letter_lower == 0:
                result = "There are not enough lowercase letters in the password"
            elif counts_numbers == 0:
                result = "There are not enough numbers in the password"
            elif counts_characters == 0:
                result = "There are not enough characters in the password"
        
    else:
        result = "Your length is wrong"   
    return result
print(check_password(password))