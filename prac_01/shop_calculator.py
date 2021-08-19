"""
CP1404/CP5632 - Practical - Suggested Solution
Shop calculator program to determine total (discounted) price
"""

total = 0
number_of_items = int(input("Number of Items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of Items: "))
for i in range(number_of_items):
    price = float(input("Price of item {} :".format(i + 1)))
    total += price

if total > 100:
    total = total * 0.9

print("Total Price for {} items is ${:.2f}".format(number_of_items, total))
