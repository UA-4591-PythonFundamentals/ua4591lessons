class Human:
    def __init__(self, name):
        self.name = name
    
    def disp_msg(self):
        print(f"Hello, {self.name}")

    @classmethod
    def species(cls):
        return 'It is a species of "Homosapiens"'
    
    @staticmethod
    def arb_msg():
        return "Static method is colled"
    
h = Human("Eva")

h.disp_msg()
print(h.species())
print(h.arb_msg())