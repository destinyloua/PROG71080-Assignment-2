# Authors: Liam Cabarle and Destiny Louangsombath
# Date: November 30, 2025
# PROG71080 - Introduction to Programming with Python
# Assignment 2
# calculations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Sorry you cannot divide by zero.")
    else:
        return a / b