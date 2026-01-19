# ЗАДАНИЕ 1: Функции и условия

# 1. Создайте функцию calculate_total(price, tax_percent):
#    - возвращает итоговую цену с налогом
#    - если налог > 20% или цена < 0, возвращает сообщение об ошибке


def calculate_total(price, tax_percent):
    if price < 0 or tax_percent > 20:
        return "ошибка: некорректные входные данные"

    tax = price * (tax_percent / 100)
    total_price = price + tax
    return total_price


print(calculate_total(3000, 20))

# 2. Создайте функцию get_level(points):
#    - points >= 100 → "Эксперт"
#    - points >= 50 → "Продвинутый"
#    - points >= 20 → "Начинающий"
#    - иначе → "Новичок"


def get_level(points):
    match points:
        case p if p >= 100:
            return "Эксперт"
        case p if p >= 50:
            return "Продвинутый"
        case p if p >= 20:
            return "Начинающий"
        case _:
            return "Новичок"


print(get_level(120))
print(get_level(60))
print(get_level(30))
print(get_level(10))

# 3. Создайте функцию process_status(status) с match/case:
#    - "active" → "Статус активен"
#    - "inactive" → "Статус неактивен"
#    - "pending" → "Статус в ожидании"
#    - "blocked" → "Статус заблокирован"
#    - иначе → "Неизвестный статус"


def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"


print(process_status("blocked"))
