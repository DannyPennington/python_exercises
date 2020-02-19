import factorial
import pytest

def test_factorial_zero():
    assert factorial.factorial(0) == 0

def test_factorial_one():
    assert factorial.factorial(1) == 1

def test_factorial_neg():
    assert factorial.factorial(-1) == -1

def test_factorial_bigneg():
    assert factorial.factorial(-5) == -120

def test_factorial_ten():
    assert factorial.factorial(10) == 3628800