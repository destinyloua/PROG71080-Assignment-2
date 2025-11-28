# Authors: Liam Cabarle and Destiny Louangsombath
# Date: November 30, 2025
# PROG71080 - Introduction to Programming with Python
# Assignment 2
# test_calculation.py
import pytest 
from src.calculations import add, subtract, multiply, divide

# tests using fixture

def test_add_fixture(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 25

def test_subtract_fixture(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 15

def test_multiply_fixture(sample_numbers):
    a, b = sample_numbers
    assert multiply(a, b) == 100

def test_divide_fixture(sample_numbers):
    a, b = sample_numbers
    assert divide(a, b) == 4

# parametrized tests

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 2, 4), (3, 9, 12)])
def test_add_param(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(10, 5, 5), (2, 2, 0), (22, 4, 18)])
def test_subtract_param(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(5, 5, 25), (2, 10, 20), (3, 9, 27)])
def test_multiply_param(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(2, 2, 1), (10, 2, 5), (30, 10, 3)])
def test_divide_param(a, b, expected):
    assert divide(a, b) == expected