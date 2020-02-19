import pytest
import count

def test_count_zero():
    assert count.count([0,1,5,7,0,8],2) == 0

def test_count_string():
    assert count.count(["a","b","c","s","c"], "c") == 2

def test_count_float():
    assert count.count([1.4,2.84,24.597,85.334324], 2.84) == 1

def test_count_bool():
    assert count.count([True, False, True, True], True) == 3