"""
CP1404/CP5632 Practical
Taxi simulation with menu
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_trip_cost = 0
    print("Let's Drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            taxi_list(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                current_taxi.drive(float(input("Drive how far? ")))
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
                total_trip_cost += current_taxi.get_fare()
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid Option")
        print("Bill to date: ${:.2f}".format(total_trip_cost))
        print(MENU)
        choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_trip_cost))
    print("Taxis are now:")
    taxi_list(taxis)


def taxi_list(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
