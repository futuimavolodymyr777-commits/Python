# Меню
print("1 - Сумма и произведение")
print("2 - Площадь ромба")
print("3 - Остаток зарплаты")
print("4 - Стоимость поездки")
print("5 - Счет в ресторане")
print("6 - Аренда авто")

n = input("Выбор: ")

# 1. Сумма и произведение
if n == "1":
    a = float(input("1: "))
    b = float(input("2: "))
    c = float(input("3: "))
    print("Сумма:", a + b + c)
    print("Произведение:", a * b * c)

# 2. Площадь ромба
elif n == "2":
    d1 = float(input("d1: "))
    d2 = float(input("d2: "))
    print("Площадь:", d1 * d2 / 2)

# 3. Остаток зарплаты
elif n == "3":
    salary = float(input("Зарплата: "))
    credit = float(input("Кредит: "))
    utilities = float(input("Коммунальные: "))
    print("Останется:", salary - credit - utilities)

# 4. Стоимость поездки
elif n == "4":
    km = float(input("Расстояние: "))
    fuel = float(input("Расход/100км: "))
    price = float(input("Цена за литр: "))
    print("Стоимость:", (km / 100) * fuel * price)

# 5. Счет в ресторане
elif n == "5":
    total = float(input("Сумма счета: "))
    people = int(input("Количество людей: "))
    tips = total * 0.15
    full = total + tips
    print("Чаевые:", tips)
    print("Итого:", full)
    print("С каждого:", full / people)

# 6. Аренда авто
elif n == "6":
    day_price = float(input("Цена за день: "))
    days = int(input("Дней: "))
    deposit = float(input("Залог: "))
    rent = day_price * days
    print("С залогом:", rent + deposit)
    print("Возврат залога:", deposit)
    print("Цена за день:", rent / days)

else:
    print("Ошибка")