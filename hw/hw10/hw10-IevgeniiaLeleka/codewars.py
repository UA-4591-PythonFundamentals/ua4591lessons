# Regular Ball Super Ball

class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

# Color Ghost

import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(['white','yellow','purple','red'])

# Basic subclasses - Adam and Eve

class Human:
    def __init__(self):
        pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

# Classy Classes

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info=f"{name}s age is {age}"

# Building Spheres

from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4 / 3) * pi * self.radius ** 3
        return round(volume, 5)

    def get_surface_area(self):
        area = 4 * pi * self.radius ** 2
        return round(area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)

# Python's Dynamic Classes #1

def class_name_changer(cls, new_name):
    if not new_name or not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Invalid value provided")

    cls.__name__ = new_name
