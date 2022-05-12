import victory.victory as v

def test_random_array():
    random_integer_array = v.random_array(0, 10, 5)
    assert len(random_integer_array) == 5
    s_digits = set(random_integer_array)
    assert len(s_digits) == 5