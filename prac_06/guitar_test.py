"""
CP1404/CP5632 Practical
Testing Guitar class
"""

from prac_06.guitar import Guitar


def test():

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2000, 3000)

    print("{} get_age() - Expected {}. Got {}".format(gibson.name, 99, gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another_guitar.name, 21, another_guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(gibson.name, True, gibson.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))


test()
