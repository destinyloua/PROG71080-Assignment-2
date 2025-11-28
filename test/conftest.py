# Authors: Liam Cabarle and Destiny Louangsombath
# Date: November 30, 2025
# PROG71080 - Introduction to Programming with Python
# Assignment 2
# conftest.py

# This is where we need to put fixtures
# File name was specific so pytest automatically discovers it

import pytest 
from src.calculations import add

@pytest.fixture
def sample_numbers():
    return (20, 5)
