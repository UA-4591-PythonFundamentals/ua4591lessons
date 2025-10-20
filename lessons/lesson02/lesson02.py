# a = []
# print(type(a), a)
# a = 10
# print(type(a), a)
# a = "hello"
# print(type(a), a)

# a = [10, 20, 30]
# print(type(a), id(a), a)
# def func(x): pass
# print(type(func), id(func))
# a.append(40)
# print(type(a), id(a), a)
# a = 1
# print(type(a), id(a), a)
# a += 1
# print(type(a), id(a), a)

# print(isinstance(a, int))
# print(isinstance(a, float))
# print(type(a) is int)
# print(type(a) is float)

# class A: pass
# class B(A): pass

# a = A()
# b = B()
# print(isinstance(a, A))
# print(isinstance(b, A))
# print(isinstance(b, B))
# print(isinstance(a, B))
# print(type(a) is A)
# print(type(b) is A)

# a = [1,2,3]
# b = [1,2,3]
# print(f"a: {id(a)}, b: {id(b)}")
# print(f"{a == b =}")
# print(f"{a is b =}")
# print(f"{id(a) == id(b) =}")
# a = 1+2+3+4+5+6+7+8+9+10
# print(a)
# a = 1+2+3+4+5+\
#     6+7+8+9+10
# print(a)
# a = 1+2+3+4+5
# 6+7+8+9+10
# print(a)

# a = (1+2
#      +3+4+5+
#     6+7+8+9+10)
# print(a)
# for i in range(4):
#    print(i)
#    print(i)
#    for j in range(3):
#     print("\t", j)
#     if j == 1:
#               break

# print("end loop")

# a = 1
# b = 2
# c = 3
# print(a, b, c)
# a, b, c = 1, 2, 3
# print(a, b, c)
# # a, b, c = 1, 2 #ValueError: not enough values to unpack (expected 3, got 2)
# # a, b, c = 1, 2, 3, 4 #ValueError: too many values to unpack (expected 3, got 4)
# a, b, c = [1, 2, 3]
# print(a, b, c)
# a = "hello"
# b = a
# c = b
# print(a, b, c)
# a = b = c = "hello"

# PI = 3.14
# RADIUS = 10
# area = PI * RADIUS ** 2
# print("Area of circle:", area)
# PI = 3.14159
# RADIUS = 10
# area = PI * RADIUS ** 2
# print("Area of circle:", area)

# b = 0b1010
# o = 0o12
# h = 0xA
# d = 10
# print(b, o, h, d)
# print(b == o == h == d)
# d = 17
# print(bin(d), oct(d), hex(d))

# a = 10_000_00_0_000
# print(a)

# a = 1.1
# print(type(a), a)
# a = .1
# print(type(a), a)
# a = 1.
# print(type(a), a)
# a = 1e3 # 1 * 10**3
# print(type(a), a)
# a = 1e-3 # 1 * 10**-3
# print(type(a), a)
# a = True + True
# print(type(a), a)
# a = True
# print(type(a), a)
# a = False
# print(type(a), a)
# a = False + 10
# print(type(a), a)
# a = False * 10
# print(type(a), a)
# a = None # null, nil, nullptr
# print(type(a), a)

# a = [1,2,3]
# print(type(a), a)
# a = (1,2,3)
# print(type(a), a)
# a = {1,2,3}
# print(type(a), a)
# a = {"one":1, "two":2, "three":3}
# print(type(a), a)

# l = [1, None, "hello", 2.5, True, [1,2,3], (4,5,6), {7,8,9}, {"one":1}]
# print(id(l), l)
# l[1] = 100
# l.append("world")
# print(l[5])
# l[5][0] = "TEST"
# print(id(l), l)

# t = (1, None, "hello", 2.5, True, [1,2,3], (4,5,6), {7,8,9}, {"one":1})
# print(id(t), t)
# # t[1] = 100 # TypeError: 'tuple' object does not support item assignment
# t[5][0] = "TEST"
# print(id(t), t)

# s = {1, 2, 3, 4, 5, 1, 2, 3}
# print(id(s), s)
# s = set("hello worldhello worldhello worldhello worldhello worldhello worldhello world")
# print(id(s), s)

# d = {
#     "one":1,
#     "two":2,
#     "three":3,
#     "one":10
# }
# print(id(d), d)
# d["four"] = 4
# print(id(d), d)
# print(d["two"])
# d["two"] = 20
# print(id(d), d)

