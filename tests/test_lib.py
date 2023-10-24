"""Trivial tests for the library.

To learn more about (non-trivial) tests, read Python testing with pytest:
https://pragprog.com/titles/bopytest2/
"""
import check_system


def test_addition() -> None:
    """Test the addition function by adding numbers.

    This test can be improved by using Hypothesis and define property based
    tests. https://hypothesis.readthedocs.io/
    """
    numbers_to_add = (1, 2, 3)

    assert check_system.add(*numbers_to_add) == 6
