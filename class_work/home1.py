print("1 Кратні 7")
print("2 Робота з діапазоном")
print("3 Fizz Buzz")
print("4 Крок")
print("5 Добуток чисел")
print("6 Піднесення до степеня")

task = int(input("Обери завдання: "))

# завдання 1
if task == 1:
    a = int(input("Введи початок: "))
    b = int(input("Введи кінець: "))

    while a <= b:
        if a % 7 == 0:
            print(a)
        a = a + 1

# завдання 2
elif task == 2:
    a = int(input("Введи початок: "))
    b = int(input("Введи кінець: "))

    x = a
    while x <= b:
        print(x)
        x = x + 1

    x = b
    while x >= a:
        print(x)
        x = x - 1

    x = a
    while x <= b:
        if x % 7 == 0:
            print(x)
        x = x + 1

    count = 0
    x = a
    while x <= b:
        if x % 5 == 0:
            count = count + 1
        x = x + 1

    print("Кількість чисел, кратних 5:", count)

# завдання 3
elif task == 3:
    a = int(input("Введи початок: "))
    b = int(input("Введи кінець: "))

    while a <= b:
        if a % 3 == 0 and a % 5 == 0:
            print("Fizz Buzz")
        elif a % 3 == 0:
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        else:
            print(a)
        a = a + 1

# завдання 4
elif task == 4:
    a = int(input("Введи початок: "))
    b = int(input("Введи кінець: "))
    step = int(input("Введи крок: "))

    while a <= b:
        print(a)
        a = a + step

# завдання 5
elif task == 5:
    a = int(input("Введи початок: "))
    b = int(input("Введи кінець: "))

    if a > b:
        a, b = b, a

    result = 1
    found = 0

    while a <= b:
        if a % 4 == 0 and a % 6 != 0:
            result = result * a
            found = 1
        a = a + 1

    if found == 1:
        print("Добуток:", result)
    else:
        print("Підходящих чисел немає")

# завдання 6
elif task == 6:
    a = int(input("Введи число A: "))
    n = int(input("Введи степінь N: "))

    result = 1
    while n > 0:
        result = result * a
        n = n - 1

    print("Результат:", result)

else:
    print("Невірний номер завдання")