# input_data = "10"
# value = int(input_data)
# print(type(value), value)
# value = int(input_data, 2)
# input_data = "17"
# print(type(value), value)
# value = int(input_data, 8)
# print(type(value), value)
# value = int(input_data, 16)
# print(type(value), value)
#int() base must be >= 2 and <= 36, or 0
# 0 1 2 3 4 5 6 7 8 9
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# input_data = "11"
# value = int(input_data, 22) 
# print(type(value), value)
# value = float("1.23")
# print(type(value), value)
# value = float("1")
# # print(type(value), value)
# a  = 10
# s = str(a)
# print(type(s), s)
# class S:pass
# s = S()
# print(type(s), s)
# class S:
#     def __str__(self):
#         return "This is S class"
# s = S()
# # print(type(s), s)
# print(list("hello"))
# print(list(10)) # TypeError: 'int' object is not iterable

# for i in range(255):
#     print(i, chr(i))
# for i in "hsdgfiuncndo87vydp9shU(G)*gh9T&(T 783h4t8":
#     print(i, ord(i))

# st = "hello"
# print(type(st), st)
# st[0] = "H" # TypeError: 'str' object does not support item assignment

# text = "some text"
# print(text)
# text = "some\n text"
# print(text)

# text = "0123456789\rtext" 
# print(text)
# char = ["|", "/", "-", "\\"]
# from time import sleep
# for i in range(100):

#     print(f"\t{char[i % 4]}\t{i=}", end="\r")
#     sleep(0.05)
# print("end")  

# text = 'my"text'
# text = "my\"text"
# print(text)

# template = "my name is %s, I'm %d years old, my height is %.2f m"
# print(template)
# print(template % ("Liubomyr", 39, 1.835))
# print(template % ("Andrii", 53, 1.9))
# print(template % ("Andrii", "53", 1.9)) #TypeError: %d format: a real number is required, not str

# template = "my name is {}, I'm {} years old, my height is {} m"
# print(template)
# print(template.format("Liubomyr", 39, 1.835))
# print(template.format("Andrii", 53, 1.9))
# print(template.format("Andrii", "53", 1.9))
# template = "my name is {name}, I'm {age} years old, my height is {height} m"
# print(template)
# print(template.format(name="Liubomyr", age=39, height=1.835))
# print(template.format(height=1.9, name="Andrii", age=53))

# name = "Liubomyr"
# age = 39
# height = 1.835
# print(f"my name is {name}, I'm {age} years old, my height is {height} m")
# print(f"my name is {name.upper()}, I'm {age+1} years old, my height is {height*100:.1f} cm")

# text = "some more text"
# print(text)
# print(f"{text[0]=}")
# print(f"{text[1]=}")
# print(f"{text[2]=}")
# print(f"{len(text)=}")
# print(f"{text[-1]=}")
# print(f"{text[-2]=}") 
# print(f"{text[1:7] =}")
# print(f"{text[:7] =}")
# print(f"{text[1:] =}")
# print(f"{text[::2] =}")
# print(f"{text[2:-5:2] =}")
methods = [method for method in dir(str) if not method.startswith("__")]
print(methods)
print(len(methods))

sentence = "i love PYTHON. i love programming. i love coffee!"
print(sentence)
print(f"{sentence.capitalize() =}")
print(f"{sentence.title() =}")
print(f"{sentence.upper() =}")
print(f"{sentence.lower() =}")
print(f"{sentence.swapcase() =}")
print(f"{sentence.count("love") =}")
print(f"{sentence.count("LOVE") =}")
print(f"{sentence.count("o") =}")
print(f"{sentence.find("love") =}")
print(f"{sentence.find("LOVE") =}")
print(f"{sentence.rfind("love") =}")
print(f"{sentence.index("love") =}")    
print(f"{sentence.rindex("love") =}")
# print(f"{sentence.index("LOVE") =}") # ValueError: substring not found
print(f"{sentence.startswith("i love") =}")
print(f"{sentence.endswith("coffee!") =}")
print(f"{sentence.split() =}")
print(f"{sentence.split("love") =}")
print(f"{" => ".join(["test_1", "test_2", "test_3"]) =}")
print(f"{sentence.rsplit("love", 1) =}")
print(f"{sentence.partition("programming") =}") 
print(f"{sentence.rpartition("love") =}")
print(f"{sentence.replace("love", "like") =}")
print(f"{sentence.replace("love", "like", 1) =}")
text = "100"
print(f"{text.isdigit() =}") #0123456789
print(f"{text.isalpha() =}") #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(f"{text.isalnum() =}") #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

text = "hello"
print(f"{text.zfill(10) =}")
a = True + True
print(a)
text = "01000101010001001010001010100010101000101010001"
print(int(text, 2))
print(int(text))