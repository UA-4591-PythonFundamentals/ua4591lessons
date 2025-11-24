class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def to_dict(self):
        return {"name": self.name, "email": self.email, "age": self.age}
    

def generate_random_user(count=5):
    import random
    first_names = ["Alice", "Bob", "Charlie", "Diana"]
    last_names = ["Smith", "Johnson", "Williams", "Jones"]
    users = []
    while len(users) < count:
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = f"{name.replace(' ', '.').lower()}@example.com"
        age = random.randint(18, 70)
        if any(user.name == name for user in users):
            continue
        users.append(User(name, email, age))
    return users