"""
CP1404/CP5632 Practical
Email and name check
"""


def main():
    email_and_name = {}
    email = input("Email: ")
    while email != "":
        name = retrieve_name(email)
        name_check = input("Is your name {}? (Y/N)".format(name))
        if name_check.upper() != "Y" and name_check != "":
            name = input("Name: ")
        email_and_name[email] = name
        email = input("Email: ")

    for email, name in email_and_name.items():
        print("{} ({})".format(name, email))


def retrieve_name(email):
    stripped_email = email.split('@')[0]
    split_name = stripped_email.split('.')
    name = " ".join(split_name)
    return name


main()
