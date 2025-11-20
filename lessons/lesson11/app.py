
from utils import generate_users


if __name__ == "__main__":
    sample_user_data = [
        ("alice", 30),
        ("bob", -5),        # Invalid age
        ("charlie", 25),
        ("dave", "twenty")  # Invalid age type
    ]
    users = generate_users(sample_user_data)
    print(f"Generated {len(users)} valid users.")