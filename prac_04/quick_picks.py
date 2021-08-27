"""
CP1404/CP5632 Practical
quick picks program
"""

import random

NUMBER_PER_LINE = 6
MIN = 1
MAX = 45

number_of_picks = 6
# number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    picks = []
    for j in range(NUMBER_PER_LINE):
        number = random.randint(MIN, MAX)
        while number in picks:
            number = random.randint(MIN, MAX)
        picks.append(number)
    picks.sort()
    for pick in picks:
        print("{:2}".format(pick), end=" ")
    print()
