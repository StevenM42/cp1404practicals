"""
CP1404/CP5632 - Practical
Password check program that returns asterisks of password length"""


def main():
    minimum_character_limit = 6

    password = get_password(minimum_character_limit)

    print('*' * len(password))


def get_password(minimum_character_limit):
    password = input("Please enter password at least {} characters long: ".format(minimum_character_limit))
    while len(password) < minimum_character_limit:
        password = input("Please enter password at least {} characters long: ".format(minimum_character_limit))
    return password


main()
