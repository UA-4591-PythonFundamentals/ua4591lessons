def count_chars(s):
    """Count characters in a string and return the results"""
    return {c: s.count(c) for c in s}

print(count_chars("hello"))