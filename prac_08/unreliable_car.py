"""
CP1404/CP5632 Practical
Unreliable car class
"""

from random import randint
from prac_08.car import Car


class UnreliableCar(Car):
    """Unreliable car class"""

    def __init__(self, name, fuel, reliability):
        """Initialise a Unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """drive a car with possibility of failure"""
        reliability_chance = randint(0, 100)
        if reliability_chance >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
