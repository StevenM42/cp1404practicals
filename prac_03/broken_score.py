"""
CP1404/CP5632 - Practical
Fixed program to determine score status
"""


def main():
    import random
    score = random.randint(1, 100)
    print(score)
    print(rate_score(score))


def rate_score(score):
    if 100 < score > 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

