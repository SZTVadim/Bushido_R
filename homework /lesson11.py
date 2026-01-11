# ЗАДАНИЕ 1: Работа с кортежами

# Дано:
coordinates = (10, 20, 30, 20, 10, 20, 40)

# 1. Выведите первый элемент кортежа
print(coordinates[0])
# 2. Выведите последний элемент кортежа
print(coordinates[-1])
# 3. Выведите срез с 2-го по 4-й элемент (включительно)
print(coordinates[1:4])
# 4. Проверьте, есть ли число 30 в кортеже (используйте оператор in)
print(30 in coordinates)
# 5. Найдите индекс первого вхождения числа 20
print(coordinates.index(20))
# 6. Подсчитайте, сколько раз встречается число 20
print(coordinates.count(20))
# 7. Подсчитайте, сколько раз встречается число 50 (его нет в кортеже)
print(coordinates.count(50))
# 8. Выведите длину кортежа
print(len(coordinates))

# ЗАДАНИЕ 2: Операции с кортежами

# Дано:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
numbers = [10, 20, 30, 40, 50]

# 1. Объедините tuple1 и tuple2 в один кортеж
unique_tuple = tuple1 + tuple2
print(unique_tuple)

# 2. Создайте кортеж, где элементы tuple1 повторяются 3 раза
triple_tuple = tuple1 * 3
print(triple_tuple)

# 3. Распакуйте tuple1 в три переменные a, b, c
a, b, c = tuple1
print(a, b, c)

# 4. Распакуйте numbers (преобразовав в кортеж) так, чтобы:
#    - первый элемент был в переменной first
#    - последний элемент был в переменной last
#    - все средние элементы были в списке middle
first, *middle, last = numbers
print(first, middle, last)

# 5. Преобразуйте список numbers в кортеж
numbers_tupple = tuple(numbers)
print(numbers_tupple)

# 6. Создайте кортеж из четных чисел от 0 до 10 (используйте генератор)
tuple_6 = tuple(x for x in range(0, 11) if x % 2 == 0)
print(tuple_6)

# 7. Создайте кортеж квадратов чисел от 1 до 5 (используйте генератор)
tuple_7 = tuple(x ** 2 for x in range(1, 6))
print(tuple_7)

# 8. Создайте кортеж из одного элемента со значением 42
tuple_8 = (42, )
print(tuple_8)
