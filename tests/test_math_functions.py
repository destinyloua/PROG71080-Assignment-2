from src.math_functions import add, add_squares

def test_add():
    assert add(1, 1) == 2

def test_add_squares(): 
    assert add_squares(2, 3) == 4 + 9 

def test_add_with_floats():
    assert add(1.1, 2.2) == 1.1 + 2.2