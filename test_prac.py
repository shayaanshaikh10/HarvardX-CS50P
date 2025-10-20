# from prac import square
# import pytest


# def test_positive():
#     assert square(2)==4
#     assert square(3)==9

# def test_zero():
#     assert square(0)==0

# def test_negative():
#     assert square(-2)==4
#     assert square(-3)==9

# def test_str():
#     with pytest.raises(TypeError):
#         square("cat")


#testing for hello
from prac import hello

def test_argument():
    for name in ["shayaan", "bruce","batman"]:
        assert hello(name)==f"hello {name}"

def test_default():
    assert hello()=="hello world"