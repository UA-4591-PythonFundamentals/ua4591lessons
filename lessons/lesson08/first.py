# print(__name__)
# from math import sqrt 
# math = 42
# import math as m
# print(m.sqrt(16))
# print(math)  # should print 42
# print(sqrt(16))

# import sys
# from pprint import pprint
# pprint(sys.path)
# import second
# import second
# print(second.PI)
# print(second.PI_STRING)
# from second import PI, PI_STRING
# print(PI_STRING)
# import second
# print(PI)
# import math, sys as s, typing, os as operating_system
# print("first.py is being executed")
# print(dir())
# import math
# print(dir())
# from math import *
# print(dir())

# print(dir())
# # from second import *
# # from second import PI, PI_STRING, a, _a, __a
# print(dir())
# directory_before = [str(d) for d in dir()]
# print("Directory before import:", directory_before)
# from second_copy import *
# directory_after = [str(d) for d in dir()]
# print("Directory after import:", directory_after)
# new_items = set(directory_after) - set(directory_before)
# print("New items imported:", new_items)
# print(dir(str))


# print(f"Importing all names from {__name__}.py")
# import third
# from pprint import pprint
# print(f"Global variables in {__name__}.py: {globals()}")
# third.print_info_for_third()
# from third import print_info_for_third as pi4t
# pi4t()

# print(f"Executing in {__name__}.py")
# # import level_1.l1

# # print(level_1.l1.text)
# import level_1.l1 as level_1

# print(level_1.text)
# from level_1.level_2.l2 import text as l2_text

# print(l2_text)

# import level_1
# print(f"level_1: {level_1}")
# print(level_1.l1_text)
# print(level_1.l2_text)
# print(f"{__name__}.py has been executed")
# open("file1.txt", "w")
# import os
# from os import path

import sys
from pprint import pprint
pprint(sys.path)