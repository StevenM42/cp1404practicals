"""
CP1404/CP5632 Practical
Guitars program.
"""

from prac_06.guitar import Guitar


def main():
    """Guitar program, using Guitar class."""

    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added")
        name = input("Name: ")


main()
