class Human:
    species = "Homosapiens" 

    def __init__(self, name):
        self.name = name     

    def welcome(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls):
        return f"This species is {cls.species}"

    @staticmethod
    def random_message():
        return "Have a great day!"
    

# ---- EXAMPLES OF USE ----
person1 = Human("Marta Kozak")
person2 = Human("John Doe")

print(person1.welcome())       
print(person2.welcome())       

print(Human.get_species())     

print(Human.random_message()) 
