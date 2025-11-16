import math

def rect(l, w): return l * w
def tri(b, h): return 0.5 * b * h
def circ(r): return math.pi * r**2

shape = input("rectangle, triangle or circle? ")

if shape == "rectangle":
    print("Area =", rect(float(input("length: ")), float(input("width: "))))
elif shape == "triangle":
    print("Area =", tri(float(input("base: ")), float(input("height: "))))
elif shape == "circle":
    print("Area =", circ(float(input("radius: "))))
else:
    print("Unknown")