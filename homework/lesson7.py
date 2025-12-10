import math
# Задача 1:
numbers = [x**3 for x in range(1, 8)]
print(numbers)
print(min(numbers))
print(max(numbers))

# Задача 2:
numbers2 = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
newlist = [x for x in numbers2 if x > 10]
print(newlist)

# Задача 3
cities = ["москва", "санкт-петербург", "казань"]
uppercities = [x.capitalize() for x in cities]
print(uppercities)