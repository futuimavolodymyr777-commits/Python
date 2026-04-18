# 1 считаем финалку с скидкой
print("задание 1")

try:
    # вводим цену
    price = float(input("цена: "))
    
    # вводим скидку
    discount = float(input("скидка %: "))
    
    # считаем че по итогу выходит
    final_price = price - price * discount / 100
    print("итог:", final_price)

except ValueError:
    print("ты ввел не числа")

finally:
    print("1 задание готово")


# 2 перевод баксов в евро
print("\nзадание 2")

try:
    # сколько баксов
    dollars = float(input("баксы: "))
    
    # курс
    rate = float(input("курс: "))
    
    # если курс ноль то все ломается
    if rate == 0:
        raise Exception("курс не может быть ноль")
    
    # считаем евро
    euros = dollars * rate
    print("евро:", euros)

except ValueError:
    print("ввод кривой")

except Exception as e:
    print("ошибка:", e)

finally:
    print("2 задание конец")


# 3 средний балл
print("\nзадание 3")

try:
    # ввод оценок
    data = input("оценки: ")
    
    # делаем список чисел
    grades = []
    for x in data.split():
        grades.append(int(x))
    
    # считаем среднее
    avg = sum(grades) / len(grades)
    print("средний балл:", avg)

except ValueError:
    print("что-то не число")

except ZeroDivisionError:
    print("пустой список")

finally:
    print("готово")


# 4 банкомат
print("\nзадание 4")

balance = 1000

try:
    # сколько хотим снять
    amount = float(input("сумма: "))
    
    # если больше бабок или не кратно 10
    if amount > balance or amount % 10 != 0:
        raise Exception("нельзя так снимать")
    
    balance -= amount
    print("забрал деньги осталось:", balance)

except ValueError:
    print("ввел фигню")

except Exception as e:
    print("ошибка:", e)

finally:
    print("операция закончена")


# 5 заказ
print("\nзадание 5")

try:
    # номер заказа
    order = input("заказ: ")
    
    # проверка норм ли формат
    if not (order.startswith("ORD") and order[3:].isdigit()):
        raise Exception("не тот формат")
    
    print("заказ ок")

except Exception as e:
    print("ошибка:", e)

finally:
    print("проверка закончена")


# 6 список чисел с мусором
print("\nзадание 6")

try:
    # ввод
    data = input("числа: ")
    
    items = data.split()
    numbers = []
    
    # чистим мусор
    for x in items:
        try:
            numbers.append(float(x))
        except ValueError:
            print("мусор пропустили:", x)
    
    # если пусто будет ошибка
    total = sum(numbers)
    avg = total / len(numbers)
    
    print("сумма:", total)
    print("среднее:", avg)

except ZeroDivisionError:
    print("норм чисел нет")

finally:
    print("всё обработано")