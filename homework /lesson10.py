# ЗАДАНИЕ 1:

# Дано множество фруктов:

fruits = {"яблоко", "банан"}
fruits.add("апельсин")
print(fruits)

fruits.update(["груша", "виноград"])
print(fruits)

fruits.discard("банан")
print(fruits)

fruits.discard("киви")
print(fruits)

# fruits.remove("киви")
# print(fruits)

delete_one = fruits.pop()
print(delete_one)
print(fruits)

# ЗАДАНИЕ 2*:

# У вас есть два множества студентов:
group1 = {"Иван", "Мария", "Петр", "Анна"}
group2 = {"Петр", "Анна", "Сергей", "Ольга"}

group3 = group2 & group1
print(group3)

group1.update(group2)
print(group1)

group1_unique = group1 - group2
print(group1_unique)
