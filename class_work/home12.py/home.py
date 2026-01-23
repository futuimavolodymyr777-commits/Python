print("Виберіть завдання:")
print("1 - Сума і добуток трьох чисел")
print("2 - Площа ромба")
print("3 - Залишок грошей після виплат")
print("4 - Вартість поїздки на авто")
print("5 - Рахунок у ресторані")
print("6 - Оренда автомобіля")

choice = int(input("Введіть номер завдання: "))

# завдання 1
if choice == 1:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    c = int(input("Введіть третє число: "))

    print("Сума:", a + b + c)
    print("Добуток:", a * b * c)

# завдання 2
elif choice == 2:
    d1 = float(input("Введіть першу діагональ: "))
    d2 = float(input("Введіть другу діагональ: "))

    print("Площа ромба:", (d1 * d2) / 2)

# завдання 3
elif choice == 3:
    salary = float(input("Введіть зарплату: "))
    credit = float(input("Введіть платіж за кредитом: "))
    utilities = float(input("Введіть комунальні платежі: "))

    print("Залишок грошей:", salary - credit - utilities)

# завдання 4
elif choice == 4:
    distance = float(input("Введіть відстань (км): "))
    fuel = float(input("Витрата палива на 100 км: "))
    price = float(input("Ціна за літр: "))

    cost = distance * fuel / 100 * price
    print("Вартість поїздки:", cost)

# завдання 5
elif choice == 5:
    bill = float(input("Введіть суму рахунку: "))
    people = int(input("Введіть кількість осіб: "))

    tips = bill * 0.15
    total = bill + tips

    print("Чайові:", tips)
    print("Загальна сума:", total)
    print("З кожного:", total / people)

# завдання 6
elif choice == 6:
    price_day = float(input("Ціна оренди за день: "))
    days = int(input("Кількість днів: "))
    deposit = float(input("Застава: "))

    rent = price_day * days

    print("Загальна сума з заставою:", rent + deposit)
    print("Повернеться застава:", deposit)
    print("Ціна за один день:", rent / days)

else:
    print("Невірний номер завдання")
    