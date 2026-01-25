print("1.Сума 2.Факторіал 3.Лінія*  4.Лінія_симв 5.Мін/Макс 6.Кальькулятор")
task = int(input("Оберіть номер завдання: "))

# Завдання 1
if task == 1:
    a = int(input("Від: "))
    b = int(input("До: "))
    s = 0
    n = 0
    for x in range(a, b + 1):
        s = s + x
        n = n + 1
    print("Сума:", s)
    print("Середнє:", s / n)

# Завдання 2
elif task == 2:
    num = int(input("Число: "))
    f = 1
    for x in range(1, num + 1):
        f = f * x
    print("Факторіал:", f)

# Завдання 3
elif task == 3:
    L = int(input("Довжина лінії: "))
    for x in range(L):
        print("*", end="")
    print()

# Завдання 4
elif task == 4:
    L = int(input("Довжина лінії: "))
    s = input("Символ: ")
    for x in range(L):
        print(s, end="")
    print()

# Завдання 5
elif task == 5:
    while True:
        print("\n1.Знайти мінімум\n2.Знайти максимум\n3.Вихід")
        op = int(input("Ваш вибір: "))
        if op == 3:
            print("Вихід...")
            break
        elif op == 1 or op == 2:
            n1 = int(input("Число 1: "))
            n2 = int(input("Число 2: "))
            if op == 1:
                if n1 < n2: print("Менше:", n1)
                else: print("Менше:", n2)
            else:
                if n1 > n2: print("Більше:", n1)
                else: print("Більше:", n2)
        else:
            print("Помилка!")

# Завдання 6
elif task == 6:
    while True:
        print("\n1.Додати\n2.Відняти\n3.Поділити\n4.Вихід")
        op = int(input("Оберіть операцію: "))
        if op == 4:
            print("Вихід...")
            break
        elif op in [1, 2, 3]:
            n1 = float(input("Перше число: "))
            n2 = float(input("Друге число: "))
            if op == 1: print("Результат:", n1 + n2)
            elif op == 2: print("Результат:", n1 - n2)
            elif op == 3:
                if n2 != 0: print("Результат:", n1 / n2)
                else: print("Помилка: ділення на нуль!")
        else:
            print("Помилка!")