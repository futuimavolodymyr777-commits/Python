print("оберіть завдання:")
print("1 - сума або добуток трьох чисел")
print("2 - максимум, мінімум або середнє арифметичне")
print("3 - оцінка від 1 до 5")
print("4 - переведення метрів")
print("5 - калькулятор")
print("6 - однакові чи різні цифри")

choice = int(input("введіть номер завдання: "))

# завдання 1
if choice == 1:
    a = float(input("введіть перше число: "))
    b = float(input("введіть друге число: "))
    c = float(input("введіть третє число: "))

    print("1 - сума")
    print("2 - добуток")
    action = int(input("оберіть дію: "))

    if action == 1:
        print("сума:", a + b + c)
    elif action == 2:
        print("добуток:", a * b * c)
    else:
        print("невірний вибір")

# завдання 2
elif choice == 2:
    a = float(input("введіть перше число: "))
    b = float(input("введіть друге число: "))
    c = float(input("введіть третє число: "))

    print("1 - максимум")
    print("2 - мінімум")
    print("3 - середнє арифметичне")
    action = int(input("оберіть дію: "))

    if action == 1:
        print("максимум:", max(a, b, c))
    elif action == 2:
        print("мінімум:", min(a, b, c))
    elif action == 3:
        print("середнє арифметичне:", (a + b + c) / 3)
    else:
        print("невірний вибір")

# завдання 3
elif choice == 3:
    grade = int(input("введіть оцінку від 1 до 5: "))

    if grade == 1:
        print("дуже погано")
    elif grade == 2:
        print("погано")
    elif grade == 3:
        print("задовільно")
    elif grade == 4:
        print("добре")
    elif grade == 5:
        print("відмінно")
    else:
        print("невірна оцінка")

# завдання 4
elif choice == 4:
    meters = float(input("введіть кількість метрів: "))

    print("1 - перевести в милі")
    print("2 - перевести в дюйми")
    print("3 - перевести в ярди")
    print("4 - перевести в милі, дюйми та ярди")
    print("5 - перевести в кілометри та сантиметри")
    action = int(input("оберіть варіант: "))

    if action == 1:
        print("милі:", meters / 1609.34)
    elif action == 2:
        print("дюйми:", meters * 39.37)
    elif action == 3:
        print("ярди:", meters * 1.0936)
    elif action == 4:
        print("милі:", meters / 1609.34)
        print("дюйми:", meters * 39.37)
        print("ярди:", meters * 1.0936)
    elif action == 5:
        print("кілометри:", meters / 1000)
        print("сантиметри:", meters * 100)
    else:
        print("невірний вибір")

# завдання 5
elif choice == 5:
    a = float(input("введіть перше число: "))
    b = float(input("введіть друге число: "))

    print("1 - додавання")
    print("2 - віднімання")
    print("3 - множення")
    print("4 - ділення")
    print("5 - залишок від ділення")
    print("6 - піднесення до степеня")
    action = int(input("оберіть операцію: "))

    if action == 1:
        print("результат:", a + b)
    elif action == 2:
        print("результат:", a - b)
    elif action == 3:
        print("результат:", a * b)
    elif action == 4:
        print("результат:", a / b)
    elif action == 5:
        print("результат:", a % b)
    elif action == 6:
        print("результат:", a ** b)
    else:
        print("невірна операція")

# завдання 6
elif choice == 6:
    number = int(input("введіть тризначне число: "))

    a = number // 100
    b = (number // 10) % 10
    c = number % 10

    if a == b == c:
        print("всі цифри однакові")
    else:
        print("цифри різні")

else:
    print("невірний номер завдання")