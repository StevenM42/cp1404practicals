"""Password check program that returns asterisks of password length"""

Minimum_character_limit = 6

password = input("Please enter password at least {} characters long: ".format(Minimum_character_limit))

while len(password) < Minimum_character_limit:
    password = input("Please enter password at least {} characters long: ".format(Minimum_character_limit))

print('*' * len(password))
