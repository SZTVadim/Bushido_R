# ЗАДАНИЕ 1: Класс Book (Книга)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return self.title, self.author, self.pages

    def is_long(self):
        return self.pages >= 300


book1 = Book('Harry Potter 1', 'ДЖ. Роуллинг', 230)
book2 = Book('Harry Potter 2', 'ДЖ. Роуллинг', 250)
book3 = Book('Harry Potter 3', 'ДЖ. Роуллинг', 320)
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
print(book1.is_long())

# ЗАДАНИЕ 2: Класс BankAccount (Банковский счёт)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return amount  # для себя добавил

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Средств достаточно")  # для себя добавил
            return True
        else:
            print("Недостаточно средств")
            return False

    def get_balance(self):
        return self.balance


account = BankAccount("Ramil")

account.deposit(100)
print(account.withdraw(50))
print(account.withdraw(100))
print(account.get_balance())
