class Human():
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome {self.name}!")

    @classmethod
    def info_species(cls):
        print(f"You are a species of {cls.species}")
              
    @staticmethod
    def arbitary_message(message):
        return print(f"This is static method and the message is: {message}. ") 


person = Human("Jack")
person.welcome_message()
person.info_species() 
person.arbitary_message("Hi there!")