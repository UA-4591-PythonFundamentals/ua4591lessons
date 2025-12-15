import unittest

def greeting_by_name(name):
    return f"Hello name!"

def get_symbol_position(text, symbol):
    return text.find(symbol)

def merge(dict1, dict2):
    dict1.update(dict2)
    return dict1
    
class TestGreeting_by_nameFunction(unittest.TestCase):
    def test_by_name(self):
        result = greeting_by_name("Anna")
        self.assertEqual(result, "Hello Anna!", "Name mast be Anna")

    def test_empty_string(self):
        result = greeting_by_name("")
        self.assertEqual(result, "Hello !", "Mast be without name")


class TestGetSymbolPosition(unittest.TestCase):
    def test_incorrect_symbol(self):
        result = get_symbol_position("OOOp", "oo")
        self.assertEqual(result, "Error! Symbol can be string with only one letter", "Symbol must be 1 character")

    def test_not_found_symbol(self):
        result = get_symbol_position("eye", "o")
        self.assertEqual(result, "Not found", "'o' is not in 'eye'")

    def test_correct_symbol(self):
        result = get_symbol_position("hello", "o")
        self.assertEqual(result, 5, "Mast be 5")

    def test_case_symbol(self):
        text = "Hello"
        symbol = "h"
        self.assertEqual(get_symbol_position(text, symbol), "Not found")
    

class TestMergeFunction(unittest.TestCase):
    def test_success_merge(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        expected = {"a": 1, "b": 2, "c": 3, "d": 4}
        result = merge(dict1, dict2)
        self.assertEqual(result, expected)

    def test_immutability_dict1(self):
        dict1 = {"k": 1, "m": 2}
        dict1_before = dict1.copy()
        dict2 = {"o": 3}
        merge(dict1, dict2)
        self.assertEqual(dict1, dict1_before, "They must be the same")

    def test_immutability_dict2(self):
        dict1 = {"k1": 1, "t1": 8}
        dict2 = {"s": 3}
        dict2_before = dict2.copy()
        merge(dict1, dict2)
        self.assertEqual(dict2, dict2_before, "They must be the same")

    def test_empty_dict(self):
        dict1 = {"x": 10, "y": 20}
        dict2 = {}
        expected = {"x": 10, "y": 20}
        result = merge(dict1, dict2)
        self.assertEqual(result, expected)
        result = merge(dict2, dict1)
        self.assertEqual(result, expected)

    def test_thesame_dict(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"a": 10, "b": 20}
        expected = {"a": 10, "b": 20}
        result = merge(dict1, dict2)
        self.assertEqual(result, expected)

    def test_empty_dict(self):
        dict1 = {}
        dict2 = {}
        result = merge(dict1, dict2)
        self.assertEqual(result, {})

if __name__ == "__main__":
    unittest.main()