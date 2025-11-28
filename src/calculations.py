"""
Authors: Liam Cabarle and Destiny Louangsombath
Date: November 30, 2025
PROG71080 - Introduction to Programming with Python
Assignment 2
calculations.py

This file contains simple arithmetic calculations
"""

def add(a, b):
    """Returns the sum of a and b"""
    return a + b

def subtract(a, b):
    """Returns the difference between a and b"""
    return a - b

def multiply(a, b):
    """Returns the product of a and b"""
    return a * b

def divide(a, b):
    """
    Returns the quotient when dividing a with b
    Raises a zero division error when dividing by zero
    """
    if b == 0:
        raise ZeroDivisionError("Sorry you cannot divide by zero.")
    else:
        return a / b