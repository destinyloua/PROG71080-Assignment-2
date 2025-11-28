# Authors: Liam Cabarle and Destiny Louangsombath
# Date: November 30, 2025
# PROG71080 - Introduction to Programming with Python
# Assignment 2

## Summary of the podcast
- Software Engineering Radio, Episode 516: Brian Okken on Testing in Python with pytest
- Link to the podcast: https://se-radio.net/2022/06/episode-516-brian-okken-on-testing-in-python-with-pytest/

- Pytest is used by many in the python community because:
    - It helps developers read and write tests easier
    - Has a flexible setup and teardown features
    - Can mock anything and has plenty of plugins

## Topics from the podcast we want to focus on:
- Proper test file naming
- Fixtures
- Parameterization

## Test naming convention
- Must be in a folder called "tests"
- Files must be named "test_insertname" (change insertname to your own test file name)
- Python automatically finds the test files when they are correctly named

## Fixtures
- Are a named thing
- Reusable code for testing
- Must have "@pytest.fixture" above the function to label it as a fixture

## Parameterization
- Used to simulate different conditions for testing
- Tests can be parameterized
- Parameterized test syntax example: "@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 2, 4), (3, 9, 12)])" must be included before the test is written
    - Note: change variables and parameters, "("a, b, expected", [(1, 2, 3), (2, 2, 4), (3, 9, 12)]" to fit your tests 

## two questions
- would making many tests 