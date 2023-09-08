power_function = lambda x, y=2: x ** y
numbers = [1, 2, 3, 4, 5]
result = list(map(power_function, numbers))
print(result)

numbers1 = [1, 2, 3]
numbers2 = [2, 3, 4]

result = list(map(power_function, numbers1, numbers2))
print("Когда передаем два списка:")
print(result)

