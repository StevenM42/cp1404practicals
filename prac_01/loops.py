"""
CP1404/CP5632 - Practical
Counting with Loops
"""

# Counting odd numbers from 1 tp 20
for i in range(1, 21, 2):
    print(i, end='')
print()

# Counting up by tens from 0 to 100
for i in range(0, 101, 10):
    print(i, end='')
print()

# Counting down by one from 20 to 1
for i in range(20, 0, -1):
    print(i, end='')
print()

# Display requested number as stars
star_count = int(input("Number: "))
for i in range(star_count):
    print('*', end=' ')
print()

# Display stars counting up from one to requested number as stars
# star_count2 = int(input("Number: "))
for i in range(1, star_count + 1):
    print('*' * i)
print()
