__all__ = ["PI_STRING", "__a", "_a"]

print(f"__name__ is {__name__}.py")
PI = 3.14159
PI_STRING = f"Value of PI is approximately {PI}"

a = 10
_a = 20
__a = 30

print(f"Variables defined in {__name__}.py: {dir()}")
print(f"{__name__}.py is being executed")