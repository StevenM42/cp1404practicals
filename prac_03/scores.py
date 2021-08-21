"""
CP1404/CP5632 - Practical
Score status program produces random score and writes it to file
"""


def main():
    import random
    score = random.randint(1, 100)
    print(score, rate_score(score))


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
