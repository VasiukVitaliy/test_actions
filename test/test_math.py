from src.math_f import add, mul

def test_add():
    assert add(3,4) == 7
    assert add(0,0) == 0
    assert add(0, 1) == 1
    assert add(1,0) == 1
    assert add(-1, 2) == 1
    
def test_mul():
    assert add(3,4) == 12
    assert add(0,0) == 0
    assert add(0, 1) == 0
    assert add(1,0) == 0
    assert add(-1, 2) == -2