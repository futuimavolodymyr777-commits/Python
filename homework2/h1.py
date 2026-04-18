import random

# задание 1 сдвиг списка
def task1():
    # ввод чисел
    nums = list(map(int, input("введи числа через пробел: ").split()))
    
    # ввод сдвига
    n = int(input("введи n: "))
    
    # нормализуем сдвиг
    n = n % len(nums)
    
    # делаем сдвиг
    res = nums[-n:] + nums[:-n]
    
    print("результат:", res)


# задание 2 работа со списками
def task2():
    # размер списков
    size = int(input("размер: "))
    
    # генерим списки
    a = [random.randint(1, 20) for _ in range(size)]
    b = [random.randint(1, 20) for _ in range(size)]
    
    print("список 1:", a)
    print("список 2:", b)
    
    # оба списка
    c1 = a + b
    print("1:", c1)
    
    # без повторов
    c2 = list(set(c1))
    print("2:", c2)
    
    # общие элементы
    c3 = list(set(a) & set(b))
    print("3:", c3)
    
    # только уникальные
    c4 = list(set(a) ^ set(b))
    print("4:", c4)
    
    # мин макс
    c5 = [min(a), max(a), min(b), max(b)]
    print("5:", c5)


# меню
def menu():
    while True:
        print("\n1 задание 1")
        print("2 задание 2")
        print("0 выход")
        
        ch = input("выбор: ")
        
        if ch == "1":
            task1()
        elif ch == "2":
            task2()
        elif ch == "0":
            print("выход")
            break
        else:
            print("ошибка")


menu()