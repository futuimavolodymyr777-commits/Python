print("МЕНЮ ЗАВДАНЬ XD")
print("1 всі числа в діапазоні")
print("2 всі непарні числа")
print("3 всі парні числа (спадання)")
print("4 числа за вибором порядку (1-зростання, 2-спадання)")
print("5 непарні числа з нормалізацією меж")
print("6 парні (зростання) та непарні (спадання) з нормалізацією")
print("0 вихід")
print("..........")

nomer_zavdannya = int(input("оберіть номер завдання: "))

# Завдання 1
if nomer_zavdannya == 1:
    print("Завдання 1")
    pochatok = int(input("Введіть початок: "))
    kinec = int(input("Введіть кінець: "))
    for chislo in range(pochatok, kinec + 1):
        print(chislo, end=" ")

# Завдання 2
elif nomer_zavdannya == 2:
    print("Завдання 2")
    pochatok = int(input("Введіть початок: "))
    kinec = int(input("Введіть кінець: "))
    for chislo in range(pochatok, kinec + 1):
        if chislo % 2 != 0:
            print(chislo, end=" ")

# Завдання 3
elif nomer_zavdannya == 3:
    print("Завдання 3")
    pochatok = int(input("Введіть початок: "))
    kinec = int(input("Введіть кінець: "))
    for chislo in range(kinec, pochatok - 1, -1):
        if chislo % 2 == 0:
            print(chislo, end=" ")

# Завдання 4
elif nomer_zavdannya == 4:
    print("Завдання 4")
    pochatok = int(input("Введіть початок: "))
    kinec = int(input("Введіть кінець: "))
    poryadok = int(input("Оберіть порядок (1 - зростання, 2 - спадання): "))
    if poryadok == 1:
        for chislo in range(pochatok, kinec + 1):
            print(chislo, end=" ")
    elif poryadok == 2:
        for chislo in range(kinec, pochatok - 1, -1):
            print(chislo, end=" ")

# Завдання 5
elif nomer_zavdannya == 5:
    print("Завдання 5")
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    if a > b:
        pochatok, kinec = b, a
    else:
        pochatok, kinec = a, b
    for chislo in range(pochatok, kinec + 1):
        if chislo % 2 != 0:
            print(chislo, end=" ")

# Завдання 6
elif nomer_zavdannya == 6:
    print("Завдання 6")
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    if a > b:
        pochatok, kinec = b, a
    else:
        pochatok, kinec = a, b
    
    print("Парні (зростання):")
    for chislo in range(pochatok, kinec + 1):
        if chislo % 2 == 0:
            print(chislo, end=" ")
    
    print("\nНепарні (спадання):")
    for chislo in range(kinec, pochatok - 1, -1):
        if chislo % 2 != 0:
            print(chislo, end=" ")

elif nomer_zavdannya == 0:
    print("Завершення роботи")

else:
    print("Такого завдання немає")