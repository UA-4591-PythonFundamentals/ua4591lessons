import functions
import functions_with_errors

modules_to_test = [functions, functions_with_errors]

for mod in modules_to_test:
    print(f"\nTesting {mod.__name__}.py")

    try:
        result = mod.greeting_by_name("Alice")
        assert result == "Hello Alice!"
        print("Test greeting_by_name is Passed")
    except AssertionError:
        print("Test greeting_by_name is Failed")

    test_cases = [
        ("hello", "e", 2),
        ("hello", "z", "Not found"),
        ("hello", "ab", "Error! Symbol can be string with only one letter")
    ]
    for text, symbol, expected in test_cases:
        try:
            result = mod.get_symbol_position(text, symbol)
            assert result == expected
            print(f"Test get_symbol_position({text!r}, {symbol!r}) is Passed")
        except AssertionError:
            print(f"Test get_symbol_position({text!r}, {symbol!r}) is Failed")

    dict1 = {"a": 1}
    dict2 = {"b": 2}
    try:
        result = mod.merge(dict1.copy(), dict2.copy())
        assert result == {"a": 1, "b": 2}
        print("Test merge(dict1, dict2) is Passed")
    except AssertionError:
        print("Test merge(dict1, dict2) is Failed")

    try:
        mod.merge(dict1.copy(), dict2.copy())
        assert dict2 == {"b": 2}
        print("Test merge(dict2 immutability) is Passed")
    except AssertionError:
        print("Test merge(dict2 immutability) is Failed")
