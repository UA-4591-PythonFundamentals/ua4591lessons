# # f = open("example_lesson14.txt", "w")

# # file = open("lessons/lesson14/example_users.txt")
# # print(type(file))
# # print(file.read())
# # file.close()
# # print(file.read(10))
# # print(file.tell())
# # print("---")
# # print(file.read(10))
# # print(file.tell())
# # print("---")
# # print(file.read(20))
# # print(file.tell())
# # print("---")
# # print(file.read(20))
# # print(file.tell())
# # print("---")
# # file.seek(0)
# # print(file.read(20))
# # print(file.tell())
# # print("---")

# # print(file.readline(), end="")
# # print(file.readline(), end="")
# # print(file.readlines(), end="")
# # for line in file:
# #     print("LINE FROM FILE:")
# #     print(f"\t{line}")
# # print("--- Using 'with' statement ---")
# # with open("lessons/lesson14/example_users.txt") as file:
# #     for line in file:
# #         print("LINE FROM FILE:")
# #         print(f"\t{line}")
# #     print("File is closed:", file.closed)

# # print("File is closed:", file.closed)
# # print("--- Without 'with' statement ---")
# # file =  open("lessons/lesson14/example_users.txt")
# # for line in file:
# #     print("LINE FROM FILE:")
# #     print(f"\t{line}")
# # print("File is closed:", file.closed)
# # file.close()
# # print("File is closed:", file.closed)

# with open("lessons/lesson14/example_users_temp.txt", "a+") as file:
#     text = file.read()
#     count = len(text)
#     print(text)
#     print("Number of characters in file:", count)
#     file.write("user1,pass1\n")
#     file.write("user2,pass2\n")
#     file.write("user3,pass3\n")
#     print("Current file position:", file.tell())
#     file.seek(count//2)
#     print("File position after seek:", file.tell())
#     file.write("INSERTED_TEXT\n")
#     file.writelines(["user4,pass4\n", "user5,pass5\n"])



