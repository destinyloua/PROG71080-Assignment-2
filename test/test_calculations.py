# Authors: Liam Cabarle and Destiny Louangsombath
# Date: November 30, 2025
# PROG71080 - Introduction to Programming with Python
# Assignment 2

import pytest 
from src.calculations import add, subtract, multiply, divide

def test_add(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 25

def test_subtract(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 15

def test_multiply(sample_numbers):
    a, b = sample_numbers
    assert multiply(a, b) == 100

def test_divide(sample_numbers):
    a, b = sample_numbers
    assert divide(a, b) == 4