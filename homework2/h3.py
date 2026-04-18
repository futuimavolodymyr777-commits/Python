# задание 1 вывод текста
def task1():
    # просто выводим текст
    print('"Don\'t compare yourself with anyone in this world..."')
    print('    if you do so, you are insulting yourself.')
    print('        Bill Gates')


# задание 2 четные числа
def task2():
    # ввод чисел
    a = int(input("введи первое число: "))
    b = int(input("введи второе число: "))
    
    # ищем четные
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()


# задание 3 квадрат
def task3():
    # ввод параметров
    size = int(input("размер: "))
    sym = input("символ: ")
    filled = input("заполненный? (true false): ").lower() == "true"
    
    # рисуем квадрат
    for i in range(size):
        if filled:
            print(sym * size)
        else:
            if i == 0 or i == size - 1:
                print(sym * size)
            else:
                print(sym + " " * (size - 2) + sym)


# задание 4 количество цифр
def task4():
    num = input("введи число: ")
    
    # считаем длину строки
    print("количество цифр:", len(num))


# задание 5 палиндром
def task5():
    num = input("введи число: ")
    
    # проверка
    if num == num[::-1]:
        print("true")
    else:
        print("false")


# меню
while True:
    print("\n1 текст")
    print("2 четные числа")
    print("3 квадрат")
    print("4 количество цифр")
    print("5 палиндром")
    print("0 выход")
    
    choice = input("выбор: ")
    
    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    elif choice == "4":
        task4()
    elif choice == "5":
        task5()
    elif choice == "0":
        print("выход")
        break
    else:
        print("ошибка")