"""
CP1404/CP5632 Practical
Car class test
"""

from prac_08.taxi import Taxi


def main():
    """Taxi class test"""
    taxi_1 = Taxi("Prius 1", 100)
    taxi_1.drive(40)
    print(taxi_1)
    taxi_1.start_fare()
    taxi_1.drive(100)
    print(taxi_1)


main()
