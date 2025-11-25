# Authors: Liam Cabarle and Destiny Louangsombath
# Date: November 30, 2025
# PROG71080 - Introduction to Programming with Python
# Assignment 2
import pytest 
from src.calculations import add
# This is where we need top put fixtures
# File name was specific so pytests automatically discovers it

@pytest.fixture
def sample_numbers():
    return (20, 5)
