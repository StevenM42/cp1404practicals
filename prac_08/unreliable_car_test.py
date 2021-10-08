"""
CP1404/CP5632 Practical
Unreliable car class test
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Unreliable car test"""

    test_car = UnreliableCar("Test Car", 100, 50)
    test_car.drive(50)
    print(test_car)


main()
