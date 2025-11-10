print(f"Importing all names from {__name__}.py")

t = 10
tt = 20
def print_info_for_third():
    print(f"This is {__name__}.py with t={t} and tt={tt}")


if __name__ == "__main__":
    print(f"{__name__}.py is being executed directly")
    print_info_for_third()

print(f"Global variables in {__name__}.py: {globals()}")
print(f"{__name__}.py has been imported")