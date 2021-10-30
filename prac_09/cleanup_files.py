"""
CP1404/CP5632 Practical
Clean up files to be consistent
"""
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    initial_changed_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    previous_character = ""
    new_name = ""
    for i, character in enumerate(initial_changed_name):
        current_character = character
        if previous_character == "_" and current_character.islower():
            new_name += current_character.upper()
        elif previous_character == "(" and current_character.islower():
            new_name += current_character.upper()
        elif previous_character.islower() and current_character.isupper():
            new_name += "_{}".format(current_character)
        else:
            new_name += current_character
        previous_character = character
    return new_name


main()
