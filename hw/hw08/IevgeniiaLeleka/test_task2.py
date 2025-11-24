from task2 import validate_password
import unittest
from unittest.mock import patch

class TestPasswordValidation(unittest.TestCase):

    def test_multiple_passwords(self):

        test_cases = {
            "Ab1$ef": True,
            "A1b@cD": True,
            "abcDEF123$": True,
            "abcdef": False,
            "ABC123": False,
            "Ab1$": False,
            "Ab1$abcdefabcdefg": False,
            "Abcdef$": False,
            "12345$A": False,
            "abc1$def": False,
        }

        for pwd, expected in test_cases.items():
            with patch('builtins.input', return_value=pwd):
                result = validate_password()
                self.assertEqual(result, expected, msg=f"Failed for password: {pwd}")

if __name__ == "__main__":
    unittest.main()
