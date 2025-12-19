class Human:

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species(cls):
        print("You are homosapiens")

    @staticmethod
    def arbitrary():
        print("Have a good day")

person = Human("Viacheslav")

person.welcome()

Human.species()

Human.arbitrary()

person.arbitrary()