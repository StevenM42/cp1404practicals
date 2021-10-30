"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    if n == 1:
        return s * n
    else:
        i = [s, s]
        e = " ".join(i)
        return e


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these

    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"

    test_car = Car()
    assert test_car.fuel == 0, "Car does not set fuel correctly"

# (don't change the tests, change the function!)

# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass


def sentence_formatting(phrase):
    """
    Format a phrase into a sentence, making start a capital and end with a period
    >>> sentence_formatting('hello')
    'Hello.'
    >>> sentence_formatting('It is an ex parrot')
    'It is an ex parrot.'
    >>> sentence_formatting('david Bowie')
    'David bowie.'
    """
    sentence = phrase.capitalize()
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()

doctest.testmod()