# class Ball(object):
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type

# tests = (Ball().ball_type, Ball('super').ball_type)

# for test in tests:
#     print(test)

# =========================================================================================================================================

# class Ghost(object):
#     def __init__(self):
#         import random as rn
#         x = rn.randint(0,3)
#         color_set = ("white", "yellow", "purple", "red")
#         self.color = color_set[x]
    
# ghost = Ghost()
# print(ghost.color)

# =========================================================================================================================================

# def God():
#     return [Man(), Woman()]

# class Human:
#     pass

# class Man(Human):
#     pass

# class Woman(Human):
#     pass

# paradise = God()
# print(isinstance(paradise[0], Man))

# =========================================================================================================================================

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @property    
#     def info(self):
#         return f"{self.name}s age is {self.age}"
    
# class Person: 
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 
#         self.info = f"{self.name}s age is {self.age}"
    
# john = Person("john", 34)
# print(john.info)

# names=["john","matt","alex","cam"]
# ages=[16,25,57,39]
# for i in range(4):
#     name,age=names[i],ages[i]
#     person=Person(name,age)
#     print(person.info)

# =========================================================================================================================================

# import math
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
        
#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         return round(4 / 3 * math.pi * self.radius ** 3, 5)
    
#     def get_surface_area(self):
#         return round(4 * math.pi * self.radius ** 2, 5)

#     def get_density(self):
#         return round(self.mass / self.get_volume(), 5)
    
# ball = Sphere(2,50)
# print(ball.get_radius())
# print(ball.get_volume())
# print(ball.get_density())

# =========================================================================================================================================


# def class_name_changer(cls, new_name):
#     if new_name is None or not new_name or not new_name[0].isupper() or not new_name.isalnum():
#         raise Exception("Invalid class name")
#     else: 
#         cls.__name__ = new_name
#         return cls


