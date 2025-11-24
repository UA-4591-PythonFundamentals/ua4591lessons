from num_of_characters import num_of_characters

def test_single_character():
    assert num_of_characters("a") == {"a": 1}

def test_multiple_unique_characters():
    assert num_of_characters("abc") == {"a": 1, "b": 1, "c": 1}

def test_repeated_characters():
    assert num_of_characters("aabbc") == {"a": 2, "b": 2, "c": 1}

def test_empty_string():
    assert num_of_characters("") == {}

def test_mixed_case():
    assert num_of_characters("AaA") == {"A": 2, "a": 1}

def test_with_spaces():
    assert num_of_characters("a a") == {"a": 2, " ": 1}

def test_with_special_characters():
    assert num_of_characters("a!a?") == {"a": 2, "!": 1, "?": 1}
