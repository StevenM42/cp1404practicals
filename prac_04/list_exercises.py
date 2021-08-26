"""
CP1404/CP5632 - Practical
list exercises
"""

numbers = []

for i in range(5):
    number = int(input("Input Number: "))
    numbers.append(number)

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
average = sum(numbers) / len(numbers)
print("The average of the numbers is", average)


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
