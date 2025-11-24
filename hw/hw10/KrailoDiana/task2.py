class Human:

    species_name = "Homosapiens"

    def __init__(self, name):
        self.name = name
    
    def message(self):
        return f"Welcome {self.name}, I hope you are doing well."

    @classmethod
    def species(cls):
        return f"In fact, you are a member of the species \"{cls.species_name}\"."
    
    @staticmethod
    def static_message(species_name):
        return f"{species_name} " \
                    "have a highly developed brain, " \
                    "which determines the presence of consciousness, " \
                    "language, and abstract thinking. "
    
name = "Lukas"
h = Human(name)
print(h.message())
print(Human.species())
print(Human.static_message(Human.species_name))