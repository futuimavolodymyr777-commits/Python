# Меню заданий
print("1 - Четное / нечетное")
print("2 - Кратность 7")
print("3 - Большее число")
print("4 - Меньшее число")
print("5 - Операции")
print("6 - Валюта")

n = input("Выбор: ")

# 1. Четное или нечетное
if n == "1":
    a = int(input("Число: "))
    if a % 2 == 0:
        print(a, "Even number")
    else:
        print(a, "Odd number")

# 2. Кратно ли 7
elif n == "2":
    a = int(input("Число: "))
    if a % 7 == 0:
        print(a, "Number is multiple 7")
    else:
        print(a, "Number is not multiple 7")

# 3. Большее
elif n == "3":
    a = int(input("Первое: "))
    b = int(input("Второе: "))
    if a > b:
        print("Большее:", a)
    else:
        print("Большее:", b)

# 4. Меньшее
elif n == "4":
    a = int(input("Первое: "))
    b = int(input("Второе: "))
    if a < b:
        print("Меньшее:", a)
    else:
        print("Меньшее:", b)

# 5. Операция
elif n == "5":
    a = float(input("Первое: "))
    b = float(input("Второе: "))
    print("1 +  2 -  3 *  4 ср.")
    op = input("Опер.: ")
    if op == "1":
        print(a + b)
    elif op == "2":
        print(a - b)
    elif op == "3":
        print(a * b)
    elif op == "4":
        print((a + b) / 2)

# 6. Валюта
elif n == "6":
    usd = float(input("USD: "))
    cur = input("Валюта: ")
    rate = float(input("Курс: "))
    print(usd * rate, cur)

else:
    print("Ошибка")
