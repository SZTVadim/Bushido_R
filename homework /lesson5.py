# ЗАДАНИЕ 1: Работа с типами данных
word = "Привет"
print(type(word))
number = 42
print(type(number))
floatnumber = 3.14
print(type(floatnumber))
list = [1, 2, 3]
print(type(list))

# ЗАДАНИЕ 2: Преобразование регистра строк
x = "python PROGRAMMING"
print(x.lower())
print(x.upper())
print(x.capitalize())
print(x.title())

# ЗАДАНИЕ 3: Удаление пробелов
y = "  Hello World  "
print(y.strip())
print(y.lstrip())
print(y.rstrip())

# ЗАДАНИЕ 4: Разделение и объединение строк
z = "яблоко,банан,апельсин,груша"
newz = z.split(",")
print(newz)
newz2 = " | ".join(newz)
print(newz2)

# ЗАДАНИЕ 5: Замена подстрок
getstring = "Я изучаю Python. Python - это круто!"
new_getstring = getstring.replace("Python","Java")
print(new_getstring)

# ЗАДАНИЕ 6: Поиск и подсчет
new_new = "Python программирование на Python"
newtext = new_new.find("Python")
print(newtext)
newtext1 = "Python программирование на Python".count("Python")
print(newtext1)
print(new_new.find("Java"))

# ЗАДАНИЕ 7: Проверка типа символов
findtext = "Hello123"
print(findtext.isalnum())
findnumbers = "12345"
print(findnumbers.isdigit())
findtext2 = "Hello"
print(findtext2.isalpha())
findtabs = "   "
print(findtabs.isspace())

# ЗАДАНИЕ 8: Срезы строк

text8 = "Python very good"
print(text8[0:3])
print(text8[-3::])
print(text8[::2])
print(text8[:: -1])

# ЗАДАНИЕ 9: Экранирование символов
print("Он сказал: \"Привет\"")
print("Первая строка \nВторая строка")

# ЗАДАНИЕ 10: Добавление элементов в список
fruits = ['яблоко']
fruits.append('банан')
print(fruits)
fruits.extend(['апельсин', 'груша'])
print(fruits)
fruits.insert(1, 'виноград')
print(fruits)

# ЗАДАНИЕ 11: Удаление элементов из списка
fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
print(fruits)
fruits1 = ["яблоко", "банан", "апельсин", "банан"]
last = fruits1.pop()
print(last)
print(fruits1)

# ЗАДАНИЕ 12: Поиск элементов в списке
fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits.index("банан"))
print(fruits.count("банан"))

# ЗАДАНИЕ 13: Сортировка и реверс списка
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# БОНУСНОЕ 14: Комбинированная задача

names = "Иван,Петр,Мария,Анна"
newnames = names.split(",")
print(newnames)
newnames.append('Ольга')
print(newnames)
newnames.sort()
print(newnames)
strnames = ", ".join(newnames)
print(strnames)
