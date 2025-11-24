from largest_num import largest_num

def test_largest_num_positive_numbers():
    assert largest_num(10, 5) == 10

def test_largest_num_negative_numbers():
    assert largest_num(-10, -5) == -5

def test_largest_num_mixed_numbers():
    assert largest_num(5, -10) == 5

def test_largest_num_zero_and_pos():
    assert largest_num(0, 15) == 15

def test_largest_num_zero_and_neg():
    assert largest_num(-7, 0) == 0

def test_largest_num_equal_numbers():
    assert largest_num(25, 25) == 0
