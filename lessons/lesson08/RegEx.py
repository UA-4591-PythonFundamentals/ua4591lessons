import re

text = """Hello, my email is example@example.com
    and my website is https://www.example.com.
Feel free to reach out!
age 30 years old.
1992 was a greatello year.
This is a sample text for regex testing.
"""

# pattern = r'Hello'  # Pattern to match the word "Hello"
# matches = re.match(pattern, text)
# print("Match found:", matches)
# pattern = r'example.com'  # Pattern to match email addresses
# search = re.search(pattern, text)
# print("Search found:", search.group())
# pattern = "ea"
# findall = re.findall(pattern, text)
# print("Search found:", findall)

# pattern = re.compile(r'ea')
# finditer = pattern.finditer(text)
# for match in finditer:
#     print("Found at index:", match.start(), "-", match.group())

# pattern = "[abcdef1]"
# pattern = "[a-zA-Z0-9]"
# pattern = "\d"
# pattern = "e..o"
pattern = r"[a-z]{1,4}"
pattern_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
findall = re.findall(pattern_email, text)
print("Search found:", findall)