# Меню
print("1 - Время")
print("2 - Круг")
print("3 - Приставки")
print("4 - Файл")
print("5 - Приветствие")
print("6 - Температура")

n = input("Выбор: ")

# 1. До полуночи
if n == "1":
    s = int(input("Секунды: "))
    left = 86400 - s
    h = left // 3600
    m = left % 3600 // 60
    sec = left % 60
    print(h, "ч", m, "м", sec, "с")

# 2. Круг
elif n == "2":
    d = float(input("Диаметр: "))
    r = d / 2
    c = input("1-пл 2-пер: ")
    if c == "1":
        print(3.14 * r * r)
    elif c == "2":
        print(3.14 * d)

# 3. Приставки
elif n == "3":
    p = float(input("Цена: "))
    k = int(input("Кол-во: "))
    d = float(input("Скидка %: "))
    np = p - p * d / 100
    c = input("1-сумма 2-цена: ")
    if c == "1":
        print(np * k)
    elif c == "2":
        print(np)

# 4. Файл
elif n == "4":
    gb = float(input("ГБ: "))
    sp = float(input("бит/с: "))
    t = gb * 1024 * 1024 * 1024 * 8 / sp
    c = input("1-ч 2-м 3-с: ")
    if c == "1":
        print(t / 3600)
    elif c == "2":
        print(t / 60)
    elif c == "3":
        print(t)

# 5. Приветствие
elif n == "5":
    h = int(input("Часы: "))
    if 0 <= h < 6:
        print("Good Night")
    elif 6 <= h < 13:
        print("Good Morning")
    elif 13 <= h < 17:
        print("Good Day")
    else:
        print("Good Evening")

# 6. Температура
elif n == "6":
    t = float(input("Темп: "))
    if t < -10:
        print("Дуже холодно")
    elif t < 0:
        print("Холодно")
    elif t < 15:
        print("Прохолодно")
    elif t < 25:
        print("Тепло")
    else:
        print("Спекотно")

else:
    print("Ошибка")
