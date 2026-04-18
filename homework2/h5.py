# нсд рекурсией простым способом
def gcd(a, b):
    # если второе число стало ноль значит нашли ответ
    if b == 0:
        return a
    
    # иначе меняем местами и берём остаток
    result = gcd(b, a % b)
    return result


# сумма цифр числа рекурсией
def sum_digits(n):
    # если число закончилось возвращаем ноль
    if n == 0:
        return 0
    
    # берём последнюю цифру
    last_digit = n % 10
    
    # убираем последнюю цифру
    remaining = n // 10
    
    # складываем текущую цифру и результат дальше
    result = last_digit + sum_digits(remaining)
    return result


# проверка симметрии списка
def is_symmetric(arr):
    # если 0 или 1 элемент значит симметрия есть
    if len(arr) <= 1:
        return True
    
    # первый и последний элемент сравниваем
    first = arr[0]
    last = arr[-1]
    
    # если не равны значит не симметрия
    if first != last:
        return False
    
    # убираем края и проверяем дальше
    middle = arr[1:-1]
    result = is_symmetric(middle)
    return result


# проверка работы функций
print("нсд", gcd(48, 18))
print("сумма цифр", sum_digits(123))
print("симметрия 1", is_symmetric([1, 2, 3, 2, 1]))
print("симметрия 2", is_symmetric([1, 2, 3]))