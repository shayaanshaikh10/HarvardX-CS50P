from plates import is_valid

def test_len():
    assert is_valid("HELLOOOO") == False

def test_numplace():
    assert is_valid("AA22A") == False

def test_zero():
    assert is_valid("ABC05") == False

def test_space():
    assert is_valid("hello, world") == False

def test_beg():
    assert is_valid("H5") == False

def test_alphanum():
    assert is_valid("CS50") == True
    assert is_valid("H I") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS-50") == False
    assert is_valid("CS!50") == False
    assert is_valid("CS 50") == False