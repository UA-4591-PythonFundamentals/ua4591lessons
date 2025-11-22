def count_character_frequency(input_string):
    frequency_count = {}

    for char in input_string:
        frequency_count[char] = frequency_count.get(char, 0) + 1
        
    return frequency_count

user_text = input("Enter a string to count its characters: ")

text_without_spaces = user_text.replace(" ", "")

frequency_output = count_character_frequency(text_without_spaces)

print(f"Input: '{user_text}'")
print(f"Output: {dict(frequency_output)}")