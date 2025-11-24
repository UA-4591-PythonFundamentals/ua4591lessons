def num_of_characters(word: str) -> dict:
    """Return the number of characters in a word."""
    result = {}
    for letter in word:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result
