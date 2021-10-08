"""
CP1404/CP5632 Practical
Silver service Taxi class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes a higher fare costs."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super(SilverServiceTaxi, self).__str__(), self.flagfall)

    def get_fare(self):
        return super(SilverServiceTaxi, self).get_fare() * self.fanciness
