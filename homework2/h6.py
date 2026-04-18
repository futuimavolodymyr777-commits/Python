import random

# 1 деление чисел
print("задание 1")

try:
    # ввод первого числа
    a = float(input("введи первое число: "))
    
    # ввод второго числа
    b = float(input("введи второе число: "))
    
    # делим
    result = a / b
    print("результат:", result)

except ValueError:
    print("ошибка: нужно вводить числа")

except ZeroDivisionError:
    print("ошибка: деление на ноль")

finally:
    print("задание 1 завершено")


# 2 список и индекс
print("\nзадание 2")

arr = [10, 20, 30, 40, 50]

try:
    # ввод индекса
    i = int(input("введи индекс: "))
    
    # вывод элемента
    print("элемент:", arr[i])

except ValueError:
    print("ошибка: индекс должен быть числом")

except IndexError:
    print("ошибка: нет такого индекса")

finally:
    print("задание 2 завершено")


# 3 сумма продаж
print("\nзадание 3")

try:
    # ввод строки
    data = input("введи числа через пробел: ")
    
    # делаем список чисел
    nums = []
    for x in data.split():
        nums.append(int(x))
    
    # сумма
    total = sum(nums)
    print("сумма:", total)

except ValueError:
    print("ошибка: введены не числа")

finally:
    print("задание 3 завершено")


# 4 корень числа
print("\nзадание 4")

try:
    # ввод числа
    n = float(input("введи число: "))
    
    # проверка минуса
    if n < 0:
        raise Exception("нельзя корень из отрицательного числа")
    
    print("корень:", n ** 0.5)

except ValueError:
    print("ошибка: не число")

except Exception as e:
    print("ошибка:", e)

finally:
    print("задание 4 завершено")


# 5 товар
print("\nзадание 5")

try:
    # ввод товара
    s = input("введи (название, цена, количество): ")
    
    parts = s.split(",")
    
    # проверка формата
    if len(parts) != 3:
        raise ValueError("неправильный формат")
    
    name = parts[0].strip()
    price = float(parts[1].strip())
    count = int(parts[2].strip())
    
    print("товар:", name, "принят")

except ValueError:
    print("ошибка ввода товара")

finally:
    print("задание 5 завершено")


# 6 подключение
print("\nзадание 6")

def connect_to_server():
    # рандом успех или ошибка
    if random.randint(0, 1) == 1:
        return "успешное подключение"
    else:
        raise ConnectionError("ошибка подключения")

try:
    print(connect_to_server())

except ConnectionError:
    print("не удалось подключиться к серверу")

finally:
    print("попытка завершена")