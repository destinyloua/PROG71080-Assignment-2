"""
Authors: Liam Cabarle and Destiny Louangsombath
Date: November 30, 2025
PROG71080 - Introduction to Programming with Python
Assignment 2
conftest.py

This is where fixtures are written for tests
"""

import pytest

@pytest.fixture
def sample_numbers():
    return (20, 5)

@pytest.fixture
def division_error_num():
    return (3, 0)