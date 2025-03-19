
def return_42():
    return 42

def mult_method(a, b):
    return a * b


def test_F():
    assert True

def test_42():
    assert return_42() == 42

def test_mult_method_1():
    assert mult_method(2, 5) == 10

def test_mult_method_2():
    assert mult_method(4, 7) == 28