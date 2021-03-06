"""
CP1404/CP5632 Practical
Sort files based on extension
"""

import os
import shutil


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]

        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        shutil.move(filename, extension + '/' + filename)


main()
