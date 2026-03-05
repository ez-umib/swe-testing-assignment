from app.calculator import calculator

def test_full_addition_flow():
    calc = Calculator()
    result = calc.add(5, 3)
    assert result == 8

def test_clear_function():
    calc = Calculator()
    result = calc.clear()
    assert result == 0