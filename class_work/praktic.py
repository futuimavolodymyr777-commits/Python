print("МЕНЮ ЗАВДАНЬ XDDDD мармурову яловичину попрошу....")
print("1. Всі числа  2. Непарні  3. Парні (спадання)")
print("4. Порядок на вибір  5. Непарні (нормалізація)  6. Парні/Непарні")
print("0. Вихід")
print(".........")

task = int(input("Оберіть номер завдання: "))

if task == 0:
    print("Вихід.")

elif task == 1: # Завдання 1
    start = int(input("Початок: "))
    end = int(input("Кінець: "))
    for number in range(start, end + 1):
        print(number, end=" ")

elif task == 2: # Завдання 2
    start = int(input("Початок: "))
    end = int(input("Кінець: "))
    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number, end=" ")

elif task == 3: # Завдання 3
    start = int(input("Початок: "))
    end = int(input("Кінець: "))
    for number in range(end, start - 1, -1):
        if number % 2 == 0:
            print(number, end=" ")

elif task == 4: # Завдання 4
    start = int(input("Початок: "))
    end = int(input("Кінець: "))
    choice = int(input("1 - зростання, 2 - спадання: "))
    if choice == 1:
        for number in range(start, end + 1):
            print(number, end=" ")
    else:
        for number in range(end, start - 1, -1):
            print(number, end=" ")

elif task == 5: # Завдання 5
    num1 = int(input("Число 1: "))
    num2 = int(input("Число 2: "))
    if num1 > num2:
        start, end = num2, num1
    else:
        start, end = num1, num2
    
    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number, end=" ")

elif task == 6: # Завдання 6
    num1 = int(input("Число 1: "))
    num2 = int(input("Число 2: "))
    if num1 > num2:
        start, end = num2, num1
    else:
        start, end = num1, num2

    print("Парні:")
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number, end=" ")
    
    print("\nНепарні:")
    for number in range(end, start - 1, -1):
        if number % 2 != 0:
            print(number, end=" ")

else:
    print("Помилка.")