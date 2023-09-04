import random

dictionary = {}

for i in range(20):
    key = f'Element {i + 1}'
    value = random.randint(1, 100)
    dictionary[key] = value

print("Generated dictionary:")
for key, value in dictionary.items():
    print(f'{key}: {value}')

product = 1
for value in dictionary.values():
    product *= value

print(f'\nResult of multiplying all numbers: {product}')
