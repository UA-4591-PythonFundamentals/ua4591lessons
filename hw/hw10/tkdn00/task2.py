# TASK2

class Human():
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Hello, {self.name}")

    @classmethod
    def species(cls):
        return "It is a species of Homosapiens"

    @staticmethod
    def message():
        return "Message for TASK2"

# a = Human("Jack")
# a.welcome_message()
# print(a.species())
# print(a.message())