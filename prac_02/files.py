"""
CP1404/CP5632 - Practical
Various methods to read or write to files
"""

name = input("Name: ")

# Part 1
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()

# Part 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# Part 3.1
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# Part 3.2
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total = total + number
in_file.close()
print(total)
