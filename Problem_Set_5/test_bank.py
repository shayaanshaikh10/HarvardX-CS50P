from bank import value

def test_0():
    assert value("hello, shayaan")==0
    assert value("HELLO, shayaan")==0
def test_20():
    assert value("how are you shayaan")==20
def test_100():
    assert value("what your name")==100