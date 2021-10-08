"""
CP1404/CP5632 Practical
Silver service Taxi class test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Silver Taxi", 100, 2)
    taxi.drive(50)
    print(taxi)
    print(taxi.get_fare())


main()
