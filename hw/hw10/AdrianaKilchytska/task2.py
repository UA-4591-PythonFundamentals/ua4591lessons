class Human:

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def show_species(cls):
        print("You are homosapiens")

    @staticmethod
    def arbitrary_message():
        print("Have a great day")

person = Human("Tanya")

person.welcome_message()

Human.show_species()

Human.arbitrary_message()

person.arbitrary_message()