def greeting_by_name(name):
    return f"Hello {name}!"


def get_symbol_position(text, symbol):
    if len(symbol) > 1:
        return "Error! Symbol can be string with only one letter"
    index = text.find(symbol)
    if index > -1:
        return index + 1
    return "Not found"


def merge(dict1, dict2):
    new_dict = dict1.copy()
    new_dict.update(dict2)
    return new_dict

import unittest

class TestGreetingByName(unittest.TestCase):

    def test_greeting_by_name(self):
        self.assertEqual(greeting_by_name("Alice"), "Hello Alice!")
        self.assertEqual(greeting_by_name("Bob"), "Hello Bob!")
        self.assertEqual(greeting_by_name(""), "Hello !")


class TestGetSymbolPosition(unittest.TestCase):

    def test_valid_symbol_found(self):
        self.assertEqual(get_symbol_position("hello", "h"), 1)
        self.assertEqual(get_symbol_position("hello", "o"), 5)

    def test_valid_symbol_not_found(self):
        self.assertEqual(get_symbol_position("hello", "x"), "Not found")

    def test_invalid_symbol_more_than_one_char(self):
        self.assertEqual(
            get_symbol_position("hello", "he"),
            "Error! Symbol can be string with only one letter"
        )

    def test_symbol_at_multiple_positions_first_only(self):
        self.assertEqual(get_symbol_position("banana", "a"), 2)


class TestMerge(unittest.TestCase):

    def test_merge_simple(self):
        self.assertEqual(
            merge({"a": 1}, {"b": 2}),
            {"a": 1, "b": 2}
        )

    def test_merge_overwrite(self):
        # dict2 overwrites dict1
        self.assertEqual(
            merge({"a": 1}, {"a": 99}),
            {"a": 99}
        )

    def test_original_dicts_not_modified(self):
        d1 = {"x": 1}
        d2 = {"y": 2}
        result = merge(d1, d2)

        # Result is correct
        self.assertEqual(result, {"x": 1, "y": 2})

        # d1 and d2 remain unchanged
        self.assertEqual(d1, {"x": 1})
        self.assertEqual(d2, {"y": 2})


if __name__ == "__main__":
    unittest.main()
