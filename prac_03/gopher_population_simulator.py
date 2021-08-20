"""
CP1404/CP5632 - Practical
Gopher Population Simulator using random number generation
"""
import random

population = 1000
total_years = 10
current_year = 0
min_birth_rate = 0.1
max_birth_rate = 0.2
min_death_rate = 0.05
max_death_rate = 0.25

print('Welcome to the Gopher Population Simulator!')

while total_years > current_year:
    current_year += 1
    birth_rate = population * random.uniform(min_birth_rate, max_birth_rate)
    death_rate = population * random.uniform(min_death_rate, min_death_rate)
    population += birth_rate - death_rate
    print(f'{birth_rate:.0f} gophers were born. {death_rate:.0f} died.')
    print(f'Population: {population:.0f}')
    print(f'Year {current_year}')
