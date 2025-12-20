# ЗАДАНИЕ 1: Работа со словарями и перебор элементов

student = {
    "name": "Ivan",
    "age": 20,
    "course": 2,
    "city": "Moscow"
}

print("Вывод всех ключей словаря:")
for key in student:
    print(key)

print("Вывод всех значений словаря:")
print(student["name"], student["age"], student["course"], student["city"])

print("используя цикл, вывести все пары:")
for key, value in student.items():
    print(f"{key} : {value}")

print("используя цикл, вывести все значения:")
for value in student.values():
    print(f"{value}")

# ЗАДАНИЕ 2: Удаление элементов и генератор словарей
prices = {"яблоко": 50, "банан": 30, "апельсин": 40, "груша": 35, "виноград": 60}

del prices["груша"]
print("Вывод удаление груши из словаря:", prices)

prices = {"яблоко": 50, "банан": 30, "апельсин": 40, "груша": 35, "виноград": 60}
param_remove = prices.pop("виноград")
print("Вывод сохранения переменной", param_remove,)
print("Вывод удаления винограда", prices)

prices = {"яблоко": 50, "банан": 30, "апельсин": 40, "груша": 35, "виноград": 60}
for key, value in prices.items():
    new_prices = value * 0.9
    print("Вывод цен со скидкой 10%:", (f"{key}: {new_prices}"))

# ЗАДАНИЕ 3: Объединение словарей
student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}
student1.update(student2)
print(student1)

student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}
student3 = {**student1, **student2}
print(student2)
print(student3)
