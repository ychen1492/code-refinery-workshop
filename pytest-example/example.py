def add(a, b):
    return a + b


def test_add():
    #assert -2 == 5
    #assert add(2, 3) == 5
    #assert add('space', 'ship') == 'spaceship'
    assert abs(add(0.1, 0.2) - 0.3) < 1e-5
