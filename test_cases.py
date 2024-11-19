# Test cases for student_code.py

import pytest
from student_code import add_numbers, multiply_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(2, 3) == -1
    assert subtract_numbers(-1, 3) == -4
    assert subtract_numbers(0, 10) == -10
    assert subtract_numbers(5, 1) == 4
    assert subtract_numbers(5, 5) == 0

def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-1, 3) == -3
    assert multiply_numbers(0, 10) == 0
