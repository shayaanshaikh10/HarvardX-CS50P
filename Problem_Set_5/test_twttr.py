from twttr import shorten
import pytest

def test_lowershorten():
    assert shorten("shayaan")=="shyn"

def test_uppershorten():
    assert shorten("SHAYAAN")=="SHYN"

def test_num():
    assert shorten("shayaan50")=="shyn50"

def test_punc():
    assert shorten("shayaan!")=="shyn!"