## Summary of the podcast
- Software Engineering Radio, Episode 516: Brian Okken on Testing in Python with pytest
- Link to the podcast: https://se-radio.net/2022/06/episode-516-brian-okken-on-testing-in-python-with-pytest/

- Pytest is used by many in the python community because:
    - It helps developers read and write tests easier
    - has a flexible setup and teardown features
    - can mock anything and has plenty of plugins

- Topics from the podcast we want to focus on:
    - Proper test file naming
    - Fixtures
    - Parameterization

- Test naming convention
    - Must be in a folder called "tests"
    - Files must be named "test_insertname" (change insertname to your own test file name)
    - Python automatically finds the test files when they are correctly named

- Fixtures
    - Are a named thing
    - Reusable code for testing
    - Must have "@pytest.fixture" above the function to label it as a fixture

- Parameterization
    - Used to simulate different conditions for testing
    - Fixtures can be parameterized