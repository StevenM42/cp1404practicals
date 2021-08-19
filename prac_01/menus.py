"""
CP1404/CP5632 - Practical
Menu code
"""

name = input("Enter name: ")
MENU = """(H)ello
(G)oodbye
(Q)uit"""

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello {}".format(name))
    elif choice == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")
