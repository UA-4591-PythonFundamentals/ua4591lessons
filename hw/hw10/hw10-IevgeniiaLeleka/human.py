class Human:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello {self.name}!')

    @classmethod
    def show_species(cls):
        print('You are homosapiens.')

    @staticmethod
    def message():
        print("And you are awesome! Have a great day!")


if __name__ == '__main__':
    human = Human('Eve')
    human.greeting()
    Human.show_species()
    Human.message()
    human.message()